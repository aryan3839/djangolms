from django.urls import path
from .import views

urlpatterns = [
    # Teacher
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('teacher-login', views.teacher_login),
    path('teacher/dashboard/<int:pk>', views.TeacherDashboard.as_view()),



    # Category
    path('category/', views.CategoryList.as_view()),

    # Course
    path('course/', views.CourseList.as_view()),

    # Course Detail
    path('course/<int:pk>/', views.CourseDetailView.as_view()),

    # Chapter
    path('chapter/', views.ChapterList.as_view()),

    # Specific course chapter
    path('course-chapters/<int:course_id>', views.CourseChapterList.as_view()),

    # Specific Chapter
    path('chapter/<int:pk>', views.ChapterDetailView.as_view()),

    # Teacher Courses
    path('teacher-courses/<int:teacher_id>',
         views.TeacherCourseList.as_view()),

    # Student
    path('student/', views.StudentList.as_view()),
    path('student-login', views.student_login),
    path('student/dashboard/<int:pk>', views.StudentDashboard.as_view()),

    # Course Detail
    path('teacher-course-detail/<int:pk>',
         views.TeacherCourseDetail.as_view()),

    path('student-enroll-course/', views.StudentEnrollCourseList.as_view()),

    path('fetch-enroll-status/<int:student_Id>/<int:course_id>',
         views.fetch_enroll_status),


    path('fetch-enrolled-students/<int:course_id>',
         views.EnrolledStudentList.as_view()),

    path('fetch-all-enrolled-students/<int:teacher_id>',
         views.EnrolledStudentList.as_view()),

    path('fetch-enrolled-courses/<int:student_id>',
         views.EnrolledStudentList.as_view()),

    path('quiz/', views.Quizlist.as_view()),
    path('teacher-quiz/<int:teacher_id>', views.TeacherQuizList.as_view()),
    path('teacher-quiz-detail/<int:pk>', views.TeacherQuizDetail.as_view()),
    path('quiz-questions/<int:quiz_id>', views.QuizQuestionList.as_view()),
    path('quiz-questions/<int:quiz_id>/<int:limit>',
         views.QuizQuestionList.as_view()),
    path('quiz-assign-course/', views.CourseQuizList.as_view()),
    path('fetch-assigned-quiz/<int:course_id>', views.CourseQuizList.as_view()),
    path('attempt-quiz/', views.AttemptQuizList.as_view()),
    path('quiz-questions/<int:quiz_id>/next-question/<int:question_id>',
         views.QuizQuestionList.as_view()),
    path('fetch-quiz-attempt-status/<int:quiz_id>/<int:student_id>',
         views.fetch_quiz_attempt_status),
    path('fetch-quiz-assign-status/<int:quiz_id>/<int:course_id>',
         views.fetch_quiz_assign_status),
    path('attempted-quiz/<int:quiz_id>', views.AttemptQuizList.as_view()),
    path('fetch-quiz-result/<int:quiz_id>/<int:student_id>',
         views.fetch_quiz_result),
]
