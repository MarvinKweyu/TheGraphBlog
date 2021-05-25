from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from blog import models

#  each class below should have a name that ends with `Type`
#  because each reps a GraphQL type

class UserType(DjangoObjectType):
    class Meta:
        model = settings.AUTH_USER_MODEL

class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Profile

class PostType(DjangoObjectType):
    class Meta:
        model = models.Post

class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag

#  bring together all classes above
#  add methods to it and indicate how models can 
# be queried