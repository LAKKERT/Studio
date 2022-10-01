from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic



# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# def Change_password(request):
#     if request.method == 'POST':
#         form = ChangePasswordForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('home')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = ChangePasswordForm(request.user)
#     return render(request, 'registration/password_change_form.html', {
#         'change_password': form
#     })
