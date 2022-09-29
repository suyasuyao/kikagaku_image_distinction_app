from email import message
from django.shortcuts import render,redirect
from .forms import InputForm, LoginForm, SignUpForm
import joblib
import numpy as np
from .models import Customer, ModelFile 

from django.contrib.auth import login, authenticate 
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required # 追加

from .forms import ImageForm

from model.animal_model import Net

import torch
# import pandas as pd
from torchvision import transforms
from PIL import Image

# モデルの読み込み
#loaded_model = joblib.load('model/ml_model.pkl') 

net = Net().cpu().eval()
net.load_state_dict(torch.load('model/animal_weight.pt', map_location=torch.device('cpu')))


#推測結果の数値をもとに文字に戻す。

def index(request):
    return render(request, 'mlapp/index.html')

@login_required
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
    # 最新の登録者のデータを取得

    data = Customer.objects.order_by('id').reverse().values_list('limit_balance', 'education', 'marriage', 'age')

    # x = np.array([data[0]])
    # y = loaded_model.predict(x)
    # y_proba = loaded_model.predict_proba(x)
    # y_proba = y_proba * 100 # 追加
    # y, y_proba = y[0], y_proba[0] # 追加

  # 推論結果を保存
    # customer = Customer.objects.order_by('id').reverse()[0] # Customerの切り出し
    # customer.proba = y_proba[y]
    # customer.result = y
    # customer.save() # データを保存

    # 編集
    return render(request, 'mlapp/result.html', {'y':y, 'y_proba':round(y_proba[y], 2)})

def history(request):
    if request.method == 'POST': # POSTメソッドが送信された場合
        d_id = request.POST # POSTされた値を取得→顧客ID
        d_customer = Customer.objects.filter(id=d_id['d_id']) # filterメソッドでidが一致するCustomerのデータを取得
        d_customer.delete() # 取得した顧客データを消去
        customers = Customer.objects.all() # 顧客全データを取得
        return render(request, 'mlapp/history.html', {'customers':customers})
    else:
        customers = Customer.objects.all()
        return render(request, 'mlapp/history.html', {'customers':customers})

# ログインページ
class Login(LoginView):
    form_class = LoginForm
    template_name = 'mlapp/login.html'

class Logout(LogoutView):
    template_name = 'mlapp/base.html'

def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      #フォームから'username'を読み取る
      username = form.cleaned_data.get('username')
      #フォームから'password1'を読み取る
      password = form.cleaned_data.get('password1')
      # 読み取った情報をログインに使用する情報として new_user に格納
      new_user = authenticate(username=username, password=password)
      if new_user is not None:
         # new_user の情報からログイン処理を行う
        login(request, new_user)
        # ログイン後のリダイレクト処理
      return redirect('index')
    else :
      return render(request, 'mlapp/signup.html', {'form': form}) 
  # POST で送信がなかった場合の処理
  else:
    form = SignUpForm()
    return render(request, 'mlapp/signup.html', {'form': form})

def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_name = request.FILES['image']
            img_url = 'media/documents/{}'.format(img_name)
            animal_name = '動物名'
            proba = '3'


            # 最新の画像のデータを取得

            # data = ModelFile.objects.order_by('id').reverse().values_list('image')

            # x = np.array([data[0]])
            # y = loaded_model.predict(x)
            # y_proba = loaded_model.predict_proba(x)
            # y_proba = y_proba * 100 # 追加
            # y, y_proba = y[0], y_proba[0] # 追加

          # 推論結果を保存
            modelfile = ModelFile.objects.order_by('id').reverse()[0]
            # image = modelfile.image 

            # pred_imgs = []
            # for (img, label) in test:
            #   pred_imgs.append(img)
            # pred_imgs = torch.stack(test_imgs).to('cuda')

            # y = torch.argmax(net(test_imgs), dim=1).cpu().detach().numpy()

            # pd.Series(y, name='class').to_csv('submission.csv',index_label='id')

            img_url = request.session.get('image_url')
            transform = transforms.Compose([
                transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            ])
            img = Image.open(img_url)
            img = transform(img)

            # net = Net()
            # net.load_state_dict(torch.lord())

            with torch.no_grad():
              y = net(img.unsqueeze(0))

            request.session['y'] = y
            

          
            modelfile.proba = proba
            modelfile.animal_name = animal_name
            modelfile.save() # データを保存



        
            context = {'img_url':img_url,'animal_name': animal_name, 'proba':proba}

            
        return render(request, 'mlapp/image.html', context)
    else:
        form = ImageForm()
        return render(request, 'mlapp/index.html', {'form':form})
