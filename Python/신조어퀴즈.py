# 나도코딩 코딩퀴즈4
class Word:
    def __init__(self, Q, A, B, answer):
        self.Q = Q
        self.A = A
        self.B = B
        self.answer = answer
    
    def show_question(self):
        print("{} 의 뜻은? \n1.{} \n2.{}".format(self.Q, self.A, self.B))
    
    def check_answer(self, input_a):
        if input_a == self.answer:
            print("정답입니다.")
        else:
            print("삐빅!")        



word = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)

word.show_question()
word.check_answer(int(input("=> ")))