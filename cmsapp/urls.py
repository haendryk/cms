from django.urls import path, include
from rest_framework import routers
from cmsapp import views

routers = routers.DefaultRouter()
#routers.register(r'institucional', views.InstitucionalListSet,'institucional')
# routers.register(r'publication', views.PublicationViewSet,'publication')
# routers.register(r'identity', views.IdentityViewSet,'identity')
# routers.register(r'socialnetwork', views.SocialNetworkViewSet,'socialnetwork')
# routers.register(r'history', views.HistoryViewSet,'history')
# routers.register(r'attention', views.AttentionViewSet,'attention')
# routers.register(r'faq', views.FAQViewSet,'faq')
# routers.register(r'contact', views.ContactViewSet,'contact')
# routers.register(r'team', views.TeamViewSet,'team')
# routers.register(r'service', views.ServiceViewSet,'service')

urlpatterns = [
    path('', include(routers.urls)),
    path('institucional/list/all/', views.InstitucionalListSet.as_view()),
    path('institucional/list/valid/', views.institucional_value),
    path('publication/list/all/', views.PublicationListSet.as_view()),
    path('publication/list/valid/', views.publication_value),
    path('identity/list/all/', views.IdentityListSet.as_view()),
    path('identity/list/valid/', views.identity_value),
    path('socialnetwork/list/all/', views.SocialNetworkListSet.as_view()),
    path('socialnetwork/list/valid/', views.socialnetwork_value),
    path('history/list/all/', views.HistoryListSet.as_view()),
    path('history/list/valid/', views.history_value),
    path('attention/list/all/', views.AttentionListSet.as_view()),
    path('attention/list/valid/', views.attention_value),
    path('contact/', views.ContactCreateListSet.as_view()),
    path('team/list/all/',views.TeamListSet.as_view()),
    path('faq/list/all/', views.FAQListSet.as_view()),
    path('faq/list/valid/', views.faq_value),
    path('service/list/all/', views.ServiceListSet.as_view()),
    path('service/list/valid/', views.service_value),
]