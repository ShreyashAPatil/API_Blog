from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home,name="home"),
    path("Post/",views.Post,name="Post"),
    path("read/",views.Read,name="read"),
    # path("accounts/",include("django.contrib.auth.urls")),
    path("signup/",views.signup,name='signup'),
    path("login/",views.loginUser,name='login'),
    path("logout/",views.logoutUser,name="logout"),
    
    path("update/<int:id>",views.Update,name="update"),
    path("delete/<int:id>",views.Delete,name="delete"),

    path('api/', include('app.api.urls'))

]
urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
