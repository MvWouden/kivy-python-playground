"""A simple example of a Python file with function definitions."""


def get_hello_world(
    print_string: bool = False, raise_exception: bool = False
) -> str:
    """Return a string with the text "Hello World!".

    This is a more extensive description of the function.
    This function returns a simple string.
    This simple string is "Hello World!".

    Parameters
    ----------
    print_string : bool
        If True, the string is printed to the console.
        Otherwise, the string is not printed to the console.
    raise_exception : bool
        If True, an exception is raised.
        Otherwise, no exception is raised.

    Returns
    -------
    str
        A string with the text "Hello World!"

    Raises
    ------
    Exception
        If raise_exception is True, an exception is raised.

    Notes
    -----
    See https://numpydoc.readthedocs.io/en/latest/example.html
    for more information on NumPy style docstrings.

    Examples
    --------
    A simple usage example:

    >>> a = get_hello_world()
    >>> print(a)
    Hello World!

    Another usage example:

    >>> get_hello_world(print_string=True)
    Hello World!

    One more usage example:

    >>> get_hello_world(raise_exception=True)
    Traceback (most recent call last):
    ...
    Exception: This is an exception.
    """
    text = "Hello World!"

    if print_string:
        print(text)

    if raise_exception:
        raise Exception("This is an exception.")

    return text


if __name__ == "__main__":
    print(get_hello_world())
