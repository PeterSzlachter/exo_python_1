from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "blog/index.html")


def article(request, numero_article):
    if numero_article in ["01", "02", "03"]:
        return render(request, f"blog/article_{numero_article}.html")
    return render(request, "blog/article_not_found.html0")

# def article_02(request):
#     return render(request, "blog/article_02.html")
#
# def article_03(request):
#     return render(request, "blog/article_03.html")
