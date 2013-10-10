#!/usr/bin/python
'''
Title: Evil Corp
Author: Niklas & Ramkumar
'''
import unittest
import string

def censor(string_to_censor, censor_list):
    if type(censor_list) == dict:
        return replace(string_to_censor, censor_list)
    else:
        return censor2(string_to_censor, censor_list)

def censor2(string_to_censor, censor_list):
    word_list = string_to_censor.split()
    for i in range(len(word_list)):
        for censor_word in censor_list:
            if censor_word in word_list[i]:
                word_list[i] = 'x'*len(word_list[i])
    return ' '.join(word_list)

def replace(string_to_censor, replacement):
    censored_str = string_to_censor
    for i in replacement:
        if i in string_to_censor:
            censored_str = string.replace(censored_str, i, replacement[i])
    return censored_str

class TestCensorFunction(unittest.TestCase):
    """ Test all classes and functions """

    def test_with_one_word(self):
        test_string = "I love test driven development!"
        test_string_censored = "I love xxxx driven development!"
        test_string_part = ["test"]
        self.assertEqual(censor(test_string, test_string_part), test_string_censored)

    def test_with_one_other_word(self):
        test_string = "I love to eat free food!"
        test_string_censored = "I love to xxx free food!"
        test_string_part = ["eat"]
        self.assertEqual(censor(test_string, test_string_part), test_string_censored)

    def test_with_two_same_words(self):
        test_string = "I am like you know, like really angry!"
        test_string_censored = "I am xxxx you know, xxxx really angry!"
        test_string_part = ["like"]
        self.assertEqual(censor(test_string, test_string_part), test_string_censored)

    def test_with_concatenated_words(self):
        test_string = "nicenicenicenice"
        test_string_censored = "xxxxxxxxxxxxxxxx"
        test_string_part = ["nice"]
        self.assertEqual(censor(test_string, test_string_part), test_string_censored)

    def test_with_non_appearing_word(self):
        test_string = "I *love* Stockholm!"
        test_string_censored = "I *love* Stockholm!"
        test_string_part = ["test"]
        self.assertEqual(censor(test_string, test_string_part), test_string_censored)

    def test_empty_string_with_word(self):
        test_string = ""
        test_string_censored = ""
        test_string_part = ["test"]
        self.assertEqual(censor(test_string, test_string_part), test_string_censored)

    def test_with_multiple_words(self):
        test_string = "To be or not to be, that is the question!"
        test_string_censored = "To xx or not to xxx that xx the xxxxxxxxx"
        test_string_part = ["be", "is", "question"]
        self.assertEqual(censor(test_string, test_string_part), test_string_censored)

    def test_with_empty_list(self):
        test_string = "To be or not to be, that is the question!"
        test_string_censored = "To be or not to be, that is the question!"
        test_string_part = []
        self.assertEqual(censor(test_string, test_string_part), test_string_censored)

    def test_words_with_wordparts(self):
        test_string = "The quest: To be or not to be, that is the question!"
        test_string_censored = "The xxxxxx To be or not to be, that is the xxxxxxxxx"
        test_string_part = ["quest"]
        self.assertEqual(censor(test_string, test_string_part), test_string_censored)

class TestReplace(unittest.TestCase):
    def test_with_word(self):
        string = "This feels magnificient!"
        string_censored = "This feels doublegood!"
        replacement = {"magnificient":"doublegood"}
        result = censor(string, replacement)
        self.assertEqual(result, string_censored)

    def test_with_words(self):
        string = "Objection is bad, a better thing to do, is to agree."
        string_censored = "Thoughtcrime is ungood, a gooder thing to do, is to crimestop."
        replacement = {"Objection":"Thoughtcrime", "bad":"ungood", "better":"gooder", "agree":"crimestop"}
        result = censor(string, replacement)
        self.assertEqual(result, string_censored)
