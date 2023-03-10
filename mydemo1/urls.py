from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('user/welcome', views.welcome, name='welcome'),
    path('user/createorganisation', views.createorganisation, name='createorganisation'),
    path('user/madeorganisation', views.madeorganisation, name='madeorganisation'),
    path('user/myorganisation', views.myorganisation, name='myorganisation'),
    path('user/organisation/renameOr/<int:pk>', views.renameOr, name='renameOr'),
    path('user/organisation/deleteOr/<int:pk>', views.deleteOr, name='deleteOr'), 
    path('user/organisation/viewNotesOr/<int:pk>', views.viewNotesOr, name='viewNotesOr'), 
    path('user/organisation/leaveOrg/<int:pk>', views.leaveOrg, name='leaveOrg'), 
    
     
    path('howtouse', views.howtouse, name='howtouse'),
    path('aboutUs', views.aboutUs, name='aboutUs'),

    path('user/organisation/addUserOr/<int:pk>', views.addUserOr, name='addUserOr'),
    path('user/organisation/allUserOr/<int:pk>', views.allUserOr, name='allUserOr'),
    path('user/organisation/removeUserOr/<int:pk1>/<int:pk2>', views.removeUserOr, name='removeUserOr'),
    
    path('user/organisation/note/addUploaderOr/<int:pk>', views.addUploaderOr, name='addUploaderOr'),
    path('user/organisation/note/viewUploaders/<int:pk>', views.viewUploaders, name='viewUploaders'),
    path('user/organisation/note/addPhotosNo/<int:pk>', views.addPhotosNo, name='addPhotosNo'),
    path('user/organisation/note/renameNo/<int:pk>', views.renameNo, name='renameNo'), 
    path('user/organisation/note/deleteNote/<int:pk>', views.deleteNote, name='deleteNote'), 
    path('user/organisation/note/uploadNotesOr/<int:pk>', views.uploadNotesOr, name='uploadNotesOr'), 
    path('user/organisation/note/visitNote/<int:pk>', views.visitNote, name='visitNote'), 
    path('user/organisation/note/visitNote/deletePhoto/<int:pk>', views.deletePhoto, name='deletePhoto'), 
    path('', views.index, name='index'),
]