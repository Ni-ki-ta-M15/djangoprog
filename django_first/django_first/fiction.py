from django.http import HttpResponse
from django.shortcuts import render


def Greates(request):
    return HttpResponse('Hello, new user! It`s my first nirmal project')


def home(request):
    return render(request, 'home.html')


# def reverse(request):
#     user_original_text = request.GET['usertext']
#     user_reverse_text = request.GET['usertext'][::-1]
#     user_reverse_text_up = user_reverse_text.upper
#
#     return render(request, 'reverse.html', {'user_original_text': user_original_text,
#                   'user_reverse_text': user_reverse_text_up})

def reverse(request):
    user_original_text = request.GET['usertext']
    user_reverse_text_up = request.GET['usertext'][::-1].upper
    len_sent_split = user_original_text.split()
    len_sent = len(len_sent_split)

    return render(request, 'reverse.html',
                  {'user_original_text': user_original_text, 'user_reverse_text': user_reverse_text_up,
                   'len_sent': len_sent})
