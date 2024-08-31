<h2 id="현상">현상</h2>
<p>스프링 빌드 환경을 계속 변경하는 상황에서 프로젝트가 실행이 안 되는 상황이 발생하였다.
프로젝트를 열면 아래와 같은 빌드 에러가 발생하였다.
<code>dependency requires at least jvm runtime version 17. this build uses a java 8 jvm</code></p>
<h2 id="원인">원인</h2>
<p>JVM 버전 셋팅이 잘못 설정된 경우에 빌드 에러가 발생할 수 있다.
스프링버전마다 최소 실행 JVM 버전이 존재한다.
3.x 버전부터는 17 이상을 사용해야 한다.</p>
<h2 id="해결-방법">해결 방법</h2>
<p>두 개 경로의 JVM 버전 설정을 수정해야 한다.</p>
<ol>
<li>Settings &gt; Build, Execution, Deployment &gt; Build Tools &gt; Gradle &gt; Gradle JVM</li>
<li>Project Structure &gt; Project &gt; SDK</li>
</ol>