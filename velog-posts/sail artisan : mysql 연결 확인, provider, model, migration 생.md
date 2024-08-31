<p>sail artisan list
sail list : sail 명령어 확인
sail artisan : sail artisan 명령어 확인</p>
<h2 id="mysql-접속">mysql 접속</h2>
<p><code>sail mysql</code>
데이터베이스 접속</p>
<h2 id="public-과-storage-디렉토리-연결">public 과 storage 디렉토리 연결</h2>
<p><code>sail artisan storage:link</code></p>
<blockquote>
<p>[기능]</p>
</blockquote>
<ul>
<li>퍼블릭 디렉토리와 스토리지 디렉토리의 연결</li>
<li>웹페이지에서 불러오려면 public 디렉토리와 storage 디렉토리 사이에 심볼릭 링크 생성</li>
<li>이를 통해 애플리케이션의 퍼블릭 파일 시스템과 스토리지 파일 시스템 간의 원활한 파일 접근과 관리가 가능해짐</li>
<li>이 심볼릭 링크를 통해 퍼블릭 디렉토리에서 스토리지 디렉토리에 저장된 파일에 쉽게 접근 가능</li>
<li>퍼블릭 디렉토리에서 스토리지 파일에 접근할 수 있으므로 url을 통해 파일을 쉽게 제공 가능</li>
</ul>
<h2 id="새-컨트롤러-파일-생성">새 컨트롤러 파일 생성</h2>
<p><code>sail artisan make:controller NewController</code></p>
<blockquote>
<p>[새 컨트롤러 생성]</p>
</blockquote>
<ul>
<li>이 파일은 웹 애플리케이션의 특정 요청을 처리하는 로직을 포함</li>
<li>생성된 파일은 기본적인 컨트롤러 구조를 포함, 이후 필요한 로직을 추가</li>
<li>생성된 컨트롤러 파일은 기본적으로 'namespace','class' 그리고 '__invoke' 메서드 등을 포함한 기본 구조 </li>
</ul>
<blockquote>
<p>[파일 위치]</p>
</blockquote>
<ul>
<li>프로젝트의 app/Http/Controller 디렉토리에 php 파일 생성</li>
<li>기본적으로 새 컨트롤러는 이 디렉토리에 저장되지만, 네임스페이스를 사용해 하위 디렉토리에 저장될 수 있음</li>
</ul>
<blockquote>
<p>[기능]</p>
</blockquote>
<ul>
<li>웹 애플리케이션의 요청 처리 : 컨트롤러는 라우트와 연결되어 사용자의 요청을 처리하고 ,데이터를 가공하거나, 모델과 상호작용하여 응답을 반환하는 역할 수행</li>
</ul>
<blockquote>
<p>[컨트롤러 활용]</p>
</blockquote>
<ul>
<li>생성된 컨트롤러는 라우트 파일에 등록되어 특정 url로의 접근 시 해당 컨트롤러 메서드가 실행되도록 설정</li>
<li>예를 들어, 'routes/web.php' 파일에 라우트를 추가하여 컨트롤러를 사용 가능<pre><code>Route::get('/example', [NewController::class, 'index']);
</code></pre></li>
</ul>
<pre><code>


## 마이그레이션 파일 생성
`sail artisan make:migration newtable`
&gt; [파일 생성]
- 마이그레이션이란 데이터베이스 구조를 설정하는 파일
- 데이터베이스 테이블을 생성하거나 수정하는 데 필요한 스크립트를 생성
- INFO  Migration [database/migrations/2024_06_09_130500_newtable.php] created successfully.  

&gt; [파일 내용]
- 생성된 마이그레이션 파일에는 'up'메서드와 'down' 메서드가 포함
- up 메서드는 데이터베이스 변경을 정의하며, 새로운 테이블을 만들거나 기존 테이블을 수정하는 등의 작업을 수행
- down 메서드는 up 메서드의 작업을 되돌리는 역할
- up 메서드와 down 메서드를 수정하여 원하는 테이블 구조를 정의

&gt; [데이터베이스 마이그레이션 준비]
- 이 명령어로 생성된 마이그레이션 파일은 데이터베이스 스키마 변경을 위한 스크립트
- 실제로 데이터베이스 변경을 적용하기 위해서는 추가적으로 'sail artisan migrate' 명령어를 실행하여 마이그레이션을 실행
- 변경사항이 있을 때마다 마이그레이션 수행 필요

```php
Schema::create('newtable', function (Blueprint $table) {
    $table-&gt;id();
    $table-&gt;string('name');
    $table-&gt;integer('age');
    $table-&gt;timestamps();
});</code></pre>