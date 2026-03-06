def route_problem(parsed_data):

    topic = parsed_data["topic"]

    if topic == "calculus":
        route = "calculus_solver"

    elif topic == "probability":
        route = "probability_solver"

    else:
        route = "general_solver"

    return route