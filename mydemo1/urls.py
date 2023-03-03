from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('createorganisation', views.createorganisation, name='createorganisation'),
    # path('joinorganisation', views.joinorganisation, name='joinorganisation'),
    path('madeorganisation', views.madeorganisation, name='madeorganisation'),
    path('myorganisation', views.myorganisation, name='myorganisation'),

    path('addUserOr/<int:pk>', views.addUserOr, name='addUserOr'),
    path('allUserOr/<int:pk>', views.allUserOr, name='allUserOr'),
    path('addUploaderOr/<int:pk>', views.addUploaderOr, name='addUploaderOr'),
    path('addPhotosNo/<int:pk>', views.addPhotosNo, name='addPhotosNo'),
    path('renameOr/<int:pk>', views.renameOr, name='renameOr'), 
    path('renameNo/<int:pk>', views.renameNo, name='renameNo'), 
    path('deleteOr/<int:pk>', views.deleteOr, name='deleteOr'), 
    path('deleteNote/<int:pk>', views.deleteNote, name='deleteNote'), 
    path('viewNotesOr/<int:pk>', views.viewNotesOr, name='viewNotesOr'), 
    path('uploadNotesOr/<int:pk>', views.uploadNotesOr, name='uploadNotesOr'), 
    path('visitNote/<int:pk>', views.visitNote, name='visitNote'), 
    path('', views.index, name='index'),
]