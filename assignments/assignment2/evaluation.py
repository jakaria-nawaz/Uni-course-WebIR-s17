#!/usr/bin/env python3
# ===========================================================
#                     Group - Gamma                         =
# ===========================================================
# Mohammad Nizam Uddin                                      =
# Md. Shohel Ahamad                                         =
# MD Jakaria Nawaz                                          =
# Shreya Chatterjee                                         =
# ===========================================================

class MyRankedRetrievalSystem:
    """A dummy ranked retrieval system for Information Retrieval.

    It acts as if it retrieved documents relevant to a query (no actual
    retrieval functionality is implemented, results are hard-coded per query).
    """

    @staticmethod
    def exec_query(query):
        """Executes a query and returns matching document ranked by relevance.

        Args:
            query (str): The query string.

        Returns:
            A list of integers, where each integer represents a document-id.
            Documents are ordered based on relevancy to the query, with the
            document deemed the most relevant taking the first position in the
            list.
        """
        if query == 'pacman':
            return [1, 3, 6, 7, 4, 2, 9, 5, 8, 10]
        elif query == 'zerg rush':
            return [1, 5, 3, 7, 10, 9, 8, 2, 6, 4]
        elif query == 'google in 1998':
            return [3, 2, 9, 5, 4, 1, 10, 8, 6, 7]
        elif query == 'askew':
            return [29, 30, 1, 21, 20, 8, 16, 6, 27, 28, 11, 12, 3, 19, 18, 15,
                    26, 4, 13, 10, 2, 23, 25, 5, 17, 22, 24, 9, 14, 7]
        elif query == 'answer to life the universe and everything':
            return [15, 7, 11, 14, 13, 9, 5, 6, 1, 2, 3, 8, 4, 10, 12]
        elif query == 'once in a blue moon':
            return [6, 5, 4, 1, 13, 15, 12, 11, 10, 2, 8, 9, 3, 7, 14]
        elif query == 'anagram':
            return [3, 8, 10, 12, 15, 5, 9, 14, 2, 4, 7, 6, 1, 11, 13]
        elif query == 'recursion':
            return [3, 13, 11, 2, 4, 5, 12, 9, 15, 14, 1, 8, 10, 7, 6]
        elif query == '_emptyresults':
            return []
        elif query == '_emptygoldstandard':
            return [1, 2, 3]
        elif query == '_emptyboth':
            return []
        else:
            return []


class MyExpertJury:
    """A dummy human expert jury defining gold standards of relevant documents.

    Obviously, it is impossible to code human judgement. Instead, this class
    can be viewed as being a recording of human judgement (gold standards are
    hard-coded per query).
    """

    @staticmethod
    def gold_standard_for_query(query):
        """Returns the gold standard of relevant documents for a given query.

        Args:
            query (str): The query string.

        Returns:
            A set of integers, where each integer represents a document-id of a
            document that was deemed relevant to the query.
        """
        if query == 'pacman':
            return {1, 6, 8, 10}
        elif query == 'zerg rush':
            return {2, 5, 6, 8, 9, 10}
        elif query == 'google in 1998':
            return {3, 4, 6, 7, 8}
        elif query == 'askew':
            return {2, 4, 6, 8, 12, 13, 15, 18, 19, 20, 21, 23, 24, 25, 27}
        elif query == 'answer to life the universe and everything':
            return {2, 4, 5, 7, 9, 14, 15}
        elif query == 'once in a blue moon':
            return {1, 3, 5, 6, 8, 11, 15}
        elif query == 'anagram':
            return {1, 2, 4, 5, 9, 12, 13}
        elif query == 'recursion':
            return {3, 4, 5, 9, 10, 11, 12}
        elif query == '_emptyresults':
            return {1, 2, 3}
        elif query == '_emptygoldstandard':
            return set()
        elif query == '_emptyboth':
            return set()
        else:
            return set()


# def precision(Aq, G):
#     """Calculates the precision for a given query."""
#     Aq_I_G           = set.intersection(Aq, G)
#     return (len(Aq_I_G)/len(Aq))
    #raise NotImplementedError
def precision(query):
    """Calculates the precision for a given query."""
    results = MyRankedRetrievalSystem.exec_query(query)
    gold_standard = MyExpertJury.gold_standard_for_query(query)

    Aq_I_G           = set.intersection(set(results), gold_standard)
    if (len(set(results)) == 0) and ((len(gold_standard)) == 0):
        return 1
    elif (len(set(results)) == 0) or ((len(gold_standard)) == 0):
        return 0
    return (len(Aq_I_G)/len(results))
    #raise NotImplementedError


