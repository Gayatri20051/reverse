from reverse import reverse_string
# change `app` to your filename if different


def test_reverse_string_normal():
    assert reverse_string("hello") == "olleh"


def test_reverse_string_palindrome():
    assert reverse_string("madam") == "madam"


def test_reverse_string_empty():
    assert reverse_string("") == ""


def test_reverse_string_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"