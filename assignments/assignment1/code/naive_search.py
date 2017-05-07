#!/usr/bin/env python3

def naive_search(filename, keyword):
    """Find documents in a corpus that contain a keyword.

    The search is case-insensitive.

    Args:
        filename: Path to the corpus file.
        keyword: The keyword that returned documents should contain.

    Returns:
        A set of the titles of all documents that contained the word.
    """
    titleSet = []
    keyword = keyword.lower()
    for doc in iter_corpus_docs(filename):
        match_result = find_match(doc['content'], keyword)
        if match_result:
            titleSet.append(doc['title'])
    return set(titleSet)
    # raise NotImplementedError

def find_match(doc_content, keyword):
    doc_content = doc_content.lower()
    content_words = doc_content.split()
    return keyword in content_words

def iter_corpus_docs(filename):
    """Iterates over all documents in a corpus.

    Example:
        Use this function like this::

            for doc in iter_corpus_docs("simplewiki-20160501-extracted-1.xml"):
                print(doc['id'], doc['url'], doc['title'], doc['content'])

    Args:
        filename: Path to the corpus file.

    Returns:
        An iterator over all documents in the corpus. Each element of the
        iterator is a dict that represent one document, e.g.::

            {'id': '1',
             'url': 'https://simple.wikipedia.org/wiki?curid=1',
             'title': 'April',
             'content': '...'}
    """
    import re
    doc_pattern = re.compile('^<doc id="(.*)" url="(.*)" title="(.*)">$')

    cur_doc = None
    with open(filename) as file:
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
    matches = naive_search('simplewiki-20160501-extracted-devel.xml', 'test')
    for match in matches:
        print('-', match)
    print('({} matches found)'.format(len(matches)))
