from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('createorganisation', views.createorganisation, name='createorganisation'),
    path('joinorganisation', views.joinorganisation, name='joinorganisation'),
    path('madeorganisation', views.madeorganisation, name='madeorganisation'),
    path('myorganisation', views.myorganisation, name='myorganisation'),

    path('addUserOr', views.addUserOr, name='addUserOr'),
    path('addUploaderOr', views.addUploaderOr, name='addUploaderOr'),
    path('renameOr', views.renameOr, name='renameOr'), 
    path('viewNotesOr/<int:pk>', views.viewNotesOr, name='viewNotesOr'), 
    path('uploadNotesOr/<int:pk>', views.uploadNotesOr, name='uploadNotesOr'), 
    path('visitNote/<int:pk>', views.visitNote, name='visitNote'), 
    path('', views.index, name=''),
]