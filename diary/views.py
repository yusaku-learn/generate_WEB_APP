from django.views import View
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import EntryForm
import os
from decouple import config
import requests



class IndexView(View):
    def get(self,request):
        datetime_now=datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
        return render(request,"diary/index.html" , {"datetime_now":datetime_now})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = EntryForm(request.POST)
            if form.is_valid():
                form.save()
                request.session['form_data'] = form.cleaned_data
                return redirect('diary:success_page') #リダイレクト
            else:
                form = EntryForm()
        # context = {
        #     'name':request.POST['name'],
        #     'email':request.POST['email'],
        #     'message': request.POST['message'],
        #     }
        # return render(request, "diary/index.html", context)
        return render(request, "diary/index.html", {'form':form})

    
    



index = IndexView.as_view()


def success_page(request):
    form_data = request.session.get('form_data')

    message = form_data.get('message')

    # 環境変数からOpenAI APIキーを取得
    API_KEY = config('SECRET_KEY_OPENAI')


    header = {
        "Content-Type" : "application/json",
        "Authorization" : f"Bearer {API_KEY}",
    }

    body = f'''
    {{
        "model": "gpt-3.5-turbo",
        "messages": [
            {{ "role": "user", "content": "{message}" }}
        ]
    }}
    '''

    body = f'''
    {{
        "model": "gpt-3.5-turbo",
        "messages": [
            {{ "role": "user", "content": f"こんにちは、私の名前は {form_data['name']} です。" }}
        ]
    }}
    '''

    response = requests.post("https://api.openai.com/v1/chat/completions", headers = header, data = body.encode('utf_8'))


    # レスポンスをJSONとしてパース
    response_json = response.json()

    # 応答部分だけを抽出
    chat_response = response_json['choices'][0]['message']['content']

    # テンプレートに渡すデータを辞書形式にする
    responce_data = {
        'chat_response': chat_response  # ChatGPTの返答のみを辞書に格納
    }

    # テンプレートに辞書型のデータを渡す
    return render(request, 'success.html', responce_data)

    # return render(request, 'success.html', {'form_data': form_data})