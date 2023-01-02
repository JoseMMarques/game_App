from django.shortcuts import render


def homepage(request):

    template_name = 'game_features/homepage.html'
    context = {}
    return render(request, template_name, context)
