import requests
import re
import urllib
from html.parser import HTMLParser

def all_target_links(link):
    try:
        #r = requests.get(link).text
        r ="""
            <a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">
            """

        pattern = r'<a href=".*">'
        a_tags = re.findall(pattern, r)
        targets = []
        for t in a_tags:
            target = t[9::]
            pointer = target.find('"')
            target = target[:pointer:]
            targets.append(target)

        pattern = r"<a href='.*'>"
        a_tags = re.findall(pattern, r)
        for t in a_tags:
            target = t[9::]
            pointer = target.find("'")
            target = target[:pointer:]
            targets.append(target)
        return targets
    except:
        return None


#link = input()




#links_list = all_target_links(link)
links_list = all_target_links('aaa')

print(links_list)

pure_set = set()
for lnk in links_list:
    parsed = urllib.parse.urlparse(lnk)
    if parsed is not None:
        pure_set.add(parsed.netloc)


pure_list = []
for lnk in pure_set:
    pure_list.append(lnk)

pure_list.sort()
for lnk in pure_list:
    print(lnk)
