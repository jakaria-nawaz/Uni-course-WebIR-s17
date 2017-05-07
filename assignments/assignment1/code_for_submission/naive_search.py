#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ===========================================================
#                     Group - Gamma                         =
# ===========================================================
# Mohammad Nizam Uddin                                      =
# Md. Shohel Ahamad                                         =
# MD Jakaria Nawaz                                          =
# Shreya Chatterjee                                         =
# ===========================================================

def naive_search(filename, keyword):
    titleSet = [] # set of titles that has the keyword match
    keyword = keyword.lower() # make the keyword lower case
    for doc in iter_corpus_docs(filename):
        # print(doc['id'], doc['url'], doc['title'], doc['content'])
        match_result = find_match(doc['content'], keyword)
        if match_result:
            titleSet.append(doc['title'])

    return set(titleSet)
    # raise NotImplementedError

def find_match(doc_content, keyword):
    doc_content = doc_content.lower() # converts the content text into lowercase
    content_words = doc_content.split() # split at whitespace the strings of the content
    return keyword in content_words # match keyword in content_words, if found returns to naive_search function

def iter_corpus_docs(filename):
    # Iterates over all documents in a corpus.

    import re
    doc_pattern = re.compile('^<doc id="(.*)" url="(.*)" title="(.*)">$')

    cur_doc = None
    with open(filename, encoding="utf-8") as file:
        for line_no, line in enumerate(file):
            line = line[:-1]
            if line == '<corpus>' or line == '</corpus>':
                continue
            elif line.startswith('<doc'):
                m = doc_pattern.match(line)
                id, url, title = m.group(1), m.group(2), m.group(3)
                cur_doc = {
                    'id': id,
                    'url': url,
                    'title': title,
                    'content': '',
                }
            elif line == '</doc>':
                assert cur_doc, ('doc-end-tag without corresponding '
                                 'doc-start-tag on line {}.'.format(line_no))
                yield cur_doc
                cur_doc = None
            else:
                cur_doc['content'] += line + '\n'

if __name__ == '__main__':
    # matches = naive_search('simplewiki-20160501-extracted-devel.xml', 'test')
    matches = naive_search('simplewiki-20160501-extracted.xml', 'test')
    for match in matches:
        print('-', match)
    print('({} matches found)'.format(len(matches)))
