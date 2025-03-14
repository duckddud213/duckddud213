import feedparser, time
from datetime import datetime
from datetime import timedelta

URL = "https://ragabys.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """

<details>
<summary>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Cowboy%20Hat%20Face.png" alt="Cowboy Hat Face" width="25" height="25" /> Status
</summary>

![](./profile-3d-contrib/profile-night-rainbow.svg)


[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=duckddud213)](https://solved.ac/duckddud213)[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=ragabys)](https://solved.ac/ragabys)

![mazandi profile](http://mazandi.herokuapp.com/api?handle=duckddud213&theme=dark)![mazandi profile](http://mazandi.herokuapp.com/api?handle=ragabys&theme=dark)


![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=duckddud213&layout=compact&theme=onedark)


![duckddud213's GitHub stats](https://github-readme-stats.vercel.app/api?username=duckddud213&show_icons=true&theme=radical)

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fduckddud213%2Fhit-counter&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</details>

<details>
  <summary>
   <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Astonished%20Face.png" alt="Astonished Face" width="25" height="25" /> Skills & Tools
  </summary>
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Hundred%20Points.png" alt="Hundred Points" width="25" height="25" />
  <img src="https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white">
  <img src="https://img.shields.io/badge/Kotlin-0095D5?&style=for-the-badge&logo=kotlin&logoColor=white">
  
  <br/>
  <br/>
  
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Hundred%20Points.png" alt="Hundred Points" width="25" height="25" />
  <img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white">
  <img src="https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white"> 
  
  <br/>
  <br/>
  
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Hundred%20Points.png" alt="Hundred Points" width="25" height="25" />
  <img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white">
  <img src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white">
  <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white">
  <img src="https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white">
  
  <br/>
  <br/>
  
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Hundred%20Points.png" alt="Hundred Points" width="25" height="25" />
  <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white">
  <img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">
  <img src="https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white">
  <img src="https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white">
  <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white">

  <br/>
  <br/>

  
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Hundred%20Points.png" alt="Hundred Points" width="25" height="25" />
  <img src="https://img.shields.io/badge/Adobe%20After%20Effects-9999FF.svg?style=for-the-badge&logo=Adobe%20After%20Effects&logoColor=white">
  <img src="https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white">
  <img src="https://img.shields.io/badge/Prezi-%23000000.svg?style=for-the-badge&logo=Prezi&logoColor=white">
  <img src="https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white">
  
  <br/>
  <br/>
  
 
</details><br/>


## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Beating%20Heart.png" alt="Beating Heart" width="25" height="25" /> 블로그 최신 글

"""  # list of blog posts will be appended here

now = datetime.now()
diffdays = timedelta(hours=9)
currentTime = now + diffdays
nowDatetime = currentTime.strftime('%Y-%m-%d %H:%M:%S')
markdown_text += f"#### [{nowDatetime} 기준]<br/>\n"

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
