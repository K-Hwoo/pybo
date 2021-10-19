from ..models import Question

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

@login_required(login_url='common:login')
def vote_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    vote_only = question.voter.all()
    for vote_list in vote_only :
        if request.user == vote_list :
            messages.error(request, '이미 추천한 글입니다.')


    if request.user == question.author :
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)
