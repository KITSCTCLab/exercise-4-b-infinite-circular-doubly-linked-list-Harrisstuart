# Read an integer that denotes the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))
# Write your code here
lst=[]
val=0
while len(lst)<length_of_circular_linked_list and val<len(circular_linked_list):
  element = circular_linked_list[val]
  if element not in lst:
    lst.append(element)
  val+=1
print(len(lst))
print(" ".join(str(num)for num in lst))

