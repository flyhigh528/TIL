# Docker
<img src="./docker.jpg" title="Docker Title" alt="Docker_Whale"></img><br/>
1. 도커란, 간단하게 말해 서버환경에서의 다양한 프로그램, 실행환경을 **컨테이너**라는 격리된 환경에서 실행할 수 있게 해주는 **컨테이너 기반의 오픈소스 가상화 플랫폼** 입니다.

이를 이용하면 복잡한 서버환경을 코드로 쉽게 관리할 수 있고 안정적인 배포환경 (무중단 배포 등) 구성할 수 있습니다.

2. Docker 설치 Windows 10)   
   ```
   https://docs.docker.com/docker-for-windows/install/ 다운로드 후 설치
   ```
3. Docker 기본 명령
   1. 이미지 관련 📜
      1. docker pull [image]:latest : dockerhub에서 이미지를 가져온다.
         (:latest를 붙이면 최신버전, 생략가능)
      1. docker rmi [이미지id or name] :  이미지 삭제
      2. docker rmi -f [이미지id or name] : 이미지 삭제(컨테이너 포함)
      4. docker image rm [이미지id or name] : 이미지 삭제
      5. docker image prune : 사용하지 않는 모든 image 삭제
      6. docker images : 이미지 목록 보기
      7. docker system df : 디스크 사용량 확인
      8. docker image ls : 이미지 디스크 사용량 확인
   2. 컨테이너 관련 📦
      2. docker ps -a : 모든 컨테이너 목록 출력
      3. docker run [options] image[:TAG|@DIGEST] [COMMAND] [ARG...] : 컨테이너 실행
      ``` docker run -d -p 8080:8080 -p 1521:1521 [이미지명]```
         1. 옵션
         - -d	detached mode 흔히 말하는 백그라운드 모드
         - -p	호스트와 컨테이너의 포트를 연결 (포워딩)
         - -v	호스트와 컨테이너의 디렉토리를 연결 (마운트)
         - -e	컨테이너 내에서 사용할 환경변수 설정
         - --name	컨테이너 이름 설정
         - --it	-i와 -t를 동시에 사용한 것으로 터미널 입력을 위한 옵션 (컨테이너의 표준 입력과 로컬 컴퓨터의 키보드 입력을 연결)
         - --rm	프로세스 종료시 컨테이너 자동 제거
         - --link	컨테이너 연결 [컨테이너 명:별칭]
      4. docker start [컨테이너 id or name] : 컨테이너 시작
      5. docker restart [컨테이너 id or name] : 컨테이너 재시작
      6. docker attach [컨테이너 id or name] : 컨테이너 접속
      7. docker stop [컨테이너 id or name] : 컨테이너 정지
         1. Bash Shell에서 'exit' 또는 'Ctrl + D'를 입력하면 컨테이너가 정지된다.
         2. 'Ctrl + P', 'Ctrl + Q'를 차례대로 입력하면 컨테이너를 정지하지 않고 빠져나온다.(detach)
      8. docker rm  [컨테이너 id or name] : 컨테이너 삭제
      9.  docker rm 'docker ps -a -q' : 모든 컨테이너 삭제
      10. docker exec -it [실행중인 컨테이너 id or name] 명령어 : 실행중인 컨테이너의 명령 실행
      11. docker rename [변경전컨테이너명] [변경후컨테이너명]