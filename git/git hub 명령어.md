# git hub 명령어



### 기본 원리

README로 프로젝트 설명

.gitignore 로 `git add .` 사용시 모든 파일 다 안가져오게 제한하기.



협업을 하면 push 할 때 레포랑 자료가 같아야함. 서로 같지 않다면 같게 만들기 위해서 pull 로 당겨오기.

pull 도 안되는 경우는 새로운 자료가 추가되어서 레포랑 pc자료가 다른 경우가 아니라, 기존 자료에서 수정되어서 자료가 다른 경우. 이경우 visual studio code에서 조정 가능

이게 너무 불편하니까 `branch` 있는 것. 브랜치는 로컬과 git에서 하는 걸로 나뉨

상대방 git을 코멘트 or 수정 위해서는 folk, pull reques 사용



### 기본 단어들



add -> commit -> push

pull

branch

switch

clone

merge



### 기본 명령어들



1. git -add .

2. git commit -m "`<message>`"

3. git push origin master

4. git pull origin master -> "상대방 가져오기"

5. git branch -> 브랜치 확인

6. git branch `<branch name>` -> 브랜치 생성

7. git switch `branch name` -> 브랜치 이동

8. git clone `<URL>` -> 레포 컴 복사.

9. git  log -> commit 기록들 확인

10. git log --oneline -> commit 이름 확인(코드네임)

   

   

   ### branch

   

   ##### 로컬에서 branch 생성후 합병

   

   branch 마다 파일이 다름.

   

   커밋할 branch에서 커밋

   

   master로 들어가서 merge `git merge <branch name>`

   

   ##### github에서 브랜치 합병

   

   ### folk 방법

   

   상대 GIT 에서 FOLK

   

   FOLK 복사본을 내 컴에 CLONE

   

   CLONE한 후 수정(VISUAL STUDIO CODE )

   !!add commit push 다시~!!

   

   상대 git hub 사이트 pull request 가기

   

   업로드~

   

   ### 과거 log로 돌아가기

   

   git log --oneline 으로 로그 확인하면 커밋 이름을 확인 가능

   

   git reset -h -> 인자 값들 확인

   

   git  reset --hard `<커밋이름>` => 입력한 커밋으로 가고, 그 커밋 이후의 것들은 없어짐

   

   

   

   

   

   

   

   

   