# Course Map and Learning Path

This note maps the major learning areas covered in the Prompt Engineering for Developers course into a developer-friendly study path.

The official course is structured around 9 lessons and 7 code examples, and covers:
- introduction
- guidelines
- iterative prompting
- summarizing
- inferring
- transforming
- expanding
- chatbot
- conclusion

This note translates those lessons into what you should understand as a builder.

---

## 1. Introduction

### What you should learn
- what prompt engineering is
- why prompting matters
- why LLMs can feel smart but still fail
- how prompts affect model behavior

### What you should be able to explain
- prompt engineering is not magic wording
- it is structured communication with a probabilistic system
- the prompt is part of the application design

---

## 2. Guidelines

### What you should learn
- write clear and specific instructions
- give the model time to think
- use delimiters
- ask for structured outputs
- ask the model to check its own work when appropriate

### What you should be able to explain
- ambiguity causes instability
- prompts work better when tasks, constraints, and formats are explicit

---

## 3. Iterative Prompting

### What you should learn
- first prompt is rarely the final prompt
- prompting improves through testing and refinement
- you often need multiple revisions to stabilize outputs

### What you should be able to explain
- prompting is an engineering loop, not a one-shot activity

---

## 4. Summarizing

### What you should learn
- compress large text into a smaller useful form
- tailor summary to audience and use case
- control summary length and structure

### What you should be able to explain
- summarization is not just shortening
- it is selecting what matters for a task

---

## 5. Inferring

### What you should learn
- extract labels, sentiment, urgency, risk, or topic
- turn unstructured text into structured signals

### What you should be able to explain
- inferring is one of the most practical LLM patterns in enterprise systems

---

## 6. Transforming

### What you should learn
- rewrite text
- translate tone
- convert from one format to another
- normalize text for downstream systems

### What you should be able to explain
- transformation is useful when systems need consistent inputs or outputs

---

## 7. Expanding

### What you should learn
- generate content from smaller inputs
- draft emails, responses, or messaging
- control style and boundaries

### What you should be able to explain
- expansion is useful, but should be bounded carefully in enterprise settings

---

## 8. Chatbot

### What you should learn
- maintain conversation behavior with system instructions
- define assistant role, tone, and guardrails
- handle different user intents

### What you should be able to explain
- chatbots are not just about chatting
- they are stateful prompting systems

---

## 9. Real developer takeaway

The course teaches prompting as an application-building skill, not just a chat skill.

That is important.

A developer should leave this learning path able to:
- design useful prompts
- request structured outputs
- test prompt variations
- build prompt-based mini applications
- understand where prompting ends and system validation begins
