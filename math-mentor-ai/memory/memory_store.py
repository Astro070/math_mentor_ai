# memory_store.py

memory_database = []  # list to store solved problems


def store_memory(question, answer):  # store solved question

    entry = {
        "question": question,
        "answer": answer
    }

    memory_database.append(entry)  # save to memory


def search_memory(question):  # check if similar question exists

    for item in memory_database:

        if question == item["question"]:  # exact match
            return item["answer"]

    return None  # no match found