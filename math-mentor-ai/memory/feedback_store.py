# feedback_store.py

feedback_database = []  # list to store feedback


def store_feedback(question, answer, feedback, comment):
    entry = {
        "question": question,
        "answer": answer,
        "feedback": feedback,
        "comment": comment
    }

    feedback_database.append(entry)  # store feedback