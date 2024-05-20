# jwt and register
    path('register/',views.user_registration,name="register_api"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

above are the auth apis
first one registers a user takes email,username,password,password2,first_name,last_name if all is fine it returns created user data with http code 200
second one takes email and password in form data and returns jwt refresh and access token
third one takes refresh token value and refreshes the token



# Review managment 
    path('reviews/', views.ReviewsListAPIView.as_view(), name='reviews'),   #GET POST
    path('reviews/<str:pk>/', views.ReviewsAPIView.as_view(), name='review_detail'),    #PUT DELETE
    #GET return all reviews of book with related reviewers names 5 part
    path('books/<str:pk>/reviews/',views.BookReviewsAPIView.as_view() , name='book_review'),
aobve api are of reviews managment
first one takes GET AND POST request if accessed by get it will return all reviews if accessed by post it will add a new review_detail
second on updates and deletes reviews according to the request method
last past returns reviews of ech book along with user details who made those reviews



#Book Managment 
    path('books/',views.BookListAPIView.as_view() , name='all_books'),  #books with optional filters of authoe and publish date
    path('books/<str:pk>/',views.EachBookDetail.as_view(), name='books_by_id'),
the first of above api returns all books and also filters books according to the query parameters passed to it
second one jus shows each book detail with all the relateddata

#Author Managment
    path('authors/',views.AllAuthorsAPIView.as_view(), name='all_authors'),
    path('authors/<str:pk>/',views.EachAuthorDetail.as_view(), name='each_author'),