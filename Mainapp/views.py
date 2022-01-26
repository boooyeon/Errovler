from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm
from Mainapp.models import Board, Comment

def home(request):
    board_list = Board.objects.order_by('-view')[:5]
    # b_no = board_list.objects.filter(b_no = b_no)
    # comment_list = Comment.objects.filter(b_no = b_no)
    # comment_cnt = len(comment_list)

    context = {'board_list': board_list,
                # 'comment_cnt': comment_cnt,
                }

    return render(request, 'Main/home.html',context)


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        print('d')
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')

            user = authenticate(username=username, password=raw_password, first_name=first_name)
            login(request, user)
            return render(request, 'Main/login.html')
    else:
        form = UserForm()
    return render(request, 'Main/signup.html', {'form': form})