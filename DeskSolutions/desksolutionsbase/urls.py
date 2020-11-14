from django.urls import path
from desksolutionsbase.views import OrganizationRegister, signup

app_name = "signup"

urlpatterns = [
    path('', OrganizationRegister, name="home"),
    path('profile/', signup, name='signups'),
]
