from django.shortcuts import render, redirect
from .forms import BootstrapUserCreationForm

def register(request):
    if request.method == 'POST':
        form = BootstrapUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('login')  # You need to define the 'login' URL name
    else:
        form = BootstrapUserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})
