from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from users import views as user_views
from users.views import *
from django.conf.urls import url



urlpatterns = [
    path('', include('pages.urls')),
    #path('accounts/', include('accounts.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('churches/', include('churches.urls')),
    path('classes/', include('classes.urls')),
    path('exam_room/', include('exam_room.urls')),
    path('exercises/', include('exercises.urls'), name="excercises-urls"),
    path('notice_board/', include('notice_board.urls')),
    path('blog/', include('blog.urls')),
    path('realtors/', include('realtors.urls')),  
    path('companys/', include ('companys.urls')),  
    path('contact/', include('contact.urls')),
    path('listings/', include('listings.urls')),
    path('lessons/', include('lessons.urls')),
    path('users/', include('users.urls')),
    path('towns/', include('towns.urls')),
    path('locations/', include('locations.urls')),
    path('students/', include('students.urls')),
    path('subjects/', include('subjects.urls')),
    path('teachers/', include('teachers.urls')),
    path('videos/', include('videos.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
  
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
        ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    

