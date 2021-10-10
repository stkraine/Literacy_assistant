import pytest
import Back_end.find_errors as error

def test_find_error_wrong_word():
    string1 = "This is the first test string"
    string2 = "This is the second test string"

    result = error.find_errors(string1, string2)
    
    assert result == ["first"]

def test_find_error_multiple_wrong_words():
    string1 = "The car drove on the highway in the rain"
    string2 = "The bus drove on the highway in the hail"

    result = error.find_errors(string1, string2)
    
    assert result == ["car", "rain"]

def test_find_error_switched_word():
    string1 = "A bunny ate a carrot"
    string2 = "A bunny a ate carrot"

    result = error.find_errors(string1,string2)
    
    assert result == ["a"]

def test_find_error_add_word():
    string1 = "The kids were sledding down the hill"
    string2 = "The kids were sledding up down the hill"

    result = error.find_errors(string1,string2)
    
    assert result == []

def test_find_error_add_two_words():
    string1 = "The teacher was reading Harry Potter to the students"
    string2 = "The high school teacher was reading Harry Potter to the students"

    result = error.find_errors(string1,string2)
    
    assert result == []

def test_find_error_missing_word():
    string1 = "I do not know why there is all of this commotion"
    string2 = "I do not know why there is all this commotion"

    result = error.find_errors(string1,string2)
    
    assert result == ["of"]

def test_find_error_two_missing_words():
    string1 = "Rowing is a very physically demanding sport"
    string2 = "Rowing is a demanding sport"

    result = error.find_errors(string1,string2)
    
    assert result == ["very", "physically"]