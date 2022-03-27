# Git TroubleShooting
## Git 사용중 자주 일어나는 문제 해결 방법!
#
## Remote에 올라간 파일/폴더 삭제
- 실수로 remote repository에 불필요한 파일/폴더를 Push했다. 
- .gitignore에 추가하고 삭제 후 push해도 원격에서는 지워지지 않는다.
  
Case.1) 로컬과 리모트 모두 지우고 싶다.
```
 git rm -r 파일/폴더명
```

Case.2) 로컬에는 남겨두고 리모트에서만 지우고 싶다. 
```
git rm -r --cached 파일/폴더명
```
#
## 실수로 master 브랜치에서 작업한내용 복구
- 실수로 작업(Topic) 브랜치가 아닌 메인(Master) 브랜치에서 작업하고 커밋했다.
- Master는 원위치하고, 작업한 소스는 살리고 싶다!!

Case.1) 다행히 PUSH는 하지 않았다.
```
-- branch 확인
git branch
-- 임시 branch 생성
git branch tmp
--- master branch로 이동
git checkout master
-- master branch 롤백(바로 전)
git reset --hard HEAD~
-- 작업 branch로 이동
git checkout [branch명]
-- tmp의 파일을 가져오기
git merge --no-ff tmp
-- tmp branch 삭제
git branch -d tmp
```
Case.2) PUSH까지 해버렸다. 
```
-- 임시 branch 생성
git branch tmp
--- master branch로 이동
git checkout master
-- master branch 롤백(바로 전)
git reset --hard HEAD~
-- 적용 전 소스 push
git push -f origin master
-- 작업 branch로 이동
git checkout [branch명]
-- tmp의 파일을 가져오기
git merge --no-ff tmp
-- tmp branch 삭제
git branch -d tmp
```

#
## 실수로 작업중인 브랜치를 삭제
- 작업 중이던 Topic 브랜치를 실수로 삭제했다. (-D)
- git reset으로 브랜치는 복구되지 않는다.
- 브랜치를 그대로 복원하고 싶다.
```
-- 작업 branch를 실수로 삭제
git branch -D [branch명]
--  reflog에서 해쉬id값 확인
git reflog 
-- branch 해쉬id 시점으로 생성
git checkout -b [branch명] [해쉬id값]
```

#
## 특정 태그로 긴급 롤백 & 다시 배포
- 버그 수정(hotfix)해서 Tag 0.2.1 배포 후 

Case.1) 예기치 못한 장애가 발생했다. 얼른 0.2.0으로 Rollback 하고 다시 배포하자!
```
-- 임시 branch 생성 (0.2.1 임시저장)
git branch tmp
-- tag 0.2.0 으로 reset
git reset --hard 0.2.0
-- 0.2.0 reset한 소스를 배포
git push origin +master



```
Case.2) 0.2.1의 소스를 이용해서 0.2.2를 작업하자.
```
-- 소스수정
git flow hotfix start 0.2.1
-- tmp에 백업해둔 소스 가져오기
git merge --no-ff tmp
-- tmp는 삭제
git branch -D tmp
-- 수정완료 후 커멋 후 flow finish
git flow hotfix finish 0.2.2
```
