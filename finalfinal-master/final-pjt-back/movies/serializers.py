from rest_framework import serializers
from .models import Movie, Review, ReviewComment, Ott, Cinemanow, Cinemaupcoming, Updatedate


class MovieSerializer(serializers.ModelSerializer):

    class Meta:

        model = Movie
        fields = '__all__'
        read_only_fields = ('like_movies', 'like_users',)


# 여기여기여기여기여기

class UpdatedateSerializer(serializers.ModelSerializer):
    class Meta:
      model = Updatedate
      fields = '__all__'

class OttSerializer(serializers.ModelSerializer):

    class Meta:
      model = Ott
      fields = '__all__'

class CinemanowSerializer(serializers.ModelSerializer):

    class Meta:
      model = Cinemanow
      fields = '__all__'

class CinemaupcomingSerializer(serializers.ModelSerializer):

    class Meta:
      model = Cinemaupcoming
      fields = '__all__'


# 여기여기여기여기여기





#----------------------------------------------------------------

class ReviewListSerializer(serializers.ModelSerializer):
  movie_title = serializers.SerializerMethodField()

  def get_movie_title(self, obj):
    return obj.movie.title

  userName = serializers.SerializerMethodField()
  
  def get_userName(self,obj):
    return obj.user.username

  class Meta:
    model = Review
    fields = ('id', 'user', 'title', 'content', 'movie', 'rank', 'created_at', 'updated_at', 'movie_title', 'userName')
    read_only_fields = ('user',)
    

#----------------------------------------------------------------

class ReviewReadSerializer(serializers.ModelSerializer):
  movie_title = serializers.SerializerMethodField()
  created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
  updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

  def get_movie_title(self, obj):
    return obj.movie.title

  userName = serializers.SerializerMethodField()
  
  def get_userName(self,obj):
    return obj.user.username

  class Meta:
    model = Review
    fields = ('id', 'user', 'title', 'content', 'movie', 'rank', 'created_at', 'updated_at', 'movie_title', 'userName')
    read_only_fields = ('user',)

#----------------------------------------------------------------

class ReviewCommentSerializer(serializers.ModelSerializer):
  userName = serializers.SerializerMethodField()

  def get_userName(self,obj):
    return obj.user.username

  
  class Meta:
    model = ReviewComment
    fields = '__all__'
    read_only_fields = ('user', 'review',)


#----------------------------------------------------------------

class ReviewCommentReadSerializer(serializers.ModelSerializer):
  userName = serializers.SerializerMethodField()
  created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
  updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

  def get_userName(self,obj):
    return obj.user.username

  
  class Meta:
    model = ReviewComment
    fields = '__all__'
    read_only_fields = ('user', 'review',)
