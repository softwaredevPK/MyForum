from django.shortcuts import render

# Create your views here.


def main_page(request):
     return render(request, 'forum/base_template.html')  # temporary, to see how it looks



