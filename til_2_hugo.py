# encoding: utf-8
#!/bin/env/python
import os
import codecs
import json
from datetime import datetime


TIL_FOLDER = '../khanhicetea.com/content/til'
DOC_CONTENT = u'''+++
date = "{post_date}"
title = "#TIL {learn_date} : {topics}"
description = "I learned in {learn_date} about {titles}"
categories = {categories}
tags = {tags}
+++

'''


def read_entire_file(file_path):
    with codecs.open(file_path, 'r') as content_file:
        return content_file.read()


def write_entire_file(file_path, content):
    with codecs.open(file_path, 'w', encoding='utf=8') as content_file:
        return content_file.write(content)


def parse_article(content, category):
    pos1 = content.find('- Date : ')
    pos2 = content.find('- Tags : ', pos1)
    pos3 = content.find("\n", pos2)
    pos4 = content.find("##", pos3)
    pos5 = content.find("\n", pos4)
    post = {
        "date": datetime.strptime(content[pos1+9:pos2].strip(), "%Y-%m-%d"),
        "category": category,
        "tags": [t[1:] for t in content[pos2+9:pos3].strip().split(' ')],
        "content": content[pos3:].strip(),
        "title": content[pos4+3:pos5].strip(),
    }

    return post


def convert_til_2_hugo(source, dest):
    excluded_folders = [".git", TIL_FOLDER]
    categories = [f for f in os.listdir(source) if os.path.isdir(f) and f not in excluded_folders]

    data = dict()

    for cat in categories:
        for file in os.listdir(os.path.join(source, cat)):
            raw = read_entire_file(os.path.join(source, cat, file))
            parts = raw.split('/--------------------/')
            for part in parts:
                article = parse_article(part.strip(), cat)
                article_date = article['date'].date().isoformat()
                if article_date not in data:
                    data[article_date] = []
                data[article_date].append(article)

    for post_date in data:
        article_date = datetime.strptime(post_date, "%Y-%m-%d")
        articles = data[post_date]
        content = ""
        categories = ['Today I learned']
        tags = ['til']
        titles = []

        for article in articles:
            content += "\n# " + article['category'].upper()
            content += "\n\n" + article['content'] + "\n"

            titles.append(article['title'].decode('utf-8'))
            categories.append(article['category'])
            for tag in article['tags']:
                tags.append(tag)

        raw_file = DOC_CONTENT.format(
            post_date=article_date.isoformat(),
            titles="; ".join(titles),
            learn_date=post_date,
            topics=", ".join(set(tags)),
            categories=json.dumps(list(set(categories))),
            tags=json.dumps(list(set(tags)))
        )

        write_entire_file(
            os.path.join(dest, "{}.md".format(post_date)),
            raw_file + content.decode('utf-8')
        )


if __name__ == '__main__':
    cwd = os.getcwd()
    convert_til_2_hugo(cwd, os.path.join(cwd, TIL_FOLDER))
    print("Converted !")
