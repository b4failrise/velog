import feedparser
import git
import os

# 벨로그 RSS 피드 URL
# example : rss_url = 'https://api.velog.io/rss/@soozi'
rss_url = 'https://api.velog.io/rss/@b4failrise'

# 깃허브 레포지토리 경로
repo_path = '.'

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 레포지토리 로드
repo = git.Repo(repo_path)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

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

    with open(file_path, 'w', encoding='utf-8') as file:
        print(entry.title)
        try: 
            file.write(entry.description)  # 글 내용을 파일에 작성
        except AttributeError as err:
            file.write('')
            print("empty description")
    
    repo.git.add(file_path)
    if repo.is_dirty():
        repo.git.commit('-m', msg)
        print(msg)
    else:
        print("No changes to commit")
    
# 변경 사항을 깃허브에 푸시
repo.git.push()
