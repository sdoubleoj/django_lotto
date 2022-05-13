from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
#클래스로 각각 한건씩 케이스를 만든다 생각하면 됨
class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name='Test numbers', text='selected numbers')
        g.generate() # GuessNumbers 클래스의 generate 함수를 실행
        print(g.update_date)
        print(g.lottos)

        # 실제 Test case (OK or FAILED)
        # default로 6개 숫자 x 5set = 30개의 숫자가 생성됨을 확인
        #괄호 안 조건의 True여부 확인해서 generate()함수를 테스트
        #하고자 하는 실험에 따라 aessert문은 다양해짐
        self.assertTrue(len(g.lottos) > 20)
