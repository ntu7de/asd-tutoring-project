from django.test import TestCase
from mainApp.models import User
from mainApp.models import Profile
from mainApp.models import Tutor
# Create your tests here.


class TutorTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="password")
        self.user.profile = Profile.objects.create(user=self.user, first_name="f_name", last_name="l_name", year=1,
                                                   email="email", pronouns="pronouns", major="major", is_tutor=True,
                                                   is_student=False, fun_fact="fact")
        self.user.tutor = Tutor.objects.create(user=self.user, hourly_rate=10, monday_hours="10-2", tuesday_hours="5-6",
                                               wednesday_hours="10-2", thursday_hours="5-6", friday_hours="none")

    def test_tutor_profile(self):
        """
        testing if tutor profile data is correctly stored in profile
        """
        tutor = self.user.profile
        self.assertEqual(tutor.first_name, 'f_name')
        self.assertEqual(tutor.last_name, 'l_name')
        self.assertEqual(tutor.year, 1)
        self.assertEqual(tutor.email, 'email')
        self.assertEqual(tutor.pronouns, 'pronouns')
        self.assertEqual(tutor.major, 'major')
        self.assertEqual(tutor.is_tutor, True)
        self.assertEqual(tutor.is_student, False)
        self.assertEqual(tutor.fun_fact, 'fact')

    def test_tutor_hours(self):
        tutor = self.user.tutor
        self.assertEqual(tutor.hourly_rate, 10)
        self.assertEqual(tutor.monday_hours, "10-2")
        self.assertEqual(tutor.tuesday_hours, "5-6")
        self.assertEqual(tutor.wednesday_hours, "10-2")
        self.assertEqual(tutor.thursday_hours, "5-6")
        self.assertEqual(tutor.friday_hours, "none")
