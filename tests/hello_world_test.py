from pytest import LogCaptureFixture, raises

from kivy_playground.hello_world import get_hello_world


def test_hello_world(
    capsys: LogCaptureFixture,
) -> None:
    """Test the function get_hello_world.

    Goes through all possible scenario's of the function.
    1. No parameters are given (both parameters defaulted to False).
    2. Only print_string is True.
    3. Only raise_exception is True.
    4. Both print_string and raise_exception are given.
    """
    assert get_hello_world() == "Hello World!"
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""

    assert get_hello_world(print_string=True) == "Hello World!"
    out, err = capsys.readouterr()
    assert out == "Hello World!\n"
    assert err == ""

    with raises(Exception):
        get_hello_world(raise_exception=True)
        out, err = capsys.readouterr()
        assert out == ""
        assert err == "This is an exception.\n"
