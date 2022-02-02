import graphene
from graphene_django import DjangoObjectType

from announcements.models import Announcement
from events.models import Event, EventType

class AnnouncementNodeType(DjangoObjectType):
    class Meta:
        model = Announcement
        fields = "__all__"

class EventTypeNodeType(DjangoObjectType):
    class Meta:
        model = EventType
        fields = "__all__"

class EventNodeType(DjangoObjectType):
    class Meta:
        model = Event
        fields = "__all__"

class Query(graphene.ObjectType):
    announcements = graphene.List(AnnouncementNodeType)
    events = graphene.List(EventNodeType)

    def resolve_announcements(root, info):
        return Announcement.objects.all()

    def resolve_events(root, info):
        return Event.objects.all()

schema = graphene.Schema(query=Query)