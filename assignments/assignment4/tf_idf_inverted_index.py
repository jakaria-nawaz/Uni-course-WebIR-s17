#!/usr/bin/env python3
# ===========================================================
#                     Group - Gamma                         =
# ===========================================================
# Mohammad Nizam Uddin                                      =
# Md. Shohel Ahamad                                         =
# MD Jakaria Nawaz                                          =
# Shreya Chatterjee                                         =
# ===========================================================

from math import log10, sqrt


class TfIdfInvertedIndex:
    """An index that can efficiently retrieve and tf-idf rank documents."""

    def __init__(self):
        self.term_frequencies = {}
        self.document_frequencies = {}
        self.document_lengths = {}
        self.corpus_size = 0

    def __str__(self):
        from pprint import pformat
        return pformat({
            'term frequencies': self.term_frequencies,
            'document frequencies': self.document_frequencies,
            'document lengths': self.document_lengths,
            'corpus size': self.corpus_size,
        }, indent=2, compact=True)

    def add_document(self, docid, terms):
        """Add a document to the index.

        Args:
            docid: The document ID.
            terms: An iterable of the document's terms.
        """
        self.corpus_size += 1
        for term in set(terms):
            if term not in self.term_frequencies:
                self.term_frequencies[term] = {}
                self.document_frequencies[term] = 0
            self.term_frequencies[term][docid] = terms.count(term)
            self.document_frequencies[term] += 1

    def calc_document_lengths(self):
        """Calculates the lengths of document vector representations.

        Call this after adding all documents and before searching. Don't add any
        documents to the corpus after without re-running this method.
        """
        for doc_no in range(self.corpus_size):
            doc_id  = doc_no+1
            doc_sum = 0
            for k, v in self.term_frequencies.items():
                for ke, vl in v.items():
                    if ke == doc_id:
                        sqr_val = vl*(log10(self.corpus_size/self.document_frequencies[k]))
                        sqr_val = sqr_val**2
                        doc_sum = doc_sum + sqr_val
            self.document_lengths[doc_id] = sqrt(doc_sum)
        # raise NotImplementedError

    def search(self, query_terms):
        """Find all documents matching some query terms and relevance-rank them.

        Args:
            query_terms: An iterable of words of the query.

        Returns:
            A list of pairs of IDs of documents and their relevance scored,
            sorted decreasingly after relevance.
        """
        scores = {}
        if len(query_terms) > 0:
            for query_term in query_terms:
                for k, v in self.term_frequencies.items():
                    if k == query_term:
                        for ke, vl in v.items():
                            score_frag = (log10(self.corpus_size/self.document_frequencies[query_term]))*vl*(log10(self.corpus_size/self.document_frequencies[query_term]))
                            if ke not in list(scores):
                                scores[ke] = score_frag
                            else:
                                scores[ke] += score_frag
            # raise NotImplementedError
            for k, v in scores.items():
                scores[k] = (v/self.document_lengths[k])

        return sorted(scores.items(), key=lambda entry: entry[1], reverse=True)


if __name__ == '__main__':
    index = TfIdfInvertedIndex()
    index.add_document(1, 'coffee coffee'.split())
    index.add_document(2, 'tea cup jar jar tea'.split())
    index.add_document(3, 'cup coffee jar cup'.split())
    index.add_document(4, 'coffee cup coffee jar tea cup coffee jar cup jar'
                       .split())
    index.add_document(5, 'jar water water jar'.split())

    index.calc_document_lengths()
    print('Index after loading document corpus:')
    print(index)

    query = 'cup jar'
    print()
    print('Searching for "{}":'.format(query))
    results = index.search(query.split())
    print(
        '\n'.join(['- Doc {} (score: {})'.format(r[0], r[1]) for r in results]))
