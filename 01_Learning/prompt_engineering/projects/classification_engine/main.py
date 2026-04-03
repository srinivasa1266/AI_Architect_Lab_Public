def classify_case(text: str):
    text = text.lower()
    if "delay" in text or "penalty" in text or "cancel" in text:
        return {"risk": "MEDIUM", "decision": "REVIEW", "reason": "Operational disruption detected"}
    return {"risk": "LOW", "decision": "APPROVE", "reason": "No major issue detected"}

if __name__ == "__main__":
    case = "Shipment delayed by 3 days and customer threatens cancellation."
    print(classify_case(case))
