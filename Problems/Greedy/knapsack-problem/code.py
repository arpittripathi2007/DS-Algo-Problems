class itemDS:
  def __init__(self, value, weight):
    self.value = value
    self.weight = weight

def fractionalknapsack(W,Items,n):    
    # code here
    Items.sort(key = lambda x: (x.value/x.weight), reverse=True)
    weight_remaining = W
    total_values = 0
    for item in Items:
      if(item.weight<= weight_remaining):
        weight_remaining -= item.weight
        total_values += item.value
      else:
        total_values += (item.value/item.weight)* weight_remaining
        weight_remaining = 0
    return total_values

if __name__ == "__main__":
    items_input = [(17, 21), (93, 26), (29, 40), (26, 41), (37, 11), (19, 44), (38, 29), (83, 22), (11, 6), (89, 26), (16, 21), (38, 4), (9, 23), (84, 1), (58, 48)]
    item_ds = []
    for item in items_input:
      item_ds.append(itemDS(item[0], item[1]))
      
    print('1st soln:', fractionalknapsack(77, item_ds, 15))

