from django.shortcuts import render

# ADD --MA-- irei usar templates para carregar css e js , verificação se estará whitenoise a funcionar
def index(request):
    context={}
    return render(request, 'index.html', context)
