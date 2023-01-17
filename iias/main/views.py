from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

# def main(request):
#     '''
#     Show 'Hello world!' in the main Page
#     '''
#     return HttpResponse('Hello world!')
def main(request):
    '''
    Render the main page
    '''
    context = {'like': '會計帳務夠健康，永續經營有保障！' }
    return render(request, 'main/main.html', context)

def about(request):
    '''
    Render the about page
    '''
    context = {'like': '會計帳務打基礎；保險業務達目標！' }
    return render(request, 'main/about.html',context)
