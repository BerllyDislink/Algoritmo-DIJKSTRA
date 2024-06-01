# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 2, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print ("The created heap is : ",(list(li)))
