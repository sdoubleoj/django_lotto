from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm


# Create your views here.
def index(request): #views의 함수들은 무조건 request를 언제나 먼저 파라미터로 받아줌!
    lottos = GuessNumbers.objects.all() #ORM

    # {"lottos"(키값):lottos} == context
    return render(request, 'lotto/default.html', {"lottos":lottos})
                                                    #보통 키값을 변수명과 동일하게 해줌

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")


def post(request):

    #서버로 들어온 요청이 'POST'라면:
    if request.method == 'POST':

        # #방법1: 손수 저장하는 (form 태그 안 쓸 때)
        # user_name = request.POST['name']
        # user_text = request.POST['text']
        # row = GuessNumbers(name=user_name, text=user_text)
        # row.generate() #self.save()

        form  = PostForm(request.POST) #유저에 의해 채워진 양식

        if form.is_valid(): #유효성 체크(models.py에서 정의된 바와 같은지 , 원래 내부적으로 가진 함수
            lotto = form.save(commit=False) #defualt: commit=True (DB table에 실제로 저장)
            # commit=False로 중간저장만 하고 DB에 실제로 반영되는 것을 미루고 그 1개 행을 받아와 후처리 해주기 위함
            lotto.generate() # <-내부의 self.save()로 DB에 최종적으로 물리적 저장

            return redirect('index') #urls.py의 index의 url별명

    #GET요청이라면:
    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})


def detail(request, lottokey):

    lotto = GuessNumbers.objects.get(id=lottokey) #models.py에서 table인 클래스 생성시 pk인 id열이 자동생성됨!

    return render(request, 'lotto/detail.html', {'lotto':lotto})
