def ask_query(query_engine, user_query: str):
    response = query_engine.query(user_query)
    return str(response)
