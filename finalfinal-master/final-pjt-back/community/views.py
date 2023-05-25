from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status

from .models import Community
from .serializers import CommunityListSerializer, CommentSerializer, CommunitySerializer, CommentListSerializer



@api_view(['GET', 'POST'])
def community_list_create(request):
    if request.method == 'GET':
        communities = Community.objects.all()
        serializer = CommunityListSerializer(communities, many=True)
        print(get_user_model().username)
        return Response(serializer.data)
    else:
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def community_detail(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)

    serializer = CommunityListSerializer(community)
    return Response(serializer.data)
    

@api_view(['GET'])
def comment_list(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    comments = community.comment_set.all()
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_comment(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, community=community)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def community_update_delete(request, community_pk):
  community = get_object_or_404(Community, pk=community_pk)

  if not request.user.communities.filter(pk=community_pk).exists():
    return Response({'message': '권한이 없습니다.'})

  if request.method == 'PUT':
      serializer = CommunitySerializer(community, data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(user=request.user)
          return Response(serializer.data)
  else:
      community.delete()
      return Response({ 'id': community_pk })


@api_view(['PUT', 'DELETE'])
def comment_delete_update(request, community_pk, comment_pk):
    community = get_object_or_404(Community, pk=community_pk)
    comment = community.comment_set.get(pk=comment_pk)

    if not request.user.comments.filter(pk=comment_pk).exists():
        return Response({'message': '권한이 없습니다.'})
    
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
    else:
        comment.delete()
        return Response({ 'id': comment_pk })
  