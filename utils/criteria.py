def create_criteria(searching: str) -> dict[str, str]:
    """
    Create a criteria dictionary based on the given searching string.

    Args:
        searching (str): A string containing comma-separated key-value pairs.

    Returns:
        dict[str, str]: A dictionary containing the key-value pairs extracted from the searching string.
    """
    options: dict = {}
    terms = searching.split(",")
    for term in terms:
        column, value = term.split("=")

        options[column.lower()] = value
    return options
