#from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from .serializers import InstitucionalSerializer, PublicationSerializer, IdentitySerializer, SocialNetworkSerializer, HistorySerializer, AttentionSerializer, FAQSerializer, ContactSerializer, TeamSerializer, ServiceSerializer
from .models import Institucional, Publication, Identity, SocialNetwork, History, Attention, FAQ, Contact, Team, Service

# class InstitucionalViewSet(viewsets.ModelViewSet):
#     serializer_class = InstitucionalSerializer
#     queryset = Institucional.objects.all()

class InstitucionalListSet(generics.ListAPIView):
    serializer_class = InstitucionalSerializer
    queryset = Institucional.objects.all()

@api_view(['GET'])
def institucional_value(request):
    try:
        institucional = Institucional.objects.difference(soft_delete=True)
        return HttpResponse({institucional},safe=False,status=200)
    except Exception as e:
        return HttpResponse(
            {
                "error": str(e)
            },
            safe=True,
            status=404
        )

class PublicationListSet(generics.ListAPIView):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()

@api_view(['GET'])
def publication_value(request):
    try:
        publication = Publication.objects.difference(soft_delete=True)
        return HttpResponse({publication},safe=False,status=200)
    except Exception as e:
        return HttpResponse(
            {
                "error": str(e)
            },
            safe=True,
            status=404
        )

class IdentityListSet(generics.ListAPIView):
    serializer_class = IdentitySerializer
    queryset = Identity.objects.all()

@api_view(['GET'])
def identity_value(request):
    try:
        identity = Identity.objects.difference(soft_delete=True)
        return HttpResponse({identity},safe=False,status=200)
    except Exception as e:
        return HttpResponse(
            {
                "error": str(e)
            },
            safe=True,
            status=404
        )

class SocialNetworkListSet(generics.ListAPIView):
    serializer_class = SocialNetworkSerializer
    queryset = SocialNetwork.objects.all()

@api_view(['GET'])
def socialnetwork_value(request):
    try:
        socialnetwork = SocialNetwork.objects.difference(soft_delete=True)
        return HttpResponse({socialnetwork},safe=False,status=200)
    except Exception as e:
        return HttpResponse(
            {
                "error": str(e)
            },
            safe=True,
            status=404
        )

class HistoryListSet(generics.ListAPIView):
    serializer_class = HistorySerializer
    queryset = History.objects.all()

def history_value(request):
    try:
        history = History.objects.difference(soft_delete=True)
        return HttpResponse({history},safe=False,status=200)
    except Exception as e:
        return HttpResponse(
            {
                "error": str(e)
            },
            safe=True,
            status=404
        )

class AttentionListSet(generics.ListAPIView):
    serializer_class = AttentionSerializer
    queryset = Attention.objects.all()

@api_view(['GET'])
def attention_value(request):
    try:
        attention = Attention.objects.difference(soft_delete=True)
        return HttpResponse({attention},safe=False,status=200)
    except Exception as e:
        return HttpResponse(
            {
                "error": str(e)
            },
            safe=True,
            status=404
        )

class FAQListSet(generics.ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()

def faq_value(request):
    try:
        faq = FAQ.objects.difference(soft_delete=True)
        return HttpResponse({faq},safe=False,status=200)
    except Exception as e:
        return HttpResponse(
            {
                "error": str(e)
            },
            safe=True,
            status=404
        )

class ContactCreateListSet(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

class TeamListSet(generics.ListAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

def team_value(request):
    try:
        team = Team.objects.difference(soft_delete=True)
        return HttpResponse({team},safe=False,status=200)
    except Exception as e:
        return HttpResponse(
            {
                "error": str(e)
            },
            safe=True,
            status=404
        )

class ServiceListSet(generics.ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

def service_value(request):
    try:
        service = Service.objects.difference(soft_delete=True)
        return HttpResponse({service},safe=False,status=200)
    except Exception as e:
        return HttpResponse(
            {
                "error": str(e)
            },
            safe=True,
            status=404
        )



