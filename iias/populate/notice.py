from populate import base
from notice.models import Notice, Comment

titles = ['Django 快速入門教學', '5分鐘快速入門，打造一個簡單Python網頁', \
          'Django 網頁應用程式框架入門', '從0 到 50 初探 如何使用Django 架構出一個網站', 
          'Django 初心者之旅', '傳承D的意志~ 邁向Django的偉大航道']
comments = ['簡單易懂', '寫什東西啊??', '您的觀點很有趣', '文章還不錯！', '學好框架不容易', '感謝大大分享！']

def populate():
    print('Populating notices and comments ...', end='')
    Notice.objects.all().delete()
    Comment.objects.all().delete()
    
    for title in titles:
        notice = Notice()
        notice.title = title
        for j in range(20):
            notice.content += title + '\n'
        notice.save()
        for comment in comments:
            Comment.objects.create(notice=notice, content=comment)
    print('done')    
    
if __name__ == '__main__':
    populate()
