# verifier_agent.py

# This function checks if the solver output looks valid
def verify_solution(question, answer):

    # Default confidence level
    confidence = "HIGH"

    # If solver failed
    if "Could not solve" in answer:
        confidence = "LOW"

    # If answer is empty
    if answer.strip() == "":
        confidence = "LOW"

    # If answer contains unsupported message
    if "support" in answer.lower():
        confidence = "MEDIUM"

    # Return verification result
    verification_result = {
        "confidence": confidence,
        "verified_answer": answer
    }

    return verification_result