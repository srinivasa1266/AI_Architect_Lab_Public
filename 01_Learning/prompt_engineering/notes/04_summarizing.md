# Summarizing

Summarization is one of the highest-value prompt patterns because it turns large text into smaller, task-relevant outputs.

But good summarization is not just “shortening text.”

It is about selecting what matters for a specific use case.

---

## Why summarization matters

In real systems, summarization helps with:
- customer reviews
- tickets
- incident reports
- meeting notes
- long emails
- multi-message threads

A good summary should preserve what matters to the next step in the workflow.

---

## Types of summarization

### 1. General summarization
Short summary of the content.

### 2. Audience-specific summarization
Same text, different audience:
- executive summary
- technical summary
- customer-facing summary

### 3. Structured summarization
Return fixed sections such as:
- issue
- impact
- next action

This is often the best enterprise pattern.

---

## Example prompt

You are an operations analyst.

Summarize the following case in 3 sections:
1. Issue
2. Business Impact
3. Recommended Next Step

Return the result in bullet points.

Input:
"""
Shipment delayed by 4 days. Customer is high priority and contract includes penalties.
"""

---

## What makes a summarization prompt strong

- target audience specified
- length controlled
- structure defined
- scope narrowed

---

## Common mistakes

- asking for “summary” without format
- not saying what matters
- not defining audience
- making it too open-ended

---

## Stronger example

Bad:
Summarize this case.

Better:
Summarize this case for an operations manager. Keep it under 60 words and include only issue, risk, and recommended next action.

---

## Enterprise use

Summaries become especially valuable when they feed:
- dashboards
- handoffs
- decision review queues
- case management systems

That means prompt design should optimize for usefulness, not literary quality.

---

## Interview point

A strong summarization prompt is audience-aware and task-aware. I usually define who the summary is for, what must be included, and what format the output should follow.
