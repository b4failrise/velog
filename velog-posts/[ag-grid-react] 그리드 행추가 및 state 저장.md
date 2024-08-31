<h1 id="1-프로젝트-생성-ag-grid-react-및-필요한-패키지-설치">1. 프로젝트 생성, ag-grid-react 및 필요한 패키지 설치</h1>
<pre><code class="language-bash">npx create-react-app ag-grid-react-input
cd ag-grid-react-input
npm install ag-grid-react ag-grid-community</code></pre>
<h1 id="2-패키지-import-및-컴포넌트-함수-생성">2. 패키지 import 및 컴포넌트 함수 생성</h1>
<p>간단히 테스트를 해보길 원하면 src/App.js 수정</p>
<pre><code class="language-jsx">import React, { useState, useRef } from 'react';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';

const App = () =&gt; {return();};
</code></pre>
<h1 id="3-기본-그리드-설정기본-필드-구성">3. 기본 그리드 설정(기본 필드 구성)</h1>
<p>columnDefs 라는 이름의 배열 생성</p>
<pre><code class="language-jsx">const columnDefs = [
    {headerName: 'idx', field: 'idx', editable: true }
    { headerName: 'Name', field: 'name', editable: true },
    { headerName: 'Model', field: 'model', editable: true },
    { headerName: 'Price', field: 'price', editable: true }
]
</code></pre>
<h1 id="4-데이터-초기화-및-새로운-행-추가-기능-구현">4. 데이터 초기화 및 새로운 행 추가 기능 구현</h1>
<pre><code class="language-jsx">const gridRef = useRef();
const [rowData, setRowData] = useState([]);

const addRow = () =&gt; {
  const newRow = {name : '', model:'', price: 0};
  setRowData([...rowData, newRow]);</code></pre>
<h1 id="5-gridrefcurrentapigetselectednodes-를-이용한-변경된-데이터-업데이트-함수-구현--이해-안됨">5. gridRef.current.api.getSelectedNodes() 를 이용한 변경된 데이터 업데이트 함수 구현 =&gt; 이해 안됨</h1>
<p>gridRef.current.api.getSelectedNodes() 이용</p>
<pre><code class="language-jsx">const handleSave(gridApi) =&gt;{
  const selectedNodes = gridApi.getSelectedNodes();
  const selectedData = selectedNodes.map( node =&gt; node.data );
  saveDataToServer(selectedData);
}</code></pre>
<p> 데이터 변경 감지할때마다 state 저장하는 함수</p>
<pre><code class="language-jsx">  const onCellValueChange(params) =&gt; {
    const updatedRowData = rowData.map((row, index) =&gt; {
      return index === params.node.rowIndex ? params.data : row;
    });
    setRowData(updatedRowData);
    console.log('Updated rowData:', updatedRowData); // 변경된 데이터를 저장하거나 서버로 전송할 수 있습니다.
  };</code></pre>
<h1 id="6-post-api-호출-함수-구현">6. POST API 호출 함수 구현</h1>
<pre><code class="language-jsx"></code></pre>
<h1 id="7-return-안에-그리드-컴포넌트-행추가-저장-버튼-생성-및-props-전달">7. return() 안에 그리드 컴포넌트, 행추가, 저장 버튼 생성 및 props 전달</h1>
<pre><code class="language-jsx">return(
  &lt;div&gt;
      &lt;button onClick={addRow}&gt;Add Row&lt;/button&gt;
      &lt;button onClick={() =&gt; handleSave(gridRef.current.api)}&gt;저장&lt;/button&gt;
      &lt;div className=&quot;ag-theme-alpine&quot; style={{ height: 400, width: 600 }}&gt;
        &lt;AgGridReact
          ref={gridRef}    // 컴포넌트 인스턴스의 참조 훅
          rowData={rowData}    // 그리드 데이터
          columnDefs={columnDefs}    // 그리프 필터 정의
          defaultColDef={{ resizable: true }}    // 
          // onCellValueChanged={onCellValueChanged}    // 변경 데이터 업데이트 함수 props로 전달
        /&gt;
      &lt;/div&gt;
    &lt;/div&gt;
);</code></pre>