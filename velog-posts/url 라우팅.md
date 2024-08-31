<h2 id="url-라우팅-개념">url 라우팅 개념</h2>
<blockquote>
<p>브라우저 주소창에 임의의 주소를 입력하면 원하는 페이지가 나오도록 처리하는 것</p>
</blockquote>
<h2 id="동작-방식-및-코드-작성-방법">동작 방식 및 코드 작성 방법</h2>
<blockquote>
</blockquote>
<ul>
<li>RouteServiceProvider 라는 파일에서 routes/web.php와 api.php를 호출하며 시작</li>
<li>일반적으로 페이지를 불러오는 코드는 web.php에, 외부에서 불러오는 REST API를 api.php에 설정
<img alt="" src="https://velog.velcdn.com/images/b4failrise/post/7094eb21-1a55-4728-a8cb-59be187c4d6a/image.png" />
<img alt="" src="https://velog.velcdn.com/images/b4failrise/post/70693d4d-d561-454e-b8f7-aa53714b1872/image.png" />
<img alt="" src="https://velog.velcdn.com/images/b4failrise/post/c689669b-e815-401b-9019-5422112698a3/image.png" />
<img alt="" src="https://velog.velcdn.com/images/b4failrise/post/d5ceff9e-d61a-45fa-9b72-823367dcd8af/image.png" />
<img alt="" src="https://velog.velcdn.com/images/b4failrise/post/da1946a2-0f86-42b7-bd6e-072261bce381/image.png" /></li>
</ul>
<h2 id="routes-디렉토리-파일">routes 디렉토리 파일</h2>
<p>api.php</p>
<blockquote>
</blockquote>
<ul>
<li>api 요청을 받아 controller 에 처리를 위임하여 데이터 처리 및 반환하기 위한 라우팅 모음</li>
<li>api.php에 설정하면 <a href="http://localhost/api/%EB%A1%9C">http://localhost/api/로</a> 페이지가 호출</li>
<li>해당 파일에 정의된 api들은 주소에 /api 입력 필수</li>
</ul>
<p>web.php</p>
<blockquote>
</blockquote>
<ul>
<li>블레이드 템플릿을 반환하기 위한 라우팅 모음</li>
<li>web.php에 호출하면 <a href="http://localhost/%EB%A1%9C">http://localhost/로</a> 호출</li>
</ul>
<h2 id="api-파일에서-라우팅-방법">api 파일에서 라우팅 방법</h2>
<blockquote>
</blockquote>
<ul>
<li>크게 http 메소드와 구현부를 정의</li>
<li>http 메소드 : get|post</li>
<li>구현부 : 응답함수|작업을 전달할 컨트롤러와 함수</li>
<li>클라이언트 요청 데이터 처리가 필요한 경우 Request 컨트롤러 사용</li>
<li>Request 컨트롤러를 서비스컨테이너 방식으로 개발자가 가공하여 DB에 저장하거나 출력하는 것이 백엔드 작업의 핵심</li>
<li>Route::get|post('연결 주소', '응답 함수'|'작업을 넘길 컨트롤러')</li>
<li>ex) Route::get('/new',function(Request $request){});</li>
<li>ex) Route::get('/new',[NewController::class],index);<pre><code>Route::get('/test', function (Request $request){
  $data = $request -&gt;input('name');
  return $data;
 });</code></pre><h2 id="url-주소를-활용하는-법">URL 주소를 활용하는 법</h2>
<blockquote>
</blockquote>
</li>
<li>무조건 정해진 주소뿐만이 아니라 상황에 따라 다른 값을 주소로 받을 수 있다.</li>
<li>이를 감지하기 위해서는 {} 대괄호를 사용</li>
<li>대괄호의 수와 function 안의 괄호에 있는 변수의 수를 맞추어야 한다.</li>
<li>제약을 걸수도 있다. 숫자만 또는 영어 알파벳일 경우를 가려낼 수 있다.</li>
<li>{} 대괄호를 통해 받는 값은 숫자, 알파벳, 한글 어떤 문자든 가능</li>
<li>제약조건을 걸어 문자를 한정할 수 있다. =&gt;whereNumber</li>
<li>일단 다 받고 숫자가 아니면 실행을 취소</li>
<li>블로그에서 발행되는 글처럼 같은 레이아웃의 페이지에 숫자만 다르게 받아서 각 숫자에 일치하는 글을 불러올 때 이 같은 라우팅 기법을 사용 </li>
<li>서비스 컨테이너가 넣어주는 컨트롤러와 함께 사용할 경우 반드시 컨트롤러 변수를 맨 앞에 배치. 그다음 대괄호와 연결된 변수를 배치<pre><code>Route::get('/route/{first}/{second}', function ($first ,$second){ return &quot;첫번째 인수 -&quot;.$first.&quot;두번째 인수-&quot;.$second;});
Route::get('/order/{number}',function ($number){return $number;})-&gt;whereNumber($number);
Route::get('/mix/{number}',function (Request $request, $number){ return $number;})-&gt;whereNumber($number);</code></pre></li>
</ul>