import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(''), '') # Test for null input for englishToFrench.
        self.assertEqual(english_to_french(), '') # Test for null input for englishToFrench.
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # Test for the translation of the world 'Hello' and 'Bonjour'.
        
        

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(''), '') # Test for null input for englishToFrench.
        self.assertEqual(french_to_english(), '') # Test for null input for englishToFrench.
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # Test for the translation of the world 'Bonjour' and 'Hello'.
        
unittest.main()
