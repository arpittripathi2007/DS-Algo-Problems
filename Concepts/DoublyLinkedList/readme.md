

# LINKED LIST
===================

Linked list is often compared to arrays. Whereas an array is a fixed size of sequence, a linked list can have its elements to be dynamically allocated. 
What are the pros and cons of these characteristics? Here are some major ones:
## Advantages
* A linked list saves memory. It only allocates the memory required for values to be stored. In arrays, you have to set an array size before filling it with values, which can potentially waste memory.
* Linked list nodes can live anywhere in the memory. Whereas an array requires a sequence of memory to be initiated, as long as the references are updated, each linked list node can be flexibly moved to a different address.

## Disadvantages
Linear look up time. When looking for a value in a linked list, you have to start from the beginning of chain, and check one element at a time for a value you’re looking for. If the linked list is n elements long, this can take up to n time. On the contrary many languages allow constant lookups in arrays.


## Operations

### Traverse

### Insert
* Insert At Begining
* Insert At End
* Insert By Value
    * Insert after the Node 
    * Insert before the Node 

### Delete
* Delete At Begining
* Delete At End
* Delete By Value