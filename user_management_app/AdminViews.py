from django.shortcuts import render,redirect ,get_object_or_404
from . AdminForms import AdminUserEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# Admin User Edit
@login_required(login_url='/error_404/')
def user_edit(request, user_id):

    if not request.user.is_superuser:
        return redirect('error_404')
    
    selected_user = User.objects.get(id = user_id)
    if request.method == 'POST':
        user_edit_form = AdminUserEditForm(request.POST, instance=selected_user)
        if user_edit_form.is_valid():
            user_edit_form.save()
            user_edit_form.send_email()
            return redirect('all_users')
        else:
            return redirect('error_404')
    else:
        user_edit_form = AdminUserEditForm(instance=selected_user)


    context = {
        'user_edit_form' : user_edit_form,
        'selected_user'  : selected_user,
    }
    return render(request, 'Admins/User_Edit.html', context)