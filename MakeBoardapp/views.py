from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from matplotlib.style import context

from .forms import BoardPost
from Mainapp.models import Board, Comment
from django.contrib.auth.models import User
from django.utils import timezone

from Mainapp.models import Board
from Mainapp.models import QnA_Board

def board_detail(request, b_no):
    board_detail = Board.objects.get(b_no = b_no)
    comment_list = Comment.objects.filter(b_no = b_no)
    comment_cnt = len(comment_list)
    print(board_detail.title)
    context = {'board_detail': board_detail,
                'comment_list':comment_list,
                'comment_cnt':comment_cnt}
    return render(request, 'MakeBoard/reading.html',context)

def writing(request):
    return render(request, 'MakeBoard/writing.html')

def qna_board_write(request):
    login_session = request.session.get('login_session','')
    context = {'login_session': login_session}

    if request.method == 'GET':
        write_form = BoardPost()
        context['forms'] = write_form
        return render(request, 'MakeBoard/writing.html', context)

    elif request.method == 'POST':
        write_form = BoardPost(request.POST)
        if write_form.is_valid():
            writer = request.user.first_name
            board = QnA_Board(
                title=write_form.title,
                contents=write_form.contents,
                writer =writer,
                category=write_form.category
            )
            board.save()
            return redirect('/Board/board')
        else:
            context['forms'] = write_form
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
            return render(request, 'MakeBoard/writing_error.html', context)

def solboard_write(request):
    login_session = request.session.get('login_session','')
    context = {'login_session': login_session}

    if request.method == 'GET':
        write_form = BoardPost()
        context['forms'] = write_form
        return render(request, 'MakeBoard/writing.html', context)

    elif request.method == 'POST':
        write_form = BoardPost(request.POST)
        if write_form.is_valid():
            writer = request.user.first_name
            board = Board(
                title=write_form.title,
                contents=write_form.contents,
                writer =writer,
                category=write_form.category
            )
            board.save()
            return redirect('/Board/solboard')
        else:
            context['forms'] = write_form
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
            return render(request, 'MakeBoard/writing_error.html', context)


def comment(request):
    if request.method == 'POST':
        contents = request.POST.get('contents')
        b_no = request.POST.get('b_no')
        print(contents, b_no)

    try:
        username = request.user.first_name
        comment = Comment.objects.create(b_no_id=b_no, contents=contents, writer = username)
        comment.save()
        return redirect('MakeBoardapp:detail_board' , b_no)

    except:
        return render(request, 'MakeBoard/reading.html')

    return render(request, 'MakeBoard/writing.html')

def photoboard(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio/portfolio.html', {'portfolios': portfolios})

