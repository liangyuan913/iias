from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from notice.models import Notice, Comment
from notice.forms import NoticeForm
import notice

# Create your views here.

def notice(request):
    '''
    Render the notice page
    '''
    # notices = Notice.objects.all()
    notices = {notice:Comment.objects.filter(notice=notice) for notice in Notice.objects.all()}
    
    # context = {'like': '公告事項請留意；錯過可能出問題！' }
    context = {'like': '公告事項請留意；錯過可能出問題！','notices':notices}
    return render(request, 'notice/notice.html', context)


def noticeCreate(request):
    '''
    Create a new notice instance
     1. If method is GET, render an empty form
     2. If method is POST,
         * validate the form and display error messages if the form is invalid
         * else, save it to the model and redirect to the notice page
    '''
    #TODO: finish the code
    #return render(request, 'notice/notice.html')
    template = 'notice/noticeCreate.html'
    #GET
    if request.method == 'GET':
        return render(request, template, {'noticeForm':NoticeForm()})
    
    #POST
    noticeForm = NoticeForm(request.POST)
    if not noticeForm.is_valid():
        return render(request, template, {'noticeForm':noticeForm})
    
    noticeForm.save()
    #return notice(request)
    messages.success(request, '公告已新增發佈')
    return redirect('notice:notice')

def noticeRead(request, noticeId):
    '''
    Read an notice
        1. Get the notice instance; redirect to the 404 page if not found
        2. Render the noticeRead template with the notice instance and its associated comments
    '''
    notice = get_object_or_404(Notice, id=noticeId)
    context = {
        'notice': notice,
        'comments':Comment.objects.filter(notice=notice)   
    }
    return render(request, 'notice/noticeRead.html', context)
