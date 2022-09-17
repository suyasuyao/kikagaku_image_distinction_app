# kikagaku_loan_screening_app2
# 起動時


```
python manage.py runserver
source djangovenv/bin/activate.fish
cd mlproject
```

#　DBデータ飛んだときつかう

```
python3 manage.py createsuperuser
#user root メール　: test@example.com　パスワード　root

python3 manage.py migrate
python3 manage.py makemigrations
```

# herokuデプロイするとき
```
git subtree push --prefix mlproject heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
#user yoo メール　: test@example.com　パスワード　yyoo1122

```