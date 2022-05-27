from django.shortcuts import redirect, render

# Create your views here.
def main(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "index.html")