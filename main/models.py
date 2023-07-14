from django.db import models
from django.core import serializers
# Teacher Model


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '1. Teachers'

    # Total teacher courses
    def total_teacher_courses(self):
        total_courses = Course.objects.filter(teacher=self).count()
        return total_courses

    # Total teacher students
    def total_teacher_students(self):
        total_students = StudentCourseEnrollment.objects.filter(
            teacher=self).count()
        return total_students


# Course Category Model


class CourseCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name_plural = '2. Course Categories'

    def __str__(self):
        return self.title

# Course Model


class Course(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    featured_img = models.ImageField(upload_to='courses_imgs/', null=True)

    class Meta:
        verbose_name_plural = '3. Courses'

    def __str__(self):
        return self.title

    def total_enrolled_students(self):
        total_enrolled_students = StudentCourseEnrollment.objects.filter(
            course=self).count()
        return total_enrolled_students

# Chapter Model


class Chapter(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='course_chapters')
    title = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    video = models.FileField(upload_to='chapter_videos/', null=True)
    video_description = models.TextField(null=True)
    pdf = models.FileField(upload_to='pdfs/', null=True)
    pdf_description = models.TextField(null=True)
    ppt = models.FileField(upload_to='ppts/', null=True)
    ppt_description = models.TextField(null=True)
    text = models.TextField(null=True)

    class Meta:
        verbose_name_plural = '4. Chapters'

    def __str__(self) -> str:
        if self.title:
            return self.title
        else:
            return 'f'

# Student Model


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=200)
    date = models.DateField(null=True)
    phone = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.first_name+self.last_name

    def enrolled_courses(self):
        enrolled_courses = StudentCourseEnrollment.objects.filter(
            student=self).count()
        return enrolled_courses

    class Meta:
        verbose_name_plural = '5. Students'


# Student Course Enrollment


class StudentCourseEnrollment(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='enrolled_courses')
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='enrolled_student')
    enrolled_time = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = '6. Enrolled Courses'

    def __str__(self):
        return f"{self.course}-{self.student}"


class Quiz(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    detail = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    def assign_status(self):
        return CourseQuiz.objects.filter(quiz=self).count()

    class Meta:
        verbose_name_plural = '7. Quiz'


class QuizQuestions(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    questions = models.CharField(max_length=200)
    ans1 = models.CharField(max_length=200)
    ans2 = models.CharField(max_length=200)
    ans3 = models.CharField(max_length=200)
    ans4 = models.CharField(max_length=200)
    right_ans = models.CharField(max_length=200)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '8. Quiz Questions'

# Add Quiz to Course


class CourseQuiz(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '9. Course Quiz'


class AttemptQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(
        QuizQuestions, on_delete=models.CASCADE, null=True)
    right_ans = models.CharField(max_length=200, null=True)
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '10. Attempted Questions'
