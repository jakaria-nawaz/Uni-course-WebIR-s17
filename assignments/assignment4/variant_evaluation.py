#!/usr/bin/env python3
# ===========================================================
#                     Group - Gamma                         =
# ===========================================================
# Mohammad Nizam Uddin                                      =
# Md. Shohel Ahamad                                         =
# MD Jakaria Nawaz                                          =
# Shreya Chatterjee                                         =
# ===========================================================

import os
import re
from glob import glob
from importlib import import_module


def iter_lisa_docs(lisa_dir):
    doc_pattern = re.compile('Document +?(?P<id>\d+?)\n'
                             '(?P<title>.+?)\n *?\n'
                             '(?P<abstract>.+?)\n'
                             + '\\*' * 44 + '\n',
                             re.DOTALL)

    for filename in ['LISA0.001', 'LISA0.501', 'LISA1.001', 'LISA1.501',
                     'LISA2.001', 'LISA2.501', 'LISA3.001', 'LISA3.501',
                     'LISA4.001', 'LISA4.501', 'LISA5.001', 'LISA5.501',
                     'LISA5.627', 'LISA5.850']:
        seen_ids = set()
        with open(os.path.join(lisa_dir, filename)) as file:
            file = file.read()  # reads whole file into memory, usually bad!
            for match in doc_pattern.finditer(file):
                id = int(match.group('id'))

                # The following code is unfortunately necessary because some IDs
                # occur multiple times in the database.
                if id in seen_ids:
                    continue
                seen_ids.add(id)

                yield {
                    'id': id,
                    'title': match.group('title'),
                    'abstract': match.group('abstract'),
                }


def iter_lisa_queries(lisa_dir):
    qrels = {}
    with open(os.path.join(lisa_dir, 'LISARJ.NUM')) as file:
        split = list(map(int, file.read().split()))
        i = 0
        while i < len(split):
            num_relevant = split[i + 1]
            qrels[split[i]] = set(split[i + 2:i + 2 + num_relevant])
            i += num_relevant + 2

    with open(os.path.join(lisa_dir, 'LISA.QUE')) as file:
        for line in file:
            id = int(line[:-1])
            query = ''
            for line in file:
                query += line[:-1] + ' '
                if line.endswith(' #\n'):
                    break
            query = query[:-3]  # remove training ' # ' again.
            yield {
                'id': id,
                'query': query,
                'relevant': qrels[id],
            }


def precision_at_k(results, gold_standard, k):
    if not results:
        if not gold_standard:
            return 1
        return 0

    first_k_results = results[:k]
    relevant_first_k_results = filter(lambda result: result in gold_standard,
                                      first_k_results)
    num_relevant_first_k_results = sum(1 for _ in relevant_first_k_results)

    return num_relevant_first_k_results / k


def average_precision(results, gold_standard):
    if not gold_standard:
        return 1
    if not results:
        return 0

    precisions = []
    for relevant_result in gold_standard:
        try:
            index = results.index(relevant_result)
        except ValueError:  # Thrown if result is not in results
            precisions.append(0)
        else:
            precisions.append(precision_at_k(results, gold_standard, index + 1))
    return sum(precisions) / len(precisions)


def tokenize(string):
    from re import sub
    return sub('\W', ' ', string).lower().split()


for file in ['tf_idf_inverted_index.py'] + sorted(
        glob('tf_idf_inverted_index_*.py')):
    variant = file[len('tf_idf_inverted_index_'):-len('.py')].replace('_', '.')
    if not variant:
        variant = 'ntc.ntc'

    module_name = file[:-len('.py')]
    module = import_module(module_name)

    index = module.TfIdfInvertedIndex()
    for doc in iter_lisa_docs('lisa'):
        terms = tokenize(doc['title'] + ' ' + doc['abstract'])
        index.add_document(doc['id'], terms)
    index.calc_document_lengths()

    precisions_at_20 = []
    average_precisions = []
    for query in iter_lisa_queries('lisa'):
        terms = tokenize(query['query'])
        results = index.search(terms)

        results = [r[0] for r in results]
        gold_standard = query['relevant']
        precisions_at_20.append(precision_at_k(results, gold_standard, 20))
        average_precisions.append(average_precision(results, gold_standard))

    print('Variant "{}" defined in file "{}":'.format(variant, file))
    print('  mean precision@20:      {:.4f}'.format(
        sum(precisions_at_20) / len(precisions_at_20)))
    print('  mean average precision: {:.4f}'.format(
        sum(average_precisions) / len(average_precisions)))
