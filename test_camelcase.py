import camelCase
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', camelCase.camel_case('Hello World'))

    def test_camelcase_longer_sentence(self):
        self.assertEqual('thisIsANewTest', camelCase.camel_case('This Is A New Test'))

    def test_camelcase_with_numbers(self):
        self.assertEqual('happy2SeeYou', camelCase.camel_case('Happy 2 See You'))

    def test_camelcase_with_one_word(self):
        self.assertEqual('hello', camelCase.camel_case('Hello'))

    def test_camelCase_with_spaces(self):
        self.assertEqual('sentenceWithSpaces', camelCase.camel_case('    Sentence    With     Spaces     '))