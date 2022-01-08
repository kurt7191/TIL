# git command

> git의 기본 명령어를 저장



![Git - Git 기초](command.assets/areas.png)



##### init

- `.git` 폴더를 생성해주는 명령어. 처음 한 번만 실행한다.



##### add

working directory에 있는 파일을 staging area 에 올리는 명령어.



- 기본 사용법
  - file name에 `.` 을 입력하면 모든 파일 폴더를 한 번에 올림

```bash
git add <file name>
```



##### commit

staging area에 있는 파일들을 하나의 commit으로 저장하는 명령어 



- 기본 사용법
  - `-m` : 커밋 메세지를 작성하기 위한 옵션, `-` 은 주로 옵션을 이야기할 때 사용함

```bash
git commit -m "message"
```



##### remote

원격저장소를 관리하기 위한 명령어



- add : 원격 저장소를 추가하는 명령어

  ```bash
  git remote add <remote name> <URL>
  ```



- remove : 원격저장소를 제거

```bash
git remote remove <remote name>
```



##### push

로컬에 저장되어 있는 커밋들을 원격저장소에 업로드 하는 명령어



- 기본 사용방법

  ```bash
  git push <remote name> master
  ```



##### status

git의 현재 상태를 확인하는 명령어



- 기본 명령어

```bash
git status
```



