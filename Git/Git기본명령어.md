# 소셜 코딩으로 이끄는 Github 실천 기술(오오츠카 히로키) / 제이펍 출판사

## git 기본 사용법
```
-- 리포지토리 초기화. '.git'폴더 생성. 이 폴더에 현재 폴더와 관련된 관리 정보가 저장. working tree라고 
git init부른다. 변경 내역 등 관리.
-- 리포지토리 상태 표시. 
git status
-- 스테이지 영역(커밋 전 임시 영역)에 파일 추가. 
git add 파일명
-- push된 파일 원격지, 원본 한번에 삭제하기
git rm -r 파일명
-- push된 파일 원격지만 삭제하기
git rm -r --cached 파일명
-- 스테이지 영역에 기록된 시점들 파일을 실제 리포지토리 변경 내역에 반영.
git commit -m '첫 커밋'
-- 리포지토리에 커밋된 로그 확인. 
git log
-- 로그 확인시 첫 번째 요약 줄만 보여주기
git log --pretty=short
-- 리드미 관련된 로그만 보기 (폴더 명도 가능)
git log README.md
-- 커밋에서 변경된 내용 함께 확인. (뒤에 파일/폴더명 붙여도 됨)
git log -p
-- working tree, 스테이지 영역, 최신 커밋 사이 변경 확인
git diff
-- 최신 commit과의 차이 확인
git diff HEAD
-- 브랜치 목록 표시, 현재 어떤 브랜치인지.
git branch
-- feature-A 이름의 브랜치 만들고 그 브랜치로 이동
git checkout -b 'feature-A'
-- 현재 브랜치에서 feature-A브랜치를 머지. 옵션은 머지 커밋도 함께 남기고 싶다는 뜻.
git merge --no--ff feature-A
-- 브랜치를 시각적으로 확인
git log --graph
-- HEAD, 스테이지, Working tree를 특정 커밋으로 복원.
git reset --hard 커밋해시값
-- 현재 브랜치 뿐만이 아니라 이 리포지토리에서 진행된 모든 로그 볼 수 있음
git reflog
-- 바로 전에 작성했던 커밋 메세지 수정
git commit --amend
-- add, commit 한번에 하기
git commit -am "바로 애드하고 커밋"
-- 현재 브랜치의 HEAD(최신 commit)를 포함한 두 개의 변경 내역과 관련된 내용 보여짐. 이 두개를 병합
> git rebase -i HEAD~2
pick 7a34294 Add feature-C
pick 6fsdfa2 Fix typo
-- 뭉개고 싶은 커밋에 'fixup'으로 고쳐주고 저장. 
pick 7a34294 Add feature-C
fixup 6fsdfa2 Fix typo
-- 주소의 저장소를 원격 저장소로 설정
git remote add origin git@github.com:사용자명/저장소이름.git
-- -u옵션: 로컬 리포에 있는 현재 브랜치 upstream이 origin 리포의 master 브랜치로 설정.
git push -u origin master
-- 원격의 feature-D브랜치로 push
git push -u origin feature-D
-- 주소의 리포지토리 받아오기
git clone git@github....git
-- 로컬 리포지토리랑 원격 리포지토리 브랜치 모두 표시
git branch -a
-- 원격의 feature-D리포를 내가 새로 만든 feature-D브랜치로 체크아웃
git checkout -b feature-D origin/feature-D
```

## 커밋 메세지
- 첫 번째 줄: 변경 내용 한 줄 요약
- 두 번째 줄: 공백
- 세 번째 줄 이후: 변경과 관련 내용 상세 기록
