<h2 id="개요">개요</h2>
<p>MVC 패턴과 템플릿엔진은 항상 서로 따라다니는 개념이다.
MVC 패턴은 웹 애플리케이션의 기본 구조 중 하나로 MODEL-VIEW-CONTROLLER 로 구성하는 것을 말한다.</p>
<h2 id="model-view-controller">MODEL-VIEW-CONTROLLER</h2>
<ol>
<li>MODEL</li>
</ol>
<ul>
<li>애플리케이션의 데이터와 비즈니스 로직을 관리한다. </li>
<li>데이터베이스와의 상호작용 및 데이터 검증 수행</li>
</ul>
<ol start="2">
<li>VIEW</li>
</ol>
<ul>
<li>사용자에게 데이터를 표시</li>
<li>HTML, CSS, JS를 사용하여 사용자가 보는 화면을 렌더링</li>
</ul>
<ol start="3">
<li>CONTROLLER</li>
</ol>
<ul>
<li>사용자 입력을 처리하고 모델과 뷰를 연결</li>
<li>요청을 받아 모델을 업데이트하고, 그 결과를 뷰로 전달</li>
</ul>
<h2 id="템플릿엔진">템플릿엔진</h2>
<p>백엔드 프레임워크에서 처리되는 데이터를 통신없이 다루어 사용자가 보는 화면을 쉽게 개발하게 도와주는 도구</p>
<h3 id="spring-mvc--템플릿엔진">Spring MVC + 템플릿엔진</h3>
<ol>
<li>thymeleaf</li>
<li>JSP(Java Server Pages)</li>
<li>FreeMarker</li>
<li>Velocity</li>
<li>Groovy templates</li>
<li>Mustache</li>
</ol>