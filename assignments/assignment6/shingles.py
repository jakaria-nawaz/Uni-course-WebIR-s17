#!/usr/bin/env python3
# ===========================================================
#                     Group - Gamma                         =
# ===========================================================
# Mohammad Nizam Uddin                                      =
# Md. Shohel Ahamad                                         =
# MD Jakaria Nawaz                                          =
# Shreya Chatterjee                                         =
# ===========================================================

class ShinglesOperation:

    def doc_shingles_similarity(self, doc_item_list_1, doc_item_list_2, shingle_n):
        if shingle_n == 1:
            similarity_result = self.jaccard_of_shingles_set(set(doc_item_list_1), set(doc_item_list_2))
        elif shingle_n == 2:
            doc_item_list_1_n2_list = []
            doc_item_list_2_n2_list = []
            n = 0
            for each_item in doc_item_list_1:
                if n<(len(doc_item_list_1)-1):
                    n2_item = each_item+' '+doc_item_list_1[n+1]
                    doc_item_list_1_n2_list.append(n2_item)
                    n = n+1
            n = 0
            for each_item in doc_item_list_2:
                if n<(len(doc_item_list_2)-1):
                    n2_item = each_item+' '+doc_item_list_2[n+1]
                    doc_item_list_2_n2_list.append(n2_item)
                    n = n+1
            similarity_result = self.jaccard_of_shingles_set(set(doc_item_list_1_n2_list), set(doc_item_list_2_n2_list))
        elif shingle_n == 3:
            doc_item_list_1_n3_list = []
            doc_item_list_2_n3_list = []
            n = 0
            for each_item in doc_item_list_1:
                if n<(len(doc_item_list_1)-2):
                    n2_item = each_item+' '+doc_item_list_1[n+1]+' '+doc_item_list_1[n+2]
                    doc_item_list_1_n3_list.append(n2_item)
                    n = n+1
            n = 0
            for each_item in doc_item_list_2:
                if n<(len(doc_item_list_2)-2):
                    n2_item = each_item+' '+doc_item_list_2[n+1]+' '+doc_item_list_2[n+2]
                    doc_item_list_2_n3_list.append(n2_item)
                    n = n+1
            similarity_result = self.jaccard_of_shingles_set(set(doc_item_list_1_n3_list), set(doc_item_list_2_n3_list))
        return similarity_result

    def jaccard_of_shingles_set(self, shingle_set_1, shingle_set_2):
        return (len(shingle_set_1.intersection(shingle_set_2))/len(shingle_set_1.union(shingle_set_2)))

if __name__ == '__main__':
    shingle_ob  = ShinglesOperation()

    doc_A_1   = 'a bump on the log in the hole in the bottom of the sea'
    doc_A_1   = doc_A_1.split()
    doc_A_2   = 'a frog on the bump on the log in the hole in the bottom of the sea'
    doc_A_2   = doc_A_2.split()

    doc_B_1   = 'your mother drives you in the car'
    doc_B_1   = doc_B_1.split()
    doc_B_2   = 'in mother russia car drives you'
    doc_B_2   = doc_B_2.split()

    docs_A_for_n1 = shingle_ob.doc_shingles_similarity(doc_A_1, doc_A_2, 1)
    docs_A_for_n2 = shingle_ob.doc_shingles_similarity(doc_A_1, doc_A_2, 2)
    docs_A_for_n3 = shingle_ob.doc_shingles_similarity(doc_A_1, doc_A_2, 3)

    print('similarity of doc_A_1 and doc_A_2 respectively for n=1, n=2, n=3: ',docs_A_for_n1, ', ',docs_A_for_n2,', ',docs_A_for_n3)

    docs_B_for_n1 = shingle_ob.doc_shingles_similarity(doc_B_1, doc_B_2, 1)
    docs_B_for_n2 = shingle_ob.doc_shingles_similarity(doc_B_1, doc_B_2, 2)
    docs_B_for_n3 = shingle_ob.doc_shingles_similarity(doc_B_1, doc_B_2, 3)

    print('similarity of doc_B_1 and doc_B_2 respectively for n=1, n=2, n=3: ',docs_B_for_n1, ', ',docs_B_for_n2,', ',docs_B_for_n3)
