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

print ("Enter your keyword",)
prompt = '> '

search_string = input(prompt)

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

file_size_set = [] # file size list for plot
time_set = [] # time set for plot
import matplotlib.pyplot as plt
import time
import os

if __name__ == '__main__':
    for i in range(1, 10): # iterates the loop of 10 files
        print('For corpus ',i)
        start = time.time() # takes the start time of the search
        matches = naive_search('simplewiki-20160501-extracted-%r.xml'% i, search_string)
        for match in matches:
            size_in_byte = os.path.getsize('simplewiki-20160501-extracted-%r.xml'% i) # gets the file size in bytes
            size_in_mebibyte = size_in_byte/1048576 # converts file size to MiB
            print('-', match)
        stop = time.time() # takes the end time of the search
        duration = (stop-start)/60 # converts seconds into minutes
        print ('Search time :','%.2f' % duration, 'minutes')
        print ('File size : ','%.2f' % size_in_mebibyte,'MiB')
        file_size_set.append('%.2f' % size_in_mebibyte)
        time_set.append('%.2f' % duration)
        print('({} matches found)'.format(len(matches)))
        print('\n')
    # print (file_size_set)
    # print (time_set)
    plt.plot(file_size_set, time_set)
    lines = plt.plot(file_size_set, time_set)
    plt.ylabel('search duration (minutes)')
    plt.xlabel('file size (MiB)')
    plt.setp(lines, color='r', linewidth=2.0)
    plt.show()
