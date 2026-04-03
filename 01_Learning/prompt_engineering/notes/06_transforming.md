# Transforming

Transforming means changing text from one form into another.

Examples:
- translate tone
- rewrite for a different audience
- convert free text into structured fields
- normalize content
- reformat answers

This pattern is valuable because many systems need consistent outputs.

---

## Use cases

- convert email into ticket summary
- rewrite technical notes for business users
- transform raw incident text into JSON
- standardize inconsistent content

---

## Example prompt

Convert the following support message into JSON with fields:
issue_type, urgency, customer_sentiment, requested_action

Message:
"""
I’ve emailed twice already. My order is still delayed and I need it before Friday.
"""

Return JSON only.

---

## Why transformation matters

Transformation is often a bridge between:
- human text
- machine workflows

This makes it especially valuable in integrations.

---

## Common mistakes

- not specifying the target form
- not defining field names
- asking for too many transformations at once
- not handling missing values

---

## Good developer practice

If using transformation prompts in software:
- define schema
- validate schema
- handle nulls
- never blindly trust generated fields

---

## Interview point

Transformation prompts are useful when I need consistent, machine-friendly outputs from messy human text. They are especially valuable in workflows where unstructured inputs must be normalized before further processing.
