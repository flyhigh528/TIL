# Jupyter Notebook 설치 & 크롬 기본 브라우저로 설정방법
1. Anaconda 사이트에서 다운로드 & 설치
2. Anaconda Prompt 실행
3. jupyter notebook --generate-config 입력 후 실행
4. 생성된 jupyter_notebook_config.py의 경로로 이동 후 편집기로 실행
5. c.NotebookApp.browser 검색
6. #c.NotebookApp.browser의 주석을 풀고 아래 내용을 입력 후 저장
```
import webbrowser
webbrowser.register('chrome', None, webbrowser.GenericBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
c.NotebookApp.browser = 'chrome'
```
7. jupyter notebook을 실행하여 크롬으로 잘 뜨는지 확인!



