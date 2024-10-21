from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_management_app.models import Profile
from courses_app.models import Language
from django.db.models import Q

# Create your views here.

# ------------------------- Admin Dashboard Starts -------------------------

# --- Users Section Starts ---

# Function to view type of Users
@login_required(login_url='/error_404/')
def all_users(request):
    if not request.user.is_superuser:
        return redirect('base')
    users_profile = Profile.objects.all()
    all_user_profiles = users_profile.count()
    search_query = request.GET.get('search_user')

    if search_query:
        search_query = Profile.objects.filter(
            Q(user__username__icontains         = search_query) | 
            Q(user__first_name__icontains       = search_query) | 
            Q(user__email__icontains            = search_query)
        )


    active_users = Profile.objects.filter(user__is_active = True).count()
    non_active_users = Profile.objects.filter(user__is_active = False).count()

    context = {
        'search_query'          : search_query,
        'users_profile'         : users_profile,
        'all_user_profiles'     : all_user_profiles,
        'active_users'          : active_users,
        'non_active_users'      : non_active_users
    }
    return render (request, 'Admins/Users/All_Users.html', context)


# Function to view all Teacher Users
@login_required(login_url='/error_404/')
def all_teacher_users(request):
    if not request.user.is_superuser:
        return redirect('error_404')
    teacher_profile = Profile.objects.filter(user__is_staff=True,
                                             user__is_active=True,
                                             user__is_superuser =False)
    
    total_teacher_profiles  = teacher_profile.count()
    
    context = {
        'teacher_profile'           : teacher_profile,
        'total_teacher_profiles'    : total_teacher_profiles
    }
    return render (request, 'Admins/Users/All_Teacher_Users.html', context)

# Function to view all Student Users
@login_required(login_url='/error_404/')
def all_student_users(request):
    if not request.user.is_superuser:
        return redirect('error_404')
    student_profile = Profile.objects.filter(user__is_active=True,
                                             user__is_staff=False,
                                             user__is_superuser =False)
    
    total_student_profiles      = student_profile.count()
 
    context = {
        'student_profile'           : student_profile,
        'total_student_profiles'    : total_student_profiles

    }
    return render (request, 'Admins/Users/All_Student_Users.html', context)

# Function to view all Admin Users
@login_required(login_url='/error_404/')
def all_admin_users(request):
    if not request.user.is_superuser:
        return redirect('error_404')
    admin_profile = Profile.objects.filter(user__is_active=True,
                                           user__is_staff=True,
                                           user__is_superuser =True)
    
    total_admin_profiles = admin_profile.count()

    context = {
        'admin_profile'         :admin_profile,
        'total_admin_profiles'  : total_admin_profiles
    }
    return render (request, 'Admins/Users/All_Admin_Users.html', context )

# Function to view all Non Active Users
@login_required(login_url='/error_404/')
def all_non_active_users(request):
    if not request.user.is_superuser:
        return redirect('error_404')
    non_active_profile = Profile.objects.filter(user__is_active=False,)

    total_non_acttive_profiles = non_active_profile.count()

    context ={
        'non_active_profile'              : non_active_profile,
        'total_non_acttive_profiles'      : total_non_acttive_profiles
    }

    return render (request, 'Admins/Users/All_Non_Active_Users.html', context)

# --- Users Section Ends ---



# --- Course Categories Section Starts ---

# Function to view all Course Categories
@login_required(login_url='/error_404/')
def all_languages(request):
    if not request.user.is_superuser:
        return redirect('error_404')
    context = {
    'course_languages': Language.objects.all()
    }
    return render(request, 'Admins/Course_Languages/All_Languages.html', context)

# --- Course Categories Section Ends ---



# ------------------------- Admin Dashboard Ends -------------------------