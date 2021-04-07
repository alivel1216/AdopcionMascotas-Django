"""Users URLs."""

# Django
from django.urls import path
from django.views.generic import TemplateView

# View
from users import views

urlpatterns = [

    # Management
    path(
        route='login/',
        view=views.login_views,
        name='login'
    ),
    path(
        route='logout/',
        view=views.logout_views,
        name='logout'
    ),
    path(
        route='signup/',
        view=views.signup,
        name='signup'
    ),
    path(
        route='me/profile/',
        view=views.update_profile,
        name='update'
    ),

    # Posts
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    )

]