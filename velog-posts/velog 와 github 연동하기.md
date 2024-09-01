<h2 id="1-github에-레포지토리-생성">1. github에 레포지토리 생성</h2>
<h2 id="2-폴더-파일-생성">2. 폴더, 파일 생성</h2>
<p><img alt="" src="https://velog.velcdn.com/images/b4failrise/post/8a84c89f-4d67-4175-8ab8-c71fc869551a/image.png" /></p>
<h2 id="3-update_blogyml-파일에-github-action-작성">3. update_blog.yml 파일에 github action 작성</h2>
<p><code>⛔ git config 계정 및 원격 레포지토리 주소 확인</code>
<code>✔️ GitHub Actions에서 크론 스케줄링은 정확히 1분 단위로 실행되는 것을 보장하지 않을 수 있습니다. GitHub Actions는 매분마다 트리거되도록 설정할 수 있지만, GitHub의 인프라 상태에 따라 약간의 지연이 발생할 수 있습니다. (5분이하로 설정하면 최소 5분마다로도 실행이 안 된다.)</code></p>
<pre><code>name: Update Blog Posts


on:
  push:
      branches:
        - master  # 또는 워크플로우를 트리거하고 싶은 브랜치 이름
  schedule:
    - cron: '*/6 * * * *'  # 6분마다 실행

jobs:
  update_blog:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout
      uses: actions/checkout@v2

    - name: Push changes
      run: |
        git config --global user.name 'b4failrise'
        git config --global user.email 'b4failrise@gmail.com'
        git push https://${{ secrets.GH_PAT }}@github.com/b4failrise/velog.test

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        pip install feedparser gitpython

    - name: Run script
      run: python scripts/update_blog.py
</code></pre><h2 id="4-update_blogpy-파일에-파이썬-스크립트-작성">4. update_blog.py 파일에 파이썬 스크립트 작성</h2>
<p><code>⛔ rss_url 내 벨로그 아이디 확인</code></p>
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
<pre><code>          try: 
            file.write(entry.description)  # 글 내용을 파일에 작성
            print(entry.title)
        except AttributeError as err:
            file.write('')
            print(&quot;empty description&quot;)</code></pre><blockquote>
<p>🚩 <strong>성공 결과</strong> 🚩
  <img alt="" src="https://velog.velcdn.com/images/b4failrise/post/7388b9b2-7298-4d16-be56-a6688bbc5b47/image.png" />
  <img alt="" src="https://velog.velcdn.com/images/b4failrise/post/ba5660e7-0a3c-43ba-b3c6-928b4880b079/image.png" /></p>
</blockquote>
<blockquote>
<p>💢 <strong>nothing to commit, working tree clean</strong> 💢</p>
</blockquote>
<pre><code>  Run python scripts/update_blog.py
  Traceback (most recent call last):
  velog 와 github 연동하기
  empty description
    File &quot;/home/runner/work/velog.test/velog.test/scripts/update_blog.py&quot;, line 49, in &lt;module&gt;
  스프링 프레임워크 첫걸음(목차)
      repo.git.commit('-m', msg)
    File &quot;/opt/hostedtoolcache/Python/3.12.5/x64/lib/python3.12/site-packages/git/cmd.py&quot;, line 986, in &lt;lambda&gt;
      return lambda *args, **kwargs: self._call_process(name, *args, **kwargs)
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File &quot;/opt/hostedtoolcache/Python/3.12.5/x64/lib/python3.12/site-packages/git/cmd.py&quot;, line 1598, in _call_process
      return self.execute(call, **exec_kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File &quot;/opt/hostedtoolcache/Python/3.12.5/x64/lib/python3.12/site-packages/git/cmd.py&quot;, line 1388, in execute
      raise GitCommandError(redacted_command, status, stderr_value, stdout_value)
  git.exc.GitCommandError: Cmd('git') failed due to: exit code(1)
    cmdline: git commit -m Modify post: 스프링 프레임워크 첫걸음(목차)
    stdout: 'On branch main
  Your branch is ahead of 'origin/main' by 2 commits.
    (use &quot;git push&quot; to publish your local commits)
  &gt;
  nothing to commit, working tree clean'</code></pre><blockquote>
<p>➡️ nothing to commit 예외 처리 ➡️</p>
</blockquote>
<pre><code>    if repo.is_dirty():
        repo.git.commit('-m', msg)
    else:
        print(&quot;No changes to commit&quot;)</code></pre><blockquote>
<p>📢 <strong>커스텀 코드 공유</strong> 📢
<code>description AttributeError 예외처리</code>
<code>nothing to commit 예외 처리</code>
<code>post 추가 외에 수정도 commit 반영</code> </p>
</blockquote>
<pre><code>import feedparser
import git
import os
&gt;
# 벨로그 RSS 피드 URL
# example : rss_url = 'https://api.velog.io/rss/@soozi'
rss_url = 'https://api.velog.io/rss/@b4failrise'
&gt;
# 깃허브 레포지토리 경로
repo_path = '.'
&gt;
# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')
&gt;
# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)
&gt;
# 레포지토리 로드
repo = git.Repo(repo_path)
&gt;
# RSS 피드 파싱
feed = feedparser.parse(rss_url)
&gt;
# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    # 파일 이름에서 유효하지 않은 문자 제거 또는 대체
    file_name = entry.title
    file_name = file_name.replace('/', '-')  # 슬래시를 대시로 대체
    file_name = file_name.replace('\\', '-')  # 백슬래시를 대시로 대체
    # 필요에 따라 추가 문자 대체
    file_name += '.md'
    file_path = os.path.join(posts_dir, file_name)
    msg = ''
    if not os.path.exists(file_path):
        msg = f'Add post: {entry.title}'
    else:
        msg = f'Modify post: {entry.title}'
&gt;
    with open(file_path, 'w', encoding='utf-8') as file:
        print(entry.title)
        try: 
            file.write(entry.description)  # 글 내용을 파일에 작성
        except AttributeError as err:
            file.write('')
            print(&quot;empty description&quot;)
&gt;    
    repo.git.add(file_path)
    if repo.is_dirty():
        repo.git.commit('-m', msg)
        print(msg)
    else:
        print(&quot;No changes to commit&quot;)
&gt;    
# 변경 사항을 깃허브에 푸시
repo.git.push()</code></pre>