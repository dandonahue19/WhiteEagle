import graphene
from graphene_django import DjangoObjectType

from announcements.models import Announcement

class AnnouncementType(DjangoObjectType):
    class Meta:
        model = Announcement
        fields = ("id", "name", "description")

class Query(graphene.ObjectType):
    announcements = graphene.List(AnnouncementType)

    def resolve_announcements(root, info):
        return Announcement.objects.all()

schema = graphene.Schema(query=Query)