# def recall(Aq, G):
#     """Calculates the recall for a given query."""
#     Aq_I_G           = set.intersection(Aq, G)
#     return (len(Aq_I_G)/len(G))
    #raise NotImplementedError
def recall(query):
    """Calculates the recall for a given query."""
    results = MyRankedRetrievalSystem.exec_query(query)
    gold_standard = MyExpertJury.gold_standard_for_query(query)
    Aq_I_G           = set.intersection(set(results), gold_standard)
    # if ((len(gold_standard)) == 0):
    #     return 1
    # if (len(set(results)) == 0):
    #     return 0
    if (len(set(results)) == 0) and ((len(gold_standard)) != 0):
        return 0
    elif ((len(gold_standard)) == 0) and (len(set(results)) != 0):
        return 1
    elif ((len(gold_standard)) == 0) and (len(set(results)) == 0):
        return 1
    return (len(Aq_I_G)/len(gold_standard))


# def f1_score(r, P):
#     """Calculates the F1-score for a given query."""
#     return (2*r*P)/(P+r)
    #raise NotImplementedError
def f1_score(query):
    """Calculates the F1-score for a given query."""
    r = recall(query)
    P = precision(query)
    
    if (r == 0) or (P == 0):
        return 0
    return (2*r*P)/(P+r)
    #raise NotImplementedError


# def precision_at_k(Aq, G, k):
#     """Calculates the precision@k for a given query."""
#     Aq      = Aq[0:k]
#     Aq      = set(Aq)
#     Aq_I_G  = set.intersection(Aq, G)
#     return ((len(Aq_I_G))/len(Aq))
    #raise NotImplementedError
def precision_at_k(query, k):
    """Calculates the precision@k for a given query."""
    results = MyRankedRetrievalSystem.exec_query(query)
    gold_standard = MyExpertJury.gold_standard_for_query(query)

    results      = results[0:k]
    results      = set(results)
    Aq_I_G  = set.intersection(results, gold_standard)
    if (len(results) == 0) or ((len(gold_standard)) == 0):
        return 0
    return ((len(Aq_I_G))/len(results))
    #raise NotImplementedError


# def r_precision(Aq, G):
#     """Calculates the r-precision for a given query."""
#     Aq      = Aq[0:len(G)]
#     Aq      = set(Aq)
#     Aq_I_G  = set.intersection(Aq, G)
#     return (len(Aq_I_G)/len(G))
def r_precision(query):
    """Calculates the r-precision for a given query."""
    results = MyRankedRetrievalSystem.exec_query(query)
    gold_standard = MyExpertJury.gold_standard_for_query(query)

    results      = results[0:len(gold_standard)]
    results      = set(results)
    if (len(results) == 0):
        return 0
    elif ((len(gold_standard)) == 0):
        return 1
    Aq_I_G  = set.intersection(results, gold_standard)
    return (len(Aq_I_G)/len(gold_standard))


def mean_average_precision(Aq, G):
    """Calculates the mean average precision for a given set of queries."""
    cum_precision = 0
    for g_doc in G:
        k_val = Aq.index(g_doc)
        cum_precision = cum_precision+precision_at_k(Aq, G, k_val+1)
    return cum_precision/len(G)
    #raise NotImplementedError


if __name__ == '__main__':
    query = 'pacman'

    results = MyRankedRetrievalSystem.exec_query(query)
    gold_standard = MyExpertJury.gold_standard_for_query(query)

    print('Calculating evaluation measures for query "{}"...'.format(query))
    print()
    print('Ranked result set for query was:', results)
    print('Gold standard of relevant documents for query was:', gold_standard)
    print()
    precision = precision(query)
    #precision = precision(set(results), gold_standard)
    print('Precision:', precision)
    recall = recall(query)
    # recall = recall(set(results), gold_standard)
    print('Recall:', recall)
    # print('F1-Score:', f1_score(recall, precision))
    print('F1-Score:', f1_score(query))
    #print('Precision@1:', precision_at_k(results, gold_standard, 1))
    print('Precision@1:', precision_at_k(query, 1))
    # print('Precision@5:', precision_at_k(results, gold_standard, 5))
    print('Precision@5:', precision_at_k(query, 5))
    # print('R-Precision:', r_precision(results, gold_standard))
    print('R-Precision:', r_precision(query))
    print('Average Precision:', mean_average_precision(results, gold_standard))
    #print('Average Precision:', mean_average_precision(results, gold_standard))
