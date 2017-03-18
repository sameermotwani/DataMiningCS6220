import sys
from bs4 import BeautifulSoup as Soup
from collections import Counter
from collections import defaultdict
import timestring

posts_by_tag = defaultdict()
tags_by_year = defaultdict()
tags=list()


def populate_posts_by_tag(tag,post_id):
    global posts_by_tag
    if tag == '':
        return
    if post_id == '':
        return

    if tag not in posts_by_tag:
        posts_by_tag[tag] = set()
    posts_by_tag[tag].add(int(post_id))


def populate_tags_by_year(tag,year):
    global tags_by_year
    if tag == '':
        return
    if year == '':
        return

    if tag not in tags_by_year:
        tags_by_year[tag] = list()
    tags_by_year[tag].append(year)


def parseLog(file):
    count=0
    with open(file, encoding='utf8') as handler:
        soup = Soup(handler,"html.parser")
        for message in soup.findAll('row'):
            msg_attrs = dict(message.attrs)
            #print(msg_attrs['id'])
            if 'tags' in msg_attrs:
                id = msg_attrs['id']
                year = timestring.Date(msg_attrs['creationdate']).year
                #print(year)
                msg_attrs=(msg_attrs[u'tags'].replace('<','').replace('>',','))
                for msg in msg_attrs.split(','):
                    tags.append(msg)
                    populate_posts_by_tag(msg,id)
                    populate_tags_by_year(msg,year)
                #count=count+1

            # if count == 5:
            #     break

if __name__ == "__main__":

    parseLog("programmers.stackexchange.com/Posts.xml")
    tags=list(filter(None, tags))
    counts=dict()
    #counts=Counter(tags)
    #print(Counter(tags).most_common(20))
    #print(posts_by_tag)
    print(tags_by_year)