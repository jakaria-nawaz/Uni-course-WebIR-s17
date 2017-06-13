#!/usr/bin/env python3
# ===========================================================
#                     Group - Gamma                         =
# ===========================================================
# Mohammad Nizam Uddin                                      =
# Md. Shohel Ahamad                                         =
# MD Jakaria Nawaz                                          =
# Shreya Chatterjee                                         =
# ===========================================================

class QueryLikelihoodInvertedIndex:
    def __init__(self):
        self.term_frequencies = {}
        self.document_frequencies = {}
        self.document_tokens = {}
        self.corpus_size = 0

    def add_document(self, docid, terms):
        """Add a document to the index.

        Args:
            docid: The document ID.
            terms: An iterable of the document's terms.
        """
        self.document_tokens[docid] = terms
        self.corpus_size += 1
        for term in set(terms):
            if term not in self.term_frequencies:
                self.term_frequencies[term] = {}
                self.document_frequencies[term] = 0
            self.term_frequencies[term][docid] = terms.count(term)
            self.document_frequencies[term] += 1
    def unigram_model_cal(self, docid, total_tokens, query_term, doc_tokens):
        gamma_val = 0.5
        try:
            term_freq = self.term_frequencies[query_term]
            cf = sum(term_freq.values())
        except KeyError:
            term_freq = {0:0}
            cf = 0
        T  = total_tokens
        try:
            tf = term_freq[docid]
        except KeyError:
            tf = 0
        dl = len(doc_tokens)
        equation_reulst = (0.5*(tf/dl)+(1-0.5)*(cf/T))
        return equation_reulst

    def search(self, query_terms):
        all_tokens = self.document_tokens
        total_tokens = sum(len(v) for v in all_tokens.values())
        count_query  = len(query_terms)
        liklihood_result = []
        for doc in self.document_tokens:
            prob_value = 1
            iter_val   = 1
            token_set = set(self.document_tokens[doc])
            query_set = set(query_terms)
            if token_set.intersection(query_set):
                for term in query_terms:
                    equation_reulst = self.unigram_model_cal( doc, total_tokens, term, self.document_tokens[doc] )
                    prob_value      = prob_value * equation_reulst
                    if iter_val == count_query:
                        iter_val = iter_val
                        key_val  = (doc, prob_value)
                        if (prob_value != 0.0016) and (prob_value != 0.0):
                            liklihood_result.append(key_val)
                    iter_val = iter_val + 1
        liklihood_result = sorted(liklihood_result,key=lambda x:(-x[1],x[0]))
        return liklihood_result

if __name__ == '__main__':
    index = QueryLikelihoodInvertedIndex()
    index.add_document(1, 'coffee coffee'.split())
    index.add_document(2, 'tea cup jar jar tea'.split())
    index.add_document(3, 'cup coffee jar cup'.split())
    index.add_document(4, 'coffee cup coffee jar tea cup coffee jar cup jar'
                       .split())
    index.add_document(5, 'jar water water jar'.split())
    query = 'jar cup'
    query_result = index.search(query.split())
    print(query_result)
