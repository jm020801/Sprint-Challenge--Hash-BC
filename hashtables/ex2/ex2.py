#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for i in tickets:
        # print(f'source is {i.source}, destination is {i.destination}')
        hash_table_insert(hashtable, i.source, i.destination)

    start = hash_table_retrieve(hashtable, 'NONE')
    # print(start)

    route = [start]
    current = start

    while len(route) < length:
        next = hash_table_retrieve(hashtable, current)
        route.append(next)
        current = next

    # print(route)
    
    return route

