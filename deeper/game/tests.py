from django.test import TestCase

# Create your tests here.
class UnitTest(TestCase):

    def test_pass(self):

        pass

    def test_fail(self):

        fail = True
        self.assertEqual(1, 2)