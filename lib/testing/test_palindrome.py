from palindrome import longest_palindromic_substring

def test_example_babad():
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]

def test_example_cbbd():
    assert longest_palindromic_substring("cbbd") == "bb"

def test_example_single_char():
    assert longest_palindromic_substring("a") == "a"

def test_example_two_chars():
    result = longest_palindromic_substring("ac")
    assert result in ["a", "c"]

def test_example_full_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"

def test_palindrome_at_start():
    assert longest_palindromic_substring("noonabc") == "noon"

def test_palindrome_at_end():
    assert longest_palindromic_substring("abcxyzmadam") == "madam"

def test_numbers_are_handled():
    assert longest_palindromic_substring("abc123321xyz") == "123321"

def test_even_length_palindrome():
    assert longest_palindromic_substring("abccba") == "abccba"

def test_all_unique_characters():
    result = longest_palindromic_substring("abcdefg")
    assert result in list("abcdefg")  # Each character is valid

def test_all_same_characters():
    assert longest_palindromic_substring("zzzzzz") == "zzzzzz"

def test_mixed_letters_and_digits():
    result = longest_palindromic_substring("1a2b2a1")
    assert result == "1a2b2a1"

def test_long_input_string():
    s = "ab" * 500  # length = 1000 (max constraint)
    result = longest_palindromic_substring(s)
    assert result == result[::-1]
    assert result in s