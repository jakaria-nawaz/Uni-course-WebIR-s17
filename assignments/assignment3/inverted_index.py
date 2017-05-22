#!/usr/bin/env python3
# ===========================================================
#                     Group - Gamma                         =
# ===========================================================
# Mohammad Nizam Uddin                                      =
# Md. Shohel Ahamad                                         =
# MD Jakaria Nawaz                                          =
# Shreya Chatterjee                                         =
# ===========================================================

class InvertedIndex:
    """An index that can efficiently find all documents containing a word."""

    def __init__(self):
        self.index = {}
        self.wordlist = []

    def add_document(self, id, words):
        """Add a document to the index.

        Args:
            id: The document ID.
            words: An iterable of the document's words.
        """
        self.wordlist.append(words)
        for word in words:
            try:
                posting_list = self.index[word]
            except KeyError:
                self.index[word] = {id}
            else:
                posting_list.add(id)

    def find_documents_with_word(self, word):
        """Find all documents containing a word.

        Args:
            word: The word to search for.

        Returns:
            A set of IDs of documents that contained the word.
        """
        return self.index.get(word, set())

    def check_document_for_phrase(self, doc_words, phrase_words):
        """Check if the document contains the phrase

        Args:
            doc_words: List of words of a document
            phrase_words: List of words of phrase

        Returns:
            Boolean
        """
        # simple solution
        """
        doc_words_string = ' '.join(doc_words)
        phrase_words_string = ' '.join(phrase_words)
        return phrase_words_string in doc_words_string
        """
        total_phrase_words = len(phrase_words)
        result_flag = 0
        iter_val = 0
        for word in doc_words:
            if result_flag == 1:
                break
            if word == phrase_words[0]:
                if total_phrase_words == 1:
                    result_flag = 1
                    break
                inner_iter = iter_val+1
                for in_val in range(total_phrase_words-1):
                    if inner_iter > (len(doc_words)-1):
                        break
                    elif doc_words[inner_iter] == phrase_words[in_val+1]:
                        inner_iter = inner_iter+1
                        if in_val+1 == (total_phrase_words-1):
                            result_flag = 1
                    else:
                        break
            iter_val = iter_val+1
        if result_flag == 1:
            return True
        else:
            return False

    def find_documents_with_phrase(self, words):
        """Find all documents containing a phrase (a sequence of words)

        Args:
            words: An iterable of words to search for.

        Returns:
            A set of IDs of documents that contained the phrase.
        """
        phrase_words_list = list(words)
        doc_with_phrase = []
        list_of_sets = []
        iter_val = 0
        for word in words:
            words[iter_val] = self.find_documents_with_word(word)
            list_of_sets.append(words[iter_val])
        common_docs = set.intersection(*list_of_sets)
        common_docs = list(common_docs)
        for common_doc in common_docs:
            check_result = self.check_document_for_phrase(self.wordlist[common_doc-1], phrase_words_list)
            if check_result:
                doc_with_phrase.append(common_doc)
        return set(doc_with_phrase)

    def __str__(self):
        return '\n'.join(
            ('{} -> [{}]'.format(word, ', '.join(map(str, posting_list)))
             for (word, posting_list) in self.index.items()))

if __name__ == '__main__':
    index = InvertedIndex()
    index.add_document(1, 'coffee coffee'.split())
    index.add_document(2, 'tea cup jar jar tea'.split())
    index.add_document(3, 'cup coffee jar cup'.split())
    index.add_document(4, 'coffee cup coffee jar tea cup coffee jar cup jar'
                       .split())
    index.add_document(5, 'jar water water jar'.split())
    print('Documents with word "jar":', index.find_documents_with_word('jar'))
    print('Documents with phrase "tea cup":',
          index.find_documents_with_phrase('tea cup'.split()))
