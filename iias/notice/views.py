from django.shortcuts import render

# Create your views here.

def notice(request):
    '''
    Render the notice page
    '''
    context = {'like': '公告事項請留意；錯過可能出問題！' }
    return render(request, 'notice/notice.html', context)