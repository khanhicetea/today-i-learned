# encoding: utf-8
#!/bin/env/python
import os
import codecs
import json
from datetime import datetime


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
        "title": content[pos4+3:pos5].strip(),
    }

    return post


def convert_til_2_readme(source, template_file, dest):
    excluded_folders = [".git", ".vscode"]
    categories = [f for f in os.listdir(source) if os.path.isdir(f) and f not in excluded_folders]
    categories.sort()
    all_articles = []
    content = "| Table of Contents | :point_down: |\n| -------- | -------- |\n| :new: **Top 5 recent learning** | |\n"
    cat_content = ""

    for cat in categories:
        cat_articles = []
        for file in os.listdir(os.path.join(source, cat)):
            raw = read_entire_file(os.path.join(source, cat, file))
            parts = raw.split('/--------------------/')
            for part in parts:
                article = parse_article(part.strip(), cat)
                article['file_name'] = file
                cat_articles.append(article)
                all_articles.append(article)
        cat_articles.sort(key=lambda a: a['date'])
        
        cat_content += "| :books: **{}** [ {} articles ] | |\n".format(cat, len(cat_articles))
        for article in cat_articles:
            cat_content += "| [{}]({}/{}) | {} |\n".format(
                article['title'], article['category'], article['file_name'],
                article['date'].strftime('%Y-%m-%d'))

    all_articles.sort(reverse=True, key=lambda a: a['date'])
    for article in all_articles[0:5]:
        content += "| [{}] [{}]({}/{}) | {} |\n".format(
            article['category'], article['title'],
            article['category'], article['file_name'],
            article['date'].strftime('%Y-%m-%d'))

    content += cat_content
    format_content = read_entire_file(template_file)
    write_content = format_content.replace('{TOC}', content)
    write_entire_file(dest, write_content.decode('utf-8'))


if __name__ == '__main__':
    cwd = os.getcwd()
    convert_til_2_readme(cwd, os.path.join(cwd, 'README.md.template'), os.path.join(cwd, 'README.md'))
    print("Updated !")
