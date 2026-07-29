"""Minimal MCP-style JSON-RPC server with one tool: unit_convert."""
import json
import sys

TOOLS = [
    {
        "name": "unit_convert",
        "description": "Convert SI-compatible length/energy units.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "value": {"type": "number"},
                "from_unit": {"type": "string"},
                "to_unit": {"type": "string"},
            },
            "required": ["value", "from_unit", "to_unit"],
            "additionalProperties": False,
        },
    }
]

CONVERSIONS = {
    ("m", "cm"): 100.0,
    ("cm", "m"): 0.01,
    ("m", "km"): 0.001,
    ("km", "m"): 1000.0,
    ("eV", "J"): 1.602176634e-19,
    ("J", "eV"): 1 / 1.602176634e-19,
}


def unit_convert(value: float, from_unit: str, to_unit: str):
    if from_unit == to_unit:
        return {"value": value, "unit": to_unit}
    key = (from_unit, to_unit)
    if key not in CONVERSIONS:
        return {"error": f"Unsupported conversion: {from_unit} -> {to_unit}"}
    return {"value": value * CONVERSIONS[key], "unit": to_unit}


def respond(req_id, result=None, error=None):
    msg = {"jsonrpc": "2.0", "id": req_id}
    if error is not None:
        msg["error"] = {"code": -32000, "message": error}
    else:
        msg["result"] = result
    sys.stdout.write(json.dumps(msg) + "\n")
    sys.stdout.flush()


def handle(request):
    method = request.get("method")
    req_id = request.get("id")
    params = request.get("params", {})

    if method == "initialize":
        respond(req_id, {
            "serverInfo": {"name": "skeleton-mcp-server", "version": "0.1.0"},
            "capabilities": {"tools": {"listChanged": False}},
        })
    elif method == "tools/list":
        respond(req_id, {"tools": TOOLS})
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name != "unit_convert":
            respond(req_id, error=f"Unknown tool: {name}")
            return
        try:
            out = unit_convert(float(args["value"]), str(args["from_unit"]), str(args["to_unit"]))
            respond(req_id, {"content": [{"type": "json", "json": out}]})
        except KeyError as exc:
            respond(req_id, error=f"Missing required field: {exc}")
    else:
        respond(req_id, error=f"Unsupported method: {method}")


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
        except json.JSONDecodeError:
            continue
        handle(request)


if __name__ == "__main__":
    main()
