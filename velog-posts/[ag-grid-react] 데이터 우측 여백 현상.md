<h2 id="현상">현상</h2>
<p>aggrid 에서 맨 우측 데이터 컬럼이 여백이 생기는 현상이 발생할 수 있다.</p>
<h2 id="해결-방법">해결 방법</h2>
<p>columnDef 를정의할 때 'flex:&lt;그리드 가용 너비에서 차지할 단위&gt;' 속성을 부여하여 해결 할 수 있다.</p>
<h2 id="columndef-예시">ColumnDef 예시</h2>
<pre><code class="language-js">{
  headerName: '비고',
  flex: 1,
  width: 80,
  minWidth: 80,
  field: 'note',
  editable: true,
  cellEditor: 'agLargeTextCellEditor',
  cellEditorPopup: true,
  valueGetter: (params: any) =&gt; {
    return convertSpecialCharToHtml(params.data?.note);
  },
}</code></pre>
<h2 id="소스코드-설명">소스코드 설명</h2>
<p>flex
flex 속성은 이 열이 가용공간에서 얼마나 많은 비율을 차지할 지 결정
flex : 1 은 해당 열이 가용 너비 내에서 1단위 만큼 차지하도록 설정</p>
<h2 id="flex-속성의-역할">flex 속성의 역할</h2>
<ol>
<li>공간 분배:</li>
</ol>
<p>그리드의 가용 공간이 있을 때, flex: 1을 사용한 '비고' 열은 이 가용 공간의 일정 비율을 차지합니다.
다른 열이 flex 속성을 사용하지 않는 경우, '비고' 열이 모든 가용 공간을 차지합니다.</p>
<ol start="2">
<li>가변 너비:</li>
</ol>
<p>그리드의 전체 너비가 변동될 때, '비고' 열의 너비도 비율에 따라 유동적으로 조정됩니다.
이로 인해 열의 너비가 고정되지 않고, 그리드의 크기에 따라 적절히 조정됩니다.</p>
<h2 id="정리">정리</h2>
<p>flex 속성은 AgGrid에서 유연하고 반응적인 열 너비를 제공하는 데 중요한 역할을 합니다. '비고' 열이 그리드의 가용 너비에서 차지할 비율을 정의하고, 그리드의 크기가 변경될 때 자동으로 조정되어 다양한 화면 크기에서 최적의 사용자 경험을 제공</p>