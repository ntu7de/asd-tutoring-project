from django.test import TestCase
from testScript import Questions
class QuestionModelTests(TestCase):
    def checkEquals(self):
        checkThis = 5
        self.assertEquals(checkThis.is5(), True)
