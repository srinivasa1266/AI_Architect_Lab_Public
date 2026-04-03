# Prompt Engineering for Developers — Learning Notes

This section captures my structured learning from completing the Prompt Engineering for Developers course.

The goal is to understand how Large Language Models (LLMs) behave and how to design effective prompts for real-world applications.

---

## 🧠 What is Prompt Engineering?

Prompt engineering is the process of designing inputs (prompts) to guide LLMs toward producing desired outputs.

LLMs do not "think" or "reason" like humans. They generate responses based on patterns learned from data.

---

## ⚙️ How LLMs Work

- LLMs are probabilistic models
- They predict the next token (word) based on context
- They do not verify correctness
- They can produce confident but incorrect answers

### Key Insight

> LLM output is not a decision — it is a suggestion that must be validated before execution.

---

## 🧩 Core Prompting Principles

### 1. Be Clear and Specific

The more explicit the instruction, the better the output.

**Example:**
