from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from .serializers import TeacherSerializer, CategorySerializer, CourseSerializer, ChapterSerializer, StudentSerializer, StudentCourseEnrollSerializer, TeacherDashboardSerializer, StudentDashboardSerializer, QuizSerializer, QuestionSerializer, CourseQuizSerializer, AttemptQuizSerializer
from .import models


class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
  #  permission_classes = [permissions.IsAuthenticated]


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializer
   # permission_classes = [permissions.IsAuthenticated]


class TeacherDashboard(generics.RetrieveAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherDashboardSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = models.CourseCategory.objects.all()
    serializer_class = CategorySerializer

# Course


class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer


# Course Detail View
class CourseDetailView(generics.RetrieveAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer

# specific teacher course


class TeacherCourseList(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        teacher = models.Teacher.objects.get(pk=teacher_id)
        return models.Course.objects.filter(teacher=teacher)


class TeacherCourseDetail(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer

 # Chapter


class ChapterList(generics.ListCreateAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = ChapterSerializer

# Course Chapter List


class CourseChapterList(generics.ListAPIView):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        course = models.Course.objects.get(pk=course_id)
        return models.Chapter.objects.filter(course=course)

# Student Data


class StudentList(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
  #  permission_classes = [permissions.IsAuthenticated]


class StudentDashboard(generics.RetrieveAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentDashboardSerializer


@csrf_exempt
def student_login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        studentData = models.Student.objects.get(
            email=email, password=password)
    except models.Student.DoesNotExist:
        studentData = None
    if studentData:
        return JsonResponse({'bool': True, 'student_id': studentData.id})
    else:
        return JsonResponse({'bool': False})


class ChapterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Chapter.objects.all()
    serializer_class = ChapterSerializer


class StudentEnrollCourseList(generics.ListCreateAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = StudentCourseEnrollSerializer


def fetch_enroll_status(request, student_Id, course_id):
    student = models.Student.objects.filter(id=student_Id).first()
    course = models.Course.objects.filter(id=course_id).first()
    enrollStatus = models.StudentCourseEnrollment.objects.filter(
        course=course, student=student).count()
    if enrollStatus:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})


class EnrolledStudentList(generics.ListAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = StudentCourseEnrollSerializer

    def get_queryset(self):
        if 'course_id' in self.kwargs:
            course_id = self.kwargs['course_id']
            course = models.Course.objects.get(pk=course_id)
            return models.StudentCourseEnrollment.objects.filter(course=course)
        elif 'teacher_id' in self.kwargs:
            teacher_id = self.kwargs['teacher_id']
            teacher = models.Teacher.objects.get(pk=teacher_id)
            return models.StudentCourseEnrollment.objects.filter(teacher=teacher).distinct()
        elif 'student_id' in self.kwargs:
            student_id = self.kwargs['student_id']
            student = models.Student.objects.get(pk=student_id)
            return models.StudentCourseEnrollment.objects.filter(student=student).distinct()


@csrf_exempt
def teacher_login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        teacherData = models.Teacher.objects.get(
            email=email, password=password)
    except models.Teacher.DoesNotExist:
        teacherData = None
    if teacherData:
        return JsonResponse({'bool': True, 'teacher_id': teacherData.id})
    else:
        return JsonResponse({'bool': False})


class Quizlist(generics.ListCreateAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = QuizSerializer


class TeacherQuizList(generics.ListCreateAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        teacher = models.Teacher.objects.get(pk=teacher_id)
        return models.Quiz.objects.filter(teacher=teacher)


class TeacherQuizDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizQuestionList(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        quiz_id = self.kwargs['quiz_id']
        quiz = models.Quiz.objects.get(pk=quiz_id)
        if 'limit' in self.kwargs:
            return models.QuizQuestions.objects.filter(quiz=quiz).order_by('id')[:1]
        elif 'question_id' in self.kwargs:
            current_question = self.kwargs['question_id']
            return models.QuizQuestions.objects.filter(quiz=quiz, id__gt=current_question).order_by('id')[:1]
        else:
            return models.QuizQuestions.objects.filter(quiz=quiz)


class CourseQuizList(generics.ListCreateAPIView):
    queryset = models.CourseQuiz.objects.all()
    serializer_class = CourseQuizSerializer

    def get_queryset(self):
        if 'course_id' in self.kwargs:
            course_id = self.kwargs['course_id']
            course = models.Course.objects.get(pk=course_id)
            return models.CourseQuiz.objects.filter(course=course)


def fetch_quiz_assign_status(request, quiz_id, course_id):
    quiz = models.Quiz.objects.filter(id=quiz_id).first()
    course = models.Course.objects.filter(id=course_id).first()
    assignStatus = models.CourseQuiz.objects.filter(
        course=course, quiz=quiz).count()
    if assignStatus:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})


class AttemptQuizList(generics.ListCreateAPIView):
    queryset = models.AttemptQuiz.objects.all()
    serializer_class = AttemptQuizSerializer

    def get_queryset(self):
        if 'quiz_id' in self.kwargs:
            quiz_id = self.kwargs['quiz_id']
            quiz = models.Quiz.objects.get(pk=quiz_id)
            return models.AttemptQuiz.objects.raw(f'SELECT * FROM main_attemptquiz WHERE quiz_id={int(quiz_id)} GROUP BY student_id')


def fetch_quiz_attempt_status(request, quiz_id, student_id):
    quiz = models.Quiz.objects.filter(id=quiz_id).first()
    student = models.Student.objects.filter(id=student_id).first()
    attemptStatus = models.AttemptQuiz.objects.filter(
        student=student, question__quiz=quiz).count()
    if attemptStatus > 0:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})


def fetch_quiz_result(request, quiz_id, student_id):
    quiz = models.Quiz.objects.filter(id=quiz_id).first()
    student = models.Student.objects.filter(id=student_id).first()
    total_questions = models.QuizQuestions.objects.filter(quiz=quiz).count()
    total_attempted_questions = models.AttemptQuiz.objects.filter(
        quiz=quiz, student=student).values('student').count()
    attempted_questions = models.AttemptQuiz.objects.filter(
        quiz=quiz, student=student)
    total_correct_questions = 0
    for attempt in attempted_questions:
        if attempt.right_ans == attempt.question.right_ans:
            total_correct_questions += 1

    return JsonResponse({'total_questions': total_questions, 'total_attempted_questions': total_attempted_questions, 'total_correct_questions': total_correct_questions})
