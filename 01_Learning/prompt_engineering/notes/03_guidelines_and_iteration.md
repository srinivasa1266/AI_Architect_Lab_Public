# Guidelines and Iterative Prompting

This note covers the two most practical themes from the course:
1. guidelines for writing strong prompts
2. iterative improvement

---

# Part A — Prompt Guidelines

## 1. Write clear and specific instructions

Clarity is the most important baseline rule.

Bad:
Analyze this case.

Better:
You are a supply chain analyst. Review the case and determine:
1. risk level
2. recommended action
3. reason

Return the answer as JSON with fields: risk, action, reason.

Why it works:
- role is defined
- task is explicit
- output format is constrained

---

## 2. Use delimiters to separate inputs

Delimiters make prompts easier for the model to parse.

Example:
```text
Summarize the following text:

"""
Customer reports shipment delayed by 5 days and threatens cancellation.
"""
```

Use delimiters when:
- input is long
- user text could contain instructions
- you want to isolate trusted instructions from raw input

---

## 3. Ask for structured output

One of the biggest shifts from beginner prompting to developer prompting is asking for machine-readable results.

Example:
```text
Return valid JSON with:
severity, decision, reason
```

This improves:
- parsing
- consistency
- integration
- testing

---

## 4. Check whether conditions are satisfied

For complex prompts, ask the model to verify constraints.

Example:
- Did the response include all required fields?
- Did the output stay within the requested format?

This is not perfect, but it helps.

---

## 5. Give the model time to think

For harder tasks, ask for a process.

Example:
- first identify key facts
- then assess risk
- then produce final result

This often improves quality.

In production, you may still hide intermediate reasoning and only keep the final output.

---

# Part B — Iterative Prompting

A prompt usually improves through cycles.

## Typical loop
1. write first draft
2. test prompt
3. inspect errors
4. revise wording
5. test again
6. stabilize output

This is similar to debugging.

---

## What to revise during iteration

### Revise task wording
Maybe the prompt is too vague.

### Revise role
Maybe the assistant needs a better frame.

### Revise constraints
Maybe it needs clearer limits.

### Revise output format
Maybe it should return JSON or bullets.

### Add examples
Maybe few-shot prompting is needed.

---

## Common prompt iteration workflow

### Version 1
“Analyze this case.”

Problem:
too vague.

### Version 2
“Analyze the shipment delay and identify risk.”

Problem:
still unclear what output should look like.

### Version 3
“You are a supply chain operations analyst. Determine risk as LOW, MEDIUM, or HIGH. Return JSON with risk and reason.”

Improvement:
more focused.

### Version 4
Add examples and boundary conditions.

Result:
more stable.

---

## What good iteration looks like

Good iteration is not random.

You should track:
- what changed
- why it changed
- what improved
- what still fails

That is why prompt experiments are useful.

---

## Interview answer you can use

Prompt engineering is iterative because model behavior depends heavily on wording, structure, and context. In practice, I treat prompts like application logic: I test them, inspect failure modes, refine them, and stabilize them based on the task and expected output.
