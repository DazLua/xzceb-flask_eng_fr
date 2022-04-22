import unittest
from translator import frenchToEnglish, englishToFrench

class machinetranslation(unittest.TestCase):

    def test_englishToFrench(self):
        if self is None:
            return self
        self.assertNotEqual(englishToFrench('Hello'), 'Bonjour')    

    def test_frenchToEnglish(self):
        if self is None:
            return self
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Hello')

if __name__=='__main__':
    unittest.main()