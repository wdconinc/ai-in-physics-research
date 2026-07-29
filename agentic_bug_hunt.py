"""Broken ~60-line agentic loop used for debugging exercises."""
import random


def tool_search_papers(query):
    if "rare" in query:
        return []  # BUG 1: silent empty result instead of explicit failure
    return [f"paper-{i}:{query}" for i in range(3)]


def fake_llm(prompt):
    if len(prompt) > 280:
        raise RuntimeError("token limit exceeded")
    return "summary:" + prompt[-60:]


def run_pipeline(question, iterations=6):
    # BUG 3: no random seed, output differs run-to-run
    history = ""
    decisions = ["broaden", "narrow", "rephrase"]

    for i in range(iterations):
        step = random.choice(decisions)
        query = f"{question} | strategy={step}"
        if i == 2:
            query = "rare-event " + query

        papers = tool_search_papers(query)
        if not papers:
            print(f"iter={i} papers=0 (continuing silently)")
            continue

        joined = "\n".join(papers)
        history += f"\n[ITER {i}] query={query}\n{joined}\n"

        # BUG 2: unbounded context accumulation overflows at/near iteration 4
        prompt = f"You are a physics assistant. Use context:\n{history}\nAnswer briefly."
        answer = fake_llm(prompt)
        print(f"iter={i} answer={answer[:50]!r}")


if __name__ == "__main__":
    run_pipeline("quantum oscillation constraints")
