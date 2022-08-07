from django.urls import path
from .views import  EventCreateForAdmin, EventCreateForUser,LeadCreateViewForAdmin, LeadCreateViewForUser, detail_view, lead_list, events_list, lead_update_admin, lead_update_user, LeadDeleteView


app_name = "leads"

urlpatterns = [
        path('', lead_list, name='lead_list'),


        path('create/',LeadCreateViewForUser.as_view() , name='lead_create_user'),
        path('createAd/',LeadCreateViewForAdmin.as_view() , name='lead_create_admin'),
        path('<pk>/update', lead_update_user,name='lead_update_user'),
        path('<pk>/updateAd', lead_update_admin,name='lead_update_admin'),
        path('<pk>/delete/', LeadDeleteView.as_view(), name='lead_delete'),
        path('<int:pk>/', detail_view,name='lead_detail'),





        path('events/createUs', EventCreateForUser.as_view(),name='event_create_user'),
        path('events/createAd', EventCreateForAdmin.as_view(),name='event_create_admin'),


        
       
        path('events_list', events_list, name='events_list'),


       


        
]