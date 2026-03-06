import re

# words that should NOT be treated as variables
STOP_WORDS = {
    "derivative", "integrate", "integral", "probability",
    "calculate", "solve", "find", "of", "the", "with"
}

def parse_question(question):

    q = question.lower()

    topic = "unknown"

    if "derivative" in q or "integrate" in q or "integral" in q:
        topic = "calculus"

    elif "probability" in q:
        topic = "probability"

    # extract words (tokens)
    tokens = re.findall(r"\b[a-zA-Z]+\b", q)

    # keep only single-letter variables like x,y,z
    variables = [t for t in tokens if len(t) == 1 and t not in STOP_WORDS]

    variables = list(set(variables))  # remove duplicates

    parsed_data = {
        "problem_text": question,
        "topic": topic,
        "variables": variables,
        "needs_clarification": False
    }

    return parsed_data