from django.test import TestCase, Client
from mainApp.models import User, Profile, Tutor, Student, Classes, tutorClasses, Request
# Create your tests here.


class TutorTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="password", id="1234")
        self.user.profile = Profile.objects.create(user=self.user, first_name="f_name", last_name="l_name", year="1",
                                                   pronouns="pronouns", major="major", tutor_or_student="tutor",
                                                   fun_fact="fact")
        self.user.tutor = Tutor.objects.create(user=self.user, hourly_rate=20, monday_start="9:00 AM",
                                               monday_end="12:00 PM", tuesday_start="9:00 AM", tuesday_end="12:00 PM",
                                               wednesday_start="9:00 AM", wednesday_end="12:00 PM",
                                               thursday_start="9:00 AM", thursday_end="12:00 PM",
                                               friday_start="9:00 AM", friday_end="12:00 PM")
        self.client = Client()

        # Add a class
        test_class = Classes.objects.create(subject="testing", catalognumber="1234", classsection="001", classnumber="12345",
                                            classname="testClass", instructor="testTeacher")
        tutorClasses.objects.create(tutor=self.user, classes=test_class)

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
        self.assertEqual(tutor.hourly_rate, 20)
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

    def test_tutor_account_display(self):
        """
        test to see if the accountDisplay page works correctly
        """
        self.client.force_login(self.user)
        response = self.client.get('/accountDisplay/')
        profile = response.context['profile']
        tutor = response.context['tutor']
        tutor_class = response.context['classes_offered']

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered profile info is correct
        self.assertEqual(profile.first_name, 'f_name')
        self.assertEqual(profile.last_name, 'l_name')
        self.assertEqual(profile.year, "1")
        self.assertEqual(profile.pronouns, 'pronouns')
        self.assertEqual(profile.major, 'major')
        self.assertEqual(profile.tutor_or_student, "tutor")
        self.assertEqual(profile.fun_fact, 'fact')

        # Check that the tutor's hours are correct
        self.assertEqual(tutor.hourly_rate, 20)
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

        # Check that the tutor's classes are correct
        self.assertEqual(tutor_class[0].classes.classname, "testClass")

    def test_tutor_client_response(self):
        """
        test multiple client response status codes to make sure they are all 200 OK,
        and make sure the correct templates are used.
        """
        self.client.force_login(self.user)  # login

        login_response = self.client.get('/login/')
        self.assertEqual(login_response.status_code, 200)
        self.assertTemplateUsed(login_response, 'mainApp/login.html')

        tutor_response = self.client.get('/tutor/')
        self.assertEqual(tutor_response.status_code, 200)
        self.assertTemplateUsed(tutor_response, 'mainApp/tutor.html')

        tutor_account_response = self.client.get('/accountDisplay/')
        self.assertEqual(tutor_account_response.status_code, 200)
        self.assertTemplateUsed(tutor_account_response, 'mainApp/accountDisplay.html')

        tutor_setting_response = self.client.get('/tutorsetting/')
        self.assertEqual(tutor_setting_response.status_code, 200)
        self.assertTemplateUsed(tutor_setting_response, 'mainApp/tutorSettings.html')

        tutor_class_search_response = self.client.get('/classes/')
        self.assertEqual(tutor_class_search_response.status_code, 200)
        self.assertTemplateUsed(tutor_class_search_response, 'mainApp/classsearch.html')

        tutor_calendar_response = self.client.get('/tutorCalendar/')
        self.assertEqual(tutor_calendar_response.status_code, 200)
        self.assertTemplateUsed(tutor_calendar_response, 'mainApp/tutorCalendar.html')


class StudentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="password", id="1234")
        self.user.profile = Profile.objects.create(user=self.user, first_name="f_name", last_name="l_name", year="1",
                                                   pronouns="pronouns", major="major", tutor_or_student="student",
                                                   fun_fact="fact")
        self.user.student = Student.objects.create(user=self.user)
        self.client = Client()

    def test_student_profile(self):
        """
        testing if student profile data is correctly stored in profile
        """
        student = self.user.profile
        self.assertEqual(student.first_name, 'f_name')
        self.assertEqual(student.last_name, 'l_name')
        self.assertEqual(student.year, "1")
        self.assertEqual(student.pronouns, 'pronouns')
        self.assertEqual(student.major, 'major')
        self.assertEqual(student.tutor_or_student, "student")
        self.assertEqual(student.fun_fact, 'fact')

    def test_student_account_display(self):
        """
        test to see if the accountDisplayStudent page works correctly
        """
        self.client.force_login(self.user)
        response = self.client.get('/accountDisplayStudent/')
        profile = response.context['profile']

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered profile info is correct
        self.assertEqual(profile.first_name, 'f_name')
        self.assertEqual(profile.last_name, 'l_name')
        self.assertEqual(profile.year, "1")
        self.assertEqual(profile.pronouns, 'pronouns')
        self.assertEqual(profile.major, 'major')
        self.assertEqual(profile.tutor_or_student, "student")
        self.assertEqual(profile.fun_fact, 'fact')

    def test_student_client_response(self):
        """
        test multiple client response status codes to make sure they are all 200 OK,
        and make sure the correct templates are used.
        """
        self.client.force_login(self.user)  # login

        login_response = self.client.get('/login/')
        self.assertEqual(login_response.status_code, 200)
        self.assertTemplateUsed(login_response, 'mainApp/login.html')

        student_response = self.client.get('/student/')
        self.assertEqual(student_response.status_code, 200)
        self.assertTemplateUsed(student_response, 'mainApp/student.html')

        student_account_response = self.client.get('/accountDisplayStudent/')
        self.assertEqual(student_account_response.status_code, 200)
        self.assertTemplateUsed(student_account_response, 'mainApp/accountDisplayStudent.html')

        student_setting_response = self.client.get('/studentsetting/')
        self.assertEqual(student_setting_response.status_code, 200)
        self.assertTemplateUsed(student_setting_response, 'mainApp/studentSettings.html')

        student_tutor_search_response = self.client.get('/classList/')
        self.assertEqual(student_tutor_search_response.status_code, 200)
        self.assertTemplateUsed(student_tutor_search_response, 'mainApp/classList.html')


class RequestTestCase(TestCase):
    def setUp(self):
        # make a student
        self.user = User.objects.create_user(username="student_tester", password="student_password", id="1234")
        self.user.profile = Profile.objects.create(user=self.user, first_name="student_f_name",
                                                   last_name="student_l_name", year="1", pronouns="pronouns",
                                                   major="major", tutor_or_student="student", fun_fact="fact")
        self.user.student = Student.objects.create(user=self.user)

        # make a tutor
        tutor_user = User.objects.create_user(username="tutor_tester", password="tutor_password", id="1235")
        tutor_user.profile = Profile.objects.create(user=tutor_user, first_name="tutor_f_name", last_name="tutor_l_name", year="1",
                                                   pronouns="pronouns", major="major", tutor_or_student="tutor",
                                                   fun_fact="fact")
        tutor_user.tutor = Tutor.objects.create(user=tutor_user, hourly_rate=20, monday_start="9:00 AM",
                                               monday_end="12:00 PM", tuesday_start="9:00 AM", tuesday_end="12:00 PM",
                                               wednesday_start="9:00 AM", wednesday_end="12:00 PM",
                                               thursday_start="9:00 AM", thursday_end="12:00 PM",
                                               friday_start="9:00 AM", friday_end="12:00 PM")

        # Add a class
        test_class = Classes.objects.create(subject="CS", catalognumber="1110", classsection="001", classnumber="15149",
                                            classname="Introduction to Programming")
        tutorClasses.objects.create(tutor=tutor_user, classes=test_class)

        self.client = Client()

    def test_request(self):
        """
        test if a student can make a request and see it
        """
        self.client.force_login(self.user)  # login
        request_response = self.client.get("/classList/15149/")
        self.assertEqual(request_response.status_code, 200)
        self.assertTemplateUsed(request_response, 'mainApp/detail.html')
        tutor_list = request_response.context['tutors']
        tutor = tutor_list[0][1]
        Request.objects.create(startTime="9:00 AM", endTime="10:00 AM", location="the lawn",
                                             tutor=tutor, student=self.user, approved="pending",
                                             date="2023-4-27", classname="Introduction to Programming")
        home_response = self.client.get('/student/')
        self.assertEqual(home_response.status_code, 200)
        tutor_request = home_response.context['requestlist'][0]

        # Check if the request shows up correctly
        self.assertEqual(tutor_request[0], "tutor_f_name")
        self.assertEqual(tutor_request[1], "tutor_l_name")
        self.assertEqual(tutor_request[2], "2023-4-27")
        self.assertEqual(tutor_request[3], "9:00 AM")
        self.assertEqual(tutor_request[4], "10:00 AM")
        self.assertEqual(tutor_request[5], "the lawn")
        self.assertEqual(tutor_request[6], "pending")
