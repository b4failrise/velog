<p>라라벨 세일이 웹 페이지를 구동하는 방법
<img alt="" src="https://velog.velcdn.com/images/b4failrise/post/5896381e-644a-4a83-8df1-b0b70c870903/image.png" /></p>
<ul>
<li>sail 을 이해하기 위해선 도커 선행 이해 필요</li>
<li>개발을 하는 내컴퓨터에서 자체 호스팅과 데이터베이스를 실행시키던 과거와 달리 이들을 분리하고 서버로 자주 이용되는 리눅스에서 파일을 관리</li>
<li>설정된 값을 토대로 각 기능별로 컨테이너라는 또 다른 가상 호스팅 컴퓨터를 만들고 이렇게 만든 컴퓨터들이 서로 통신하면 필요 데이터를 요청</li>
<li>일반 도커에서 docker-compose 를 사용하지만 라라벨에서는 sail 명령어로 대체</li>
</ul>
<p>모든 sail 명령어들은 <code>sail up -d</code>로 컨테이너를 실행시킨 상태에서만 동작</p>
<p>sail composer : 외부 라이브러리 설치
sail artisan : 프로젝트 파일 생성 및 수정
sail node : 프론트엔드 node.js 관련 실행
sail npm : 라라벨에 node.js 패킺 설치
sail mysql : mysql 컨테이너 명령창 불러오기</p>
<p>sail artisan list : 모든 명령어 확인</p>
<p>파일 생성(수동 생성x), 데이터베이스 관련 작업을 할 때 artisan명령어를 사용</p>
<p>naming rule
아티즌 명령어로 컨트롤로, 서비스 컨테이너, 서비스 프로바이더 같은 기능 파일을 만들려고 할 때 이름 뒤에는 식별자를 붙이는 것을 권장
예를 들어 일반 컨트롤러를 만든다면 &quot;sail artisan make:controller SecurityController&quot; 와 같이 생성</p>