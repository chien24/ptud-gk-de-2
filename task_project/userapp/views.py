from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from taskapp.models import  Category
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Tạo profile cho user
            # Profile model chưa được import
            profile = Profile.objects.create(user=user)
            
            # Tạo các danh mục mặc định
            default_categories = ['Công việc', 'Cá nhân', 'Học tập']
            for cat_name in default_categories:
                Category.objects.create(name=cat_name, user=user)
                
            username = form.cleaned_data.get('username')
            messages.success(request, f'Tài khoản cho {username} đã được tạo! Bạn có thể đăng nhập ngay.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Thông tin của bạn đã được cập nhật!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)