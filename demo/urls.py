from django.conf.urls import url
from demo import views

urlpatterns = [
    url(r'^utilisateurs/ajouter/$', views.ProfilutilisateurViewAdd.as_view()),
    url(r'^utilisateurs/liste/$', views.ProfilutilisateurViewList.as_view()),
    url(r'^utilisateurs/profil/$', views.ProfilView.as_view()),
    #url(r'^utilisateurs/(?P<is_active>[a-zA-Z])/liste/$', views.ProfilutilisateurViewList.as_view()),
    #---
    url(r'^messages/ajouter/$', views.MessagesViewAdd.as_view()),
    url(r'^messages/liste/$', views.MessagesViewList.as_view()),
    #--
    url(r'^connexions/ajouter/$', views.ConnexionViewAdd.as_view()),
    url(r'^connexions/liste/$', views.ConnexionViewList.as_view()),
    #--
    url(r'^citations/ajouter/$', views.CitationViewAdd.as_view()),
    url(r'^citations/liste/$', views.CitationViewList.as_view()),
    #--
    url(r'^role_utilisateurs/ajouter/$', views.RoleUtilisateurViewAdd.as_view()),
    url(r'^role_utilisateurs/liste/$', views.RoleUtilisateurViewList.as_view()),
    #--
    url(r'^commentaire/ajouter/$', views.CommentairesViewAdd.as_view()),
    url(r'^commentaire/liste/$', views.CommentairesViewList.as_view()),
]