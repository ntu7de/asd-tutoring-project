from django.test import TestCase, Client
from mainApp.models import User, Profile, Tutor, Classes, tutorClasses
# Create your tests here.


class TutorTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="password")
        self.user.profile = Profile.objects.create(user=self.user, first_name="f_name", last_name="l_name", year="1",
                                                   pronouns="pronouns", major="major", tutor_or_student="tutor",
                                                   fun_fact="fact")
        self.user.tutor = Tutor.objects.create(user=self.user, hourly_rate=10, monday_start="9:00 AM",
                                               monday_end="12:00 PM", tuesday_start="9:00 AM", tuesday_end="12:00 PM",
                                               wednesday_start="9:00 AM", wednesday_end="12:00 PM",
                                               thursday_start="9:00 AM", thursday_end="12:00 PM",
                                               friday_start="9:00 AM", friday_end="12:00 PM")
        self.client = Client()


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
        self.assertEqual(tutor.monday_start, "9:00 AM")
        self.assertEqual(tutor.monday_end, "12:00 PM")
        self.assertEqual(tutor.tuesday_start, "9:00 AM")
        self.assertEqual(tutor.tuesday_end, "12:00 PM")
        self.assertEqual(tutor.wednesday_start, "9:00 AM")
        self.assertEqual(tutor.wednesday_end, "12:00 PM")
        self.assertEqual(tutor.thursday_start, "9:00 AM")
        self.assertEqual(tutor.thursday_end, "12:00 PM")
        self.assertEqual(tutor.friday_start, "9:00 AM")
        self.assertEqual(tutor.friday_end, "12:00 PM")

    # def test_accountDisplay(self):
    #     """
    #     test to see if the accountDisplay page works correctly
    #     """
    #     response = self.client.get('/accountDisplay/', {"profile": self.user.profile})
    #     profile = response.context['profile']
    #
    #     # Check that the response is 200 OK.
    #     self.assertEqual(response.status_code, 200)
    #
    #     # Check that the rendered context contains 1 class.
    #     self.assertEqual(profile.first_name, 'f_name')
    #     self.assertEqual(profile.last_name, 'l_name')
    #     self.assertEqual(profile.year, "1")
    #     self.assertEqual(profile.pronouns, 'pronouns')
    #     self.assertEqual(profile.major, 'major')
    #     self.assertEqual(profile.tutor_or_student, "tutor")
    #     self.assertEqual(profile.fun_fact, 'fact')

# from https://docs.djangoproject.com/en/2.1/topics/testing/tools/
# class ListTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username="tester", password="password")
#         self.user.profile = Profile.objects.create(user=self.user, first_name="f_name", last_name="l_name", year="1",
#                                                    pronouns="pronouns", major="major", tutor_or_student="tutor",
#                                                    fun_fact="fact")
#
#         # self.user.tutor = Tutor.objects.create(user=self.user, hourly_rate=10, monday_start='09:00', monday_end='12:00',
#         #                                        tuesday_start='09:00', tuesday_end='12:00', wednesday_start="09:00",
#         #                                        wednesday_end="12:00", thursday_start="09:00", thursday_end="12:00",
#         #                                        friday_start="09:00", friday_end="12:00")
#         # Every test needs a client.
#         self.client = Client()
#
#         # Add a class
#         Classes.objects.create(subject="testing", catalognumber="1234", classsection="001", classnumber="12345",
#                                classname="testClass", instructor="testTeacher")
#         tutorClasses.objects.create(tutor=self.user)
#
#
#     def test_class_list(self):
#         """
#         testing if class list returns the correct amount of classes.
#         :return:
#         """
#         # Issue a GET request.
#         response = self.client.get('/classList/')
#
#         # Check that the response is 200 OK.
#         self.assertEqual(response.status_code, 200)
#
#         # Check that the rendered context contains 1 class.
#         self.assertEqual(len(response.context['info']), 1)
