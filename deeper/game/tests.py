from django.test import TestCase


class UnitTest(TestCase):

    def test_pass(self):

        pass

    def test_fail(self):

        fail = True
        self.assertEqual(1, 2)
