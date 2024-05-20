from rest_framework.response import Response
from rest_framework import serializers
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from .models import Review,Book,Author,User
from .serializers import ReviewsSerializerForPOST,AuthorSerializer,EachBookSerializer,ReviewsSerializer,BookSerializer,UserRegistrationSerializer,ReviewupdateSerializer,BookRatingSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.views import APIView

# Create your views here.

@api_view(['POST',])
def user_registration(request):
    if request.method == 'POST':
        data = {}
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'password must match'})
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'successffully created user'
            data['email'] = user.email
            data['username'] = user.username
            return Response(status=status.HTTP_200_OK,data=data)
        else:
            data = serializer.errors
            return Response(status=status.HTTP_401_UNAUTHORIZED,data=data)
        

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author','publish_date']


class ReviewsListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['book', 'user']
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data={}
        serializer = ReviewsSerializerForPOST(data=request.data)
        if serializer.is_valid():
            review = serializer.save(user=request.user.id)
            data['response'] = 'successffully added review'
            data['review'] = review.comment
            data['rating'] = review.rating
            data['book'] = review.book.title
            return Response(status=status.HTTP_201_CREATED,data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        if request.user != review.user:
            return Response({'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = ReviewupdateSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        data={}
        if request.user != review.user:
            return Response({'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        review.delete()
        data["response"]="deleted review"
        return Response(status=status.HTTP_200_OK,data=data)



class BookReviewsAPIView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookRatingSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EachBookDetail(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = EachBookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        


class AllAuthorsAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class EachAuthorDetail(APIView):
    def get(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
            serializer = AuthorSerializer(author)
            return Response(serializer.data)
        except Author.DoesNotExist:
            return Response({'error': 'Author does not exist'}, status=status.HTTP_404_NOT_FOUND)