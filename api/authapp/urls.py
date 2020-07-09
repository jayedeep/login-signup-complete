from django.urls import path,include
from authapp import views

urlpatterns=[
     path('',include('djoser.urls')),
     path('',include('djoser.urls.authtoken')),

    path('college/', views.CreateCollege.as_view()),
    path('college/detail/<int:pk>/', views.DetailCollege.as_view()),
    path('college/update/<int:pk>/', views.UpdateCollege.as_view()),
    path('college/delete/<int:pk>/', views.DestroyCollege.as_view()),
    # path('collegelist/', views.ListCollege.as_view()),

    path('professor/', views.CreateProfessor.as_view()),
    path('professor/detail/<int:pk>/', views.DetailProfessor.as_view()),
    path('professor/update/<int:pk>/', views.UpdateProfessor.as_view()),
    path('professor/delete/<int:pk>/', views.DestroyProfessor.as_view()),
    path('professorlist/', views.ListProfessors.as_view()),

    path('students/', views.CreateStudent.as_view()),
    path('student/detail/<int:pk>/', views.DetailStudent.as_view()),
    path('student/update/<int:pk>/',views.UpdateStudent.as_view()),
    path('student/delete/<int:pk>/', views.DestroyStudent.as_view()),
    path('studentlist/',views.ListStudents.as_view()),

]