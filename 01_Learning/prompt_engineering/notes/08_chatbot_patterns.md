# Chatbot Patterns

Chatbots are one of the most visible uses of prompt engineering, but good chatbot prompting is more than roleplay.

A chatbot prompt usually defines:
- assistant role
- tone
- boundaries
- desired behavior
- refusal rules
- output style

---

## Basic chatbot anatomy

### System instruction
Defines stable behavior.

### User message
Dynamic request.

### Optional examples
Can guide response quality.

### Context or memory
Adds prior conversation state or known data.

---

## Example chatbot system prompt

You are a helpful enterprise support assistant.

Rules:
- answer clearly
- do not invent policies
- if information is missing, say so
- keep answers concise unless the user asks for detail

---

## Why chatbots matter for developers

Chatbot prompting teaches:
- stateful interaction
- instruction hierarchy
- role stability
- refusal behavior
- response consistency

---

## Common chatbot mistakes

- no clear role
- no behavior boundaries
- no handling for missing information
- no output constraints
- no escalation path

---

## Practical note

A chatbot may feel “smart,” but it is still just generating outputs from prompts plus context. It should not be treated as a trusted authority without validation or workflow controls.

That is an important mindset if you move from chatbot demos into enterprise AI systems.
