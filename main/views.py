from django.shortcuts import render

def show_main(request):
    context = {
        'namatoko' : 'Pacil Shop',
        'name': 'Erland Hafizh Aristovi',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
