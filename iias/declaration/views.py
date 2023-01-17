from django.shortcuts import render

# Create your views here.

def declaration(request):
    '''
    Render the declaration page
    '''
    context = {'like': '會計申報要正確；保險才能無風險！' }
    return render(request, 'declaration/declaration.html', context)