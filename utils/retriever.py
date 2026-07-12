def retrieve_relevant_data(query, data):

    query = query.lower()

    context = {}

    for key, value in data.items():

        if key.lower() in query:
            context[key] = value

    if context:
        return context

    return data