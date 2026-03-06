# explainer_agent.py

def generate_explanation(question, answer):

    explanation_steps = []  # list to store explanation steps

    # check if derivative problem
    if "derivative" in question.lower():
        explanation_steps.append("Step 1: Identify the function in the question")  # identify function
        explanation_steps.append("Step 2: Apply derivative rule d/dx (x^n) = n*x^(n-1)")  # derivative rule
        explanation_steps.append("Step 3: Differentiate each term separately")  # differentiate terms
        explanation_steps.append("Step 4: Combine the results to get the final answer")  # combine results

    # check if integration problem
    elif "integrate" in question.lower():
        explanation_steps.append("Step 1: Identify the expression to integrate")  # identify expression
        explanation_steps.append("Step 2: Apply integration rule ∫x^n dx = x^(n+1)/(n+1)")  # integration rule
        explanation_steps.append("Step 3: Compute the integral")  # perform integration
        explanation_steps.append("Step 4: Add constant of integration if needed")  # constant

    else:
        explanation_steps.append("Step 1: Understand the mathematical problem")  # generic step
        explanation_steps.append("Step 2: Apply appropriate math rules")  # apply rule
        explanation_steps.append("Step 3: Simplify to obtain final result")  # simplification

    explanation_steps.append(f"Final Answer: {answer}")  # append final answer

    return explanation_steps  # return explanation list