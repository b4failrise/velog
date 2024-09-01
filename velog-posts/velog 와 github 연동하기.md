<blockquote>
<p>💢 <strong>The requested URL returned error: 403</strong> 💢</p>
</blockquote>
<pre><code>Run git config --global user.name 'b4failrise'
remote: Permission to b4failrise/velog.test.git denied to github-actions[bot].
fatal: unable to access 'https://github.com/b4failrise/velog.test/': The requested URL returned error: 403
Error: Process completed with exit code 128.```




&gt; 💬 원격지 접근 권한 문제로 가정 💬
403오류는 해당 레포지토리 주소에 접근 권한이 없을 경우 발생한다고 한다.
git remote url 등을 수정하여 조치하라는 가이드도 있었다.
`git remote set-url origin https://YOURUSERNAME@github.com/USERNAME/REPOSITORY.git`
그러나 github action 에서 수행되기 때문에 remote url을 지정할 필요는 없어보였다.



&gt; 🛠️ **첫번째 시도 : Workkflow permmisions 수정** 🛠️
token에 부여되는 작업권한인 Workflow permissions 를 수정해보았는데 동일한 에러 로그가 찍혔다.
그러나 어느 순간부터 오류 로그가 바뀌어 있었다. (조치 완료)
![](https://velog.velcdn.com/images/b4failrise/post/f61a34ec-9227-4a5a-b979-7f9a0b2bf4e8/image.png)


&gt; 💢 **AttributeError: object has no attribute 'description'** 💢
Run script 중 오류 발생</code></pre><p>Run python scripts/update_blog.py
Traceback (most recent call last):
  File &quot;/opt/hostedtoolcache/Python/3.12.5/x64/lib/python3.12/site-packages/feedparser/util.py&quot;, line 156, in <strong>getattr</strong>
    return self.<strong>getitem</strong>(key)
           ^^^^^^^^^^^^^^^^^^^^^
  File &quot;/opt/hostedtoolcache/Python/3.12.5/x64/lib/python3.12/site-packages/feedparser/util.py&quot;, line 113, in <strong>getitem</strong>
    return dict.<strong>getitem</strong>(self, key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyError: 'description'
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File &quot;/home/runner/work/velog.test/velog.test/scripts/update_blog.py&quot;, line 38, in 
    file.write(entry.description)  # 글 내용을 파일에 작성
               ^^^^^^^^^^^^^^^^^
  File &quot;/opt/hostedtoolcache/Python/3.12.5/x64/lib/python3.12/site-packages/feedparser/util.py&quot;, line 158, in <strong>getattr</strong>
    raise AttributeError(&quot;object has no attribute '%s'&quot; % key)
AttributeError: object has no attribute 'description' ```</p>
<blockquote>
<p>💬 <strong>entry 객체에 description 속성이 없어서 발생하는 것으로 가정</strong> 💬
  테스트용으로 등록한 게시물에 내용이 없었다.
  <img alt="" src="https://velog.velcdn.com/images/b4failrise/post/11b4fcd7-9f82-4adf-b7fa-4b682653a54f/image.png" /></p>
</blockquote>
<blockquote>
<p>🛠️ <strong>빈 내용이 없도록 작성</strong> 🛠️
  위에 해당 게시물에 내용을 추가하여 작성해본다.
  다른 모든 게시물에는 빈 내용이 있는지는 모르겠다.</p>
</blockquote>
<blockquote>
<p>🚩 성공 결과 🚩
  <img alt="" src="https://velog.velcdn.com/images/b4failrise/post/7388b9b2-7298-4d16-be56-a6688bbc5b47/image.png" />
  <img alt="" src="https://velog.velcdn.com/images/b4failrise/post/ba5660e7-0a3c-43ba-b3c6-928b4880b079/image.png" /></p>
</blockquote>
<blockquote>
<p>➡️ 빈 description 예외처리 ➡️</p>
</blockquote>
<blockquote>
<p>❗블로그 수정과 스크립트 수정이 바로 반영되진 않음❗
  <img alt="" src="https://velog.velcdn.com/images/b4failrise/post/35fe63eb-55ce-462f-b250-2a8e239c7328/image.png" />
  <img alt="" src="https://velog.velcdn.com/images/b4failrise/post/e44c5106-a289-483d-8c3a-daebd7720c8b/image.png" /></p>
</blockquote>