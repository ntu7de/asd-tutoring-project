from django.test import TestCase, Client
from mainApp.models import User, Profile, Tutor, Classes
# Create your tests here.


class TutorTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="password")
        self.user.profile = Profile.objects.create(user=self.user, first_name="f_name", last_name="l_name", year="1",
                                                   pronouns="pronouns", major="major", fun_fact="fact")
        self.user.tutor = Tutor.objects.create(user=self.user, hourly_rate=10, monday_hours="10-2", tuesday_hours="5-6",
                                               wednesday_hours="10-2", thursday_hours="5-6", friday_hours="none")

    def test_tutor_profile(self):
        """
        testing if tutor profile data is correctly stored in profile
        """
        tutor = self.user.profile
        self.assertEqual(tutor.first_name, 'f_name')
        self.assertEqual(tutor.last_name, 'l_name')
        self.assertEqual(tutor.year, "1")
        self.assertEqual(tutor.pronouns, 'pronouns')
        self.assertEqual(tutor.major, 'major')
        self.assertEqual(tutor.tutor_or_student, "tutor")
        self.assertEqual(tutor.fun_fact, 'fact')

    def test_tutor_hours(self):
        """
        testing to see if the tutor object keeps the correct data
        """
        tutor = self.user.tutor
        self.assertEqual(tutor.hourly_rate, 10)
        self.assertEqual(tutor.monday_hours, "10-2")
        self.assertEqual(tutor.tuesday_hours, "5-6")
        self.assertEqual(tutor.wednesday_hours, "10-2")
        self.assertEqual(tutor.thursday_hours, "5-6")
        self.assertEqual(tutor.friday_hours, "none")


# from https://docs.djangoproject.com/en/2.1/topics/testing/tools/
class ListTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="password")
        self.user.profile = Profile.objects.create(user=self.user, first_name="f_name", last_name="l_name", year="1",
                                                   pronouns="pronouns", major="major", fun_fact="fact")
        self.user.tutor = Tutor.objects.create(user=self.user, hourly_rate=10, monday_hours="10-2", tuesday_hours="5-6",
                                               wednesday_hours="10-2", thursday_hours="5-6", friday_hours="none")
        # Every test needs a client.
        self.client = Client()

        # Add a class
        Classes.objects.create(user=self.user, subject="testing", catalognumber="1234", classsection="001",
                               classnumber="12345", classname="testClass")

    def test_class_list(self):
        """
        testing if class list returns the correct amount of classes.
        :return:
        """
        # Issue a GET request.
        response = self.client.get('/classList/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 1 class.
        self.assertEqual(len(response.context['info']), 1)
