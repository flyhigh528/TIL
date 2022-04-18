

from logging import raiseExceptions

class soldouterror(Exception):
    pass

chicken = 10
waiting =1
while(True):
    try:
        print("남은치킨{}".format(chicken))
        order = int(input("몇마리주문?"))
        if order <0:
            raise ValueError
        elif order > chicken:
            print("재료가 부족합니다.")

        else:
            print("대기번호 {0} {1} 마리 주문 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
        
        if chicken == 0:
            raise soldouterror
    except ValueError:
        print("잘못된 주문입니다.")
    except soldouterror:
        print("재료가 모두 소진되었습니다.")
        break
        