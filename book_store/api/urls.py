from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,    )


app_name = 'api'


urlpatterns = [

    # jwt and register
    path('register/',views.user_registration,name="register_api"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    # Review managment 
    path('reviews/', views.ReviewsListAPIView.as_view(), name='reviews'),   #GET POST
    path('reviews/<str:pk>/', views.ReviewsAPIView.as_view(), name='review_detail'),    #PUT DELETE
    #GET return all reviews of book with related reviewers names 5 part
    path('books/<str:pk>/reviews/',views.BookReviewsAPIView.as_view() , name='book_review'),


    #Book Managment 
    path('books/',views.BookListAPIView.as_view() , name='all_books'),  #books with optional filters of authoe and publish date
    path('books/<str:pk>/',views.EachBookDetail.as_view(), name='books_by_id'),


    #Author Managment
    path('authors/',views.AllAuthorsAPIView.as_view(), name='all_authors'),
    path('authors/<str:pk>/',views.EachAuthorDetail.as_view(), name='each_author'),


]