class japanaPackage:
    def detail(self):
        print("일본 온천 투어 고고싱 10만원")

if __name__ == "__main__"        :
    print("직접호출됬음")
    trip_to = japanaPackage()
    trip_to.detail()
else:
    print("외부호출")