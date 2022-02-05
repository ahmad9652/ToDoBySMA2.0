from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.index,name='Welcome'),
    path('contact/',views.contact,name='Contact Us'),    
    path('about/',views.about,name='About us'),   
    path('task/',views.task1,name='Task List'),
    path('base/',views.base,name='base'),
    path('signup/',views.handelsignup,name='signup'),
    path('login/',views.handellogin,name='login'),
    path('logout/',views.handlelogout,name='logout'),
    path('update/<int:sno>',views.update,name="update"),
    path('delete/<int:sno>',views.deletetask,name="delete")
]