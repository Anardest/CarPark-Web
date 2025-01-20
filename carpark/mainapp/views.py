from django.shortcuts import render

def index(request):
    context = {
        # 'context' : 'Имя',
        # 'date': datetime.now(),
    }
    return render(request, "index.html", context)
