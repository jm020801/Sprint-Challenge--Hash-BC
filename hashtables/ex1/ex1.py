#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)


    for index, item in enumerate(weights, start=0):   # default is zero
        hash_table_insert(ht, item, index)

        # print(hash_table_retrieve(ht, item))

    for i in weights:
        # print(i)
        first_index = hash_table_retrieve(ht, i)
        print(f'first index is {first_index}')
        if hash_table_retrieve(ht, limit - i):
            second_index = hash_table_retrieve(ht, limit - i)
            pair = [max(first_index, second_index), min(first_index,second_index)]
            print(f'the pair is {pair}')
            return (pair)
        # else:

    print('no pair exists')
    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)
