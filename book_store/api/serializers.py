from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User,Book,Author,Review



class UserRegistrationSerializer(ModelSerializer):
    password2 = serializers.CharField(style={"input_type":"password"},write_only=True)
    class Meta:
        model = User
        fields = ['email','first_name','last_name','username','password','password2']
        extra_kwargs = {
            'password' : {'write_only' : True} }
    def save (self,**kwargs):
        user = User(
                email = self.validated_data['email'],
                first_name = self.validated_data['first_name'],
                last_name = self.validated_data['last_name'],
                username = self.validated_data['username'],
                )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2 :
            raise serializers.ValidationError({'password':'password must match'})
        user.set_password(password)
        user.save()
        return user
    
class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
class BookSerializerForReview(ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

class ReviewsSerializer(ModelSerializer):
    user = UserSerializer()
    book = BookSerializerForReview()
    class Meta:
        model = Review
        fields = ['user','book','rating','comment','created_at']
    def save (self,**kwargs):
        review = Review(
                user= User(id=str(kwargs['user'])),
                book = self.validated_data['book'],
                rating = self.validated_data['rating'],
                comment = self.validated_data['comment']
                )
        review.save()
        return review
    
class ReviewsSerializerForPOST(ModelSerializer):
    # user = UserSerializer()
    # book = BookSerializerForReview()
    class Meta:
        model = Review
        fields = ['user','book','rating','comment','created_at']
    def save (self,**kwargs):
        review = Review(
                user= User(id=str(kwargs['user'])),
                book = self.validated_data['book'],
                rating = self.validated_data['rating'],
                comment = self.validated_data['comment']
                )
        review.save()
        return review
    

class ReviewupdateSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['comment','rating']


class ReviewsSerializerForBook(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Review
        fields = ['user','rating','comment','created_at']
class BookRatingSerializer(ModelSerializer):
    book_reviews = ReviewsSerializerForBook(many=True)
    class Meta:
        model = Book
        fields = ['title','book_reviews']

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['name','bio']

class EachBookSerializer(ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = ['title','author','publish_date','isbn',]     