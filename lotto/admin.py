from django.contrib import admin
from lotto.models import GuessNumbers
#from .models import GuessNumbers
#admin.py 기준으로 models.py가 같은 폴더에 있을 때, lotto 생략 가

# Register your models here.
admin.site.register(GuessNumbers)
