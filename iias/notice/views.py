from django.shortcuts import render
from notice.models import Notice, Comment

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