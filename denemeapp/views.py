from django.shortcuts import render, get_object_or_404
from .models import Yazi
page_defaults = {
    "title": "başlıksız"
}
def homepage(request):
    yazilar = Yazi.objects.all()
    return render(request,"pages/homepage.html", {
        'yazilar': yazilar
    })


def about(request):
    content = {
        "title":"hakkımızda",
        "body": "<h1>hakkımızda</h1>"
    }
    context = {
        **page_defaults,
        **content
    }

    return render(request,"pages/page.html",context)

def contact(request):
    content = {
        "title":"iletişim",
        "body": "<h1>iletişim</h1>"
    }
    context = {
        **page_defaults,
        **content
    }
    return render(request,"pages/page.html",context)




def blog_detail(request, slug):
    yazi = get_object_or_404(Yazi, slug=slug)
    return render(request, 'pages/blog_detail.html', {
        'yazi': yazi
    })






