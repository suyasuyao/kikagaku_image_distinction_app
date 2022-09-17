from django.shortcuts import render,redirect
from .forms import InputForm

def index(request):
    return render(request, 'mlapp/index.html')

def input_form(request):
    # 下記の様に編集
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result') # /resultへ遷移するように変更
    else:
        form = InputForm()
        return render(request, 'mlapp/input_form.html', {'form':form})

def result(request):
    return render(request, 'mlapp/result.html')