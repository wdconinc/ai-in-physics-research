# Week 11 Debate Brief — FOR the Motion

**Motion:** "An LLM-generated figure in a physics paper requires explicit caption-level disclosure, not just a methods-section statement."

**Your position:** Disclosure belongs where the reader meets the figure. A methods-only statement is necessary but not sufficient.

!!! note "Scope — define it before the other side does"
    "LLM-generated" covers a spectrum: (a) generative-AI imagery (schematics, illustrations), (b) plots whose code an LLM wrote, (c) plots where an LLM chose the analysis, binning, or fit. Argue that the caption line scales with the case — one clause for (b), more for (a) and (c) — but is never zero.

## Core arguments

1. **Figures travel without their papers.** Figures are extracted into talks, review articles, press releases, theses, and image search. The caption travels with the figure; the methods section does not. Disclosure that is lost on first reuse is not disclosure.
2. **Readers read figures first.** Most readers look at the abstract, figures, and captions, and many never reach the methods. A statement the typical reader does not see fails the purpose of transparency.
3. **Figures carry evidential weight.** A plot is read as a direct record of data. LLM failure modes — plausible but wrong axis scaling, silently dropped points, invented error bars, physically impossible schematics — are precisely the kind a reader will not suspect unless prompted.
4. **Physics already puts provenance in captions.** "Simulation", "Preliminary", "Adapted from Ref. [12]", "Curves are guides to the eye", "Statistical errors only". AI provenance is the same category of information: it tells the reader how much to trust what they see.
5. **Specificity enables verification.** A blanket methods sentence ("AI tools were used in preparing this manuscript") does not say *which* figure. A caption-level note tells a referee exactly where to look harder.
6. **The cost is one clause.** "Plotting code generated with an LLM and verified against [X]" is under 15 words. The asymmetry between cost and benefit favours disclosure.

## Policy anchors (verify against the primary sources before citing)

- **Nature portfolio:** restricts generative-AI images and requires permitted exceptions to be labelled as AI-generated — i.e., labelling at the image itself, not only in methods.
- **Science journals / Elsevier:** restrict AI-generated images and require explicit disclosure where allowed; both treat images more strictly than text.
- **Course AI policy:** "When in doubt, disclose more rather than less."
- **Trend:** publisher rules for images are consistently stricter than for text. Caption-level disclosure is where the norm is heading; physics should set it rather than inherit it.

## Expect these attacks — and answer them

| They will say | You answer |
|---|---|
| "We don't disclose matplotlib or Mathematica in captions." | Those tools are deterministic: same input, same output, and the author specified every element. An LLM makes unrequested choices. Disclosure tracks *who made the decisions*, not which software ran. |
| "Authors are responsible either way." | Responsibility assigns blame after an error is found. Disclosure helps find the error in the first place. |
| "Labels stigmatise honest authors." | Stigma falls when labelling is universal. Hidden use discovered later is what destroys trust. |
| "Where do you draw the line — autocomplete?" | Line-drawing is hard for every norm (authorship, plagiarism). A workable test: did the LLM make a choice that affects what the reader sees? |

## Questions to press

- If a figure from your paper appears on a conference slide, how does the audience learn it was LLM-generated?
- If methods-only is enough for AI, why do we write "simulation" in captions?

---

*This brief was drafted with an LLM assistant and is deliberately one-sided. Check every policy claim against the current publisher pages before using it in the debate.*
