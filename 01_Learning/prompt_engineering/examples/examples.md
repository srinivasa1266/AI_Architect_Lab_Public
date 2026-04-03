# Reusable Prompt Examples

## 1. Summarization

You are an operations analyst.

Summarize the following case in 3 bullets:
- issue
- business impact
- recommended next step

Input:
"""
Shipment delayed by 4 days. Customer is high priority and contract includes penalties.
"""

---

## 2. Classification

You are a support triage assistant.

Classify this ticket as LOW, MEDIUM, or HIGH urgency.

Return JSON with:
urgency, reason

Ticket:
"""
Customer reports repeated delays and threatens cancellation.
"""

---

## 3. Extraction

Extract the following fields from the text:
shipment_id, delay_days, customer_priority, financial_impact

If a field is missing, set it to null.
Return JSON only.

---

## 4. Transformation

Convert the following free text into JSON with:
issue_type, severity, next_action

---

## 5. Critique / Governance Review

You are a governance reviewer.

Review the following AI-generated recommendation.
Check whether:
1. it matches the facts
2. the risk appears understated
3. human review is needed

Return JSON with:
validity, review_required, reason
