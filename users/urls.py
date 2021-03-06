from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as loginViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register/", userViews.Registration.as_view(), name="reg"),
    path(
        "login/",
        loginViews.LoginView.as_view(template_name="users/user.html"),
        name="log",
    ),
    path(
        "exit/",
        loginViews.LogoutView.as_view(template_name="users/exit.html"),
        name="exit",
    ),
    path(
        "pass_reset/",
        loginViews.PasswordResetView.as_view(template_name="users/pass_reset.html"),
        name="pass_reset",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        loginViews.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete/",
        loginViews.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        "password_reset_done/",
        loginViews.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # убрать при деплое


