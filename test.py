#Test the answer using pytest

import your_answer;

def test_your_answer():
    assert your_answer.find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
    assert your_answer.find_message("hello world!") == ""
    assert your_answer.find_message("HELLO WORLD!!!") == "HELLOWORLD"
