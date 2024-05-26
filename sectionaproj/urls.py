from django.urls import path 
from . import views

urlpatterns = [
    #gender paths
    path('genders', views.index_gender),
    path('genders/create', views.create_gender),
    path('genders/store', views.store_gender),
    path('genders/show/<int:gender_id>', views.show_gender),
    path('genders/edit/<int:gender_id>', views.edit_gender),
    path('genders/update/<int:gender_id>', views.update_gender),
    path('genders/delete/<int:gender_id>', views.delete_gender),
    path('genders/destroy/<int:gender_id>', views.destroy_gender),
    #Users path
    path('users', views.index_user),
    path('users/create', views.create_user),
    path('users/store', views.store_user)
]
