from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('add/',views.add1,name='a'),
    path('update/<int:id>',views.update,name='b'),
    path('delete/<int:id>',views.delete,name='c'),
    path('delete_all/',views.delete_all,name='d'),
    path('history/',views.history,name='e'),
    path('delete_history/',views.delete_history,name='f'),
    path('restore/<int:id>',views.restore,name='g'),
    path('restore_all/',views.restore_all,name='h'),
    path('delete_restore/<int:id>',views.delete_restore,name='i'),
    
]