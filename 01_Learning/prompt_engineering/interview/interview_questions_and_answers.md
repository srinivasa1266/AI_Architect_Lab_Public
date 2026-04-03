# Interview Questions and Strong Answers

## Q1. What is prompt engineering?

Prompt engineering is the practice of designing inputs that guide an LLM to produce useful, relevant, and structured outputs for a specific task. It includes task clarity, role framing, constraints, context, examples, and output formatting.

---

## Q2. Why is prompt engineering important?

Because a model’s raw capability is only part of the result. A weak prompt can produce vague, unstable, or unusable outputs. A well-designed prompt improves consistency, structure, and usefulness.

---

## Q3. What are the key principles of a good prompt?

The key principles are:
- be clear and specific
- define the role
- separate instructions from input
- ask for structured output
- use examples if needed
- add constraints
- iterate and test

---

## Q4. What is zero-shot vs few-shot prompting?

Zero-shot prompting gives the model a task without examples.
Few-shot prompting gives the model one or more examples to guide output pattern, style, or labeling.

---

## Q5. How do you reduce hallucinations?

I reduce hallucinations by:
- writing more specific prompts
- adding constraints
- asking the model to admit missing information
- using structured outputs
- validating outputs externally
- using retrieval or rules where needed

---

## Q6. Why are structured outputs important?

They allow software systems to parse, validate, store, and route model output more reliably. Structured outputs are one of the most practical techniques for integrating LLMs into real applications.

---

## Q7. What are common LLM failure modes?

Common failure modes include:
- hallucination
- overconfidence
- format drift
- context dilution
- prompt injection

---

## Q8. Is prompt engineering enough for enterprise AI systems?

No. Prompt engineering improves output quality, but enterprise systems also need validation, monitoring, logging, security controls, workflow constraints, and often human review.

---

## Q9. How does prompt engineering connect to architecture?

Prompt engineering defines model behavior, while architecture defines how outputs are validated, stored, audited, routed, and acted on. In production, prompts must be part of a larger controlled system.

---

## Q10. What did you personally learn from prompt engineering?

I learned that LLMs are powerful but not trustworthy by default. Prompting can improve output quality, but systems still need validation and governance before AI output becomes action.
