from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add-donor/', views.add_donor, name='add_donor'),
    path('request-blood/', views.request_blood, name='request_blood'),
    #path('edit-donor/<int:donor_id>/', views.edit_donor, name='edit_donor'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('donor/<int:id>/', views.donor_detail, name='donor_detail'),
    


]
