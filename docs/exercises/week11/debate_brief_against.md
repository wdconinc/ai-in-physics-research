# Week 11 Debate Brief — AGAINST the Motion

**Motion:** "An LLM-generated figure in a physics paper requires explicit caption-level disclosure, not just a methods-section statement."

**Your position:** Disclose fully — in the methods section, where it can be done properly. You are *not* arguing against disclosure; you are arguing that a mandatory caption label is the wrong instrument.

!!! note "Scope — make the other side define its terms"
    "LLM-generated" covers a spectrum: (a) generative-AI imagery, (b) plots whose code an LLM wrote, (c) plots where an LLM chose the analysis. Concede (a) if needed — several publishers already restrict it — and fight on (b) and (c), which is where almost all real physics use sits.

## Core arguments

1. **The motion's category is not well defined.** Is a figure "LLM-generated" if Copilot completed one line of the plotting script? If an LLM suggested the colour map? If it wrote the script and the author rewrote half? A requirement that cannot be applied consistently will be applied arbitrarily.
2. **Captions describe content; methods describe process.** A caption tells the reader what the axes, symbols, and curves mean. How the figure was produced — software, fitting code, analysis chain — is methods material, and we do not caption-credit matplotlib, ROOT, or the student who wrote the script.
3. **Correctness does not depend on who typed the code.** A plot is right if the data and the code are right. The remedy for a wrong figure is released code and data, not a label. A label on an irreproducible figure verifies nothing.
4. **Methods disclosure is more informative.** A methods statement can give tool, version, date, what was generated, and how it was validated. A caption clause can only say "AI was used" — a warning without content.
5. **Accountability is already complete.** Publishers that allow AI tools hold authors fully responsible for all content. No responsibility gap exists for a caption label to fill.
6. **Mandatory labels backfire.**
    - *Label fatigue:* once most figures carry the note, it conveys nothing (cf. ubiquitous warning labels).
    - *False reassurance:* unlabelled figures are read as more trustworthy, though human-written plotting code is also buggy.
    - *Perverse incentive:* a visible stigma on the figure pushes authors toward non-disclosure, which is unenforceable to detect for plotting code.

## Policy anchors (verify against the primary sources before citing)

- **Nature portfolio and ICMJE recommendations:** AI tool use is to be documented in the methods (or acknowledgments) section — the mainstream standard the motion calls insufficient.
- **arXiv:** asks that use of generative AI be reported consistent with the standards of the field; no caption requirement.
- **Image-specific restrictions** (Nature, Science, Elsevier) target generative imagery, not LLM-assisted data plots. Do not let the other side stretch them to case (b).

## Expect these attacks — and answer them

| They will say | You answer |
|---|---|
| "Figures get reused without the methods section." | Reused figures also lose cuts, selection criteria, and systematics. The norm is to cite the source paper, not to pack the methods into every caption. |
| "Nobody reads the methods." | Then fix the methods statement (make it specific, per figure), not the caption. Anyone evaluating validity must read the methods anyway. |
| "We already write 'simulation' in captions." | That describes *what is plotted* (simulated vs. measured data). AI assistance describes *how the plot was drawn*. Different categories. |
| "LLMs make silent errors." | So do students and legacy scripts. The answer is validation and open code for all figures, not a label for some. |

## Questions to press

- Give an operational definition: exactly which figures need the label? Does autocomplete count?
- What can a reader *do* with the caption label that they cannot do with a specific methods statement plus released code?

---

*This brief was drafted with an LLM assistant and is deliberately one-sided. Check every policy claim against the current publisher pages before using it in the debate.*
