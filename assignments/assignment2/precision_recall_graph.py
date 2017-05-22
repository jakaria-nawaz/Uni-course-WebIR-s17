#!/usr/bin/env python3
# ===========================================================
#                     Group - Gamma                         =
# ===========================================================
# Mohammad Nizam Uddin                                      =
# Md. Shohel Ahamad                                         =
# MD Jakaria Nawaz                                          =
# Shreya Chatterjee                                         =
# ===========================================================

import matplotlib.pyplot as plt
from evaluation import MyRankedRetrievalSystem
from evaluation import MyExpertJury
#from evaluation import precision_at_k

def precision_at_k(Aq, G, k):
    """Calculates the precision@k for a given query."""
    Aq      = Aq[0:k]
    Aq      = set(Aq)
    Aq_I_G  = set.intersection(Aq, G)
    return ((len(Aq_I_G))/len(Aq))

def recall_at_k(Aq, G, k):
    Aq      = Aq[0:k]
    Aq      = set(Aq)
    Aq_I_G  = set.intersection(Aq, G)
    return (len(Aq_I_G)/len(G))

if __name__ == '__main__':
    query = input('Write the query words: ')
    #once in a blue moon
    results = MyRankedRetrievalSystem.exec_query(query)
    gold_standard = MyExpertJury.gold_standard_for_query(query)

    prec_at_k_list = []
    reca_at_k_list = []
    k_length       = len(results)

    for index in range(k_length):
        prec_at_k_list.append(precision_at_k(results, gold_standard, index+1))
        reca_at_k_list.append(recall_at_k(results, gold_standard, index+1))

    print(prec_at_k_list)
    print(reca_at_k_list)
    plt.plot(reca_at_k_list, prec_at_k_list, color='red', label="precesion-recall")
    plt.legend(loc='upper center')
    plt.ylabel('precision')
    plt.xlabel('recall')
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.savefig('precision_recall_graph.png')
    #plt.show()
