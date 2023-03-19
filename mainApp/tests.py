from django.test import TestCase
from mainApp.models import User
from mainApp.models import Profile
from mainApp.models import Tutor
# Create your tests here.


class ProfileTestCase(TestCase):
    def test_Tutor_Profile(self):
        user = User.objects.create(username="test")
        tutor = Profile.objects.create(user=user, first_name="f_name", last_name="l_name", year=1, email="email",
                                       pronouns="pronouns", major="major", is_tutor=True, is_student=False,
                                       fun_fact="fact")
        self.assertEqual(tutor.first_name, 'f_name')
        self.assertEqual(tutor.last_name, 'l_name')
        self.assertEqual(tutor.year, 1)
        self.assertEqual(tutor.email, 'email')
        self.assertEqual(tutor.pronouns, 'pronouns')
        self.assertEqual(tutor.major, 'major')
        self.assertEqual(tutor.is_tutor, True)
        self.assertEqual(tutor.is_student, False)
        self.assertEqual(tutor.fun_fact, 'fact')
