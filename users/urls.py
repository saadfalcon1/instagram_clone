from django.urls import path
from .views import (CreateUserView, VerifyAPIView, LoginView, LoginRefreshView, LogOutView, ResetPasswordView,
                    GetNewVerifyCodeView, ChangeUserInformationView, ChangeUserPhotoView, ForgotPasswordView)

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('login/refresh/', LoginRefreshView.as_view()),
    path('signup/', CreateUserView.as_view()),
    path('verify/', VerifyAPIView.as_view()),
    path('new_verify_code/', GetNewVerifyCodeView.as_view()),
    path('change_user/', ChangeUserInformationView.as_view()),
    path('change_photo/', ChangeUserPhotoView.as_view()),
    path('logout/', LogOutView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('reset_password/', ResetPasswordView.as_view()),

]
