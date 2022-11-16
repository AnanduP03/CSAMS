import graphene


from django.contrib.auth import get_user_model

from user.graphql.types.user import UserType, FacultyType
from graphql_jwt.decorators import login_required
from backend.api import APIException
from user.models import Faculty

class UserQueries(graphene.ObjectType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)
    faculty = graphene.Field(FacultyType)
    
    
    @login_required
    def resolve_users(self, info):
        return get_user_model().objects.all()
    
    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Authentication Failure!')
        return user
    
    @login_required
    def resolve_faculty(self, info):
        user = info.context.user
        try:
            faculty = Faculty.objects.get(user_id = user.id)
        except Faculty.DoesNotExist:
            raise APIException("Faculty object not found")
        return faculty
        


__all__ = [
    'UserQueries'
]