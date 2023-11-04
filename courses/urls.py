from django.urls import path
from .views import *


app_name = 'courses'

urlpatterns = [
    path("", CourseListView.as_view(),name='courses'),
    path("category/<str:cat>",CourseListView.as_view(),name="course_cat"),
    path("teacher/<str:teacher>",CourseListView.as_view(),name="course_teacher"),
    path("search/",CourseListView.as_view(),name="course_search"),
    path("course-detail/<int:pk>",CourseDetailView.as_view(),name="course_detail"),
    path("<int:pk>",DeleteCommentView.as_view(),name="delete"),
    path("edit/comment/<int:pk>",CommentEditView.as_view(),name="edit"),
    path("comment/reply/<int:pk>",ReplyView.as_view(),name="reply"),
    # path("payment",PaymentView.as_view(),name="cart"),
    path("payment",Cart,name="cart"),
]