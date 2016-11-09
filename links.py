import requests
import re


first_link= input()
last_link = input()

def all_target_links(link):
    try:
        r = requests.get(link)
        pattern = r'<a href=".*">'
        a_tags = re.findall(pattern, r.text)
        targets = []
        for t in a_tags:
            target = t[9::]
            pointer = target.find('"')
            target = target[:pointer:]
            targets.append(target)
        return targets
    except:
        return None

targets = all_target_links(first_link)

def slt(targets):
    for t in targets:
        second_line_targets = all_target_links(t)
        for slt in second_line_targets:
            if slt == last_link:
                return True
    return False

print(["No", "Yes"][slt(targets)])
