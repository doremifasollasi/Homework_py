def count_sheeps(sheep):
    """A function that counts the number of sheep present in the array (true means present)."""
    count = 0
    for s in sheep:
      if s:
          count += 1 
    return count

    # return sheep.count(True)
    
    # return len([x for x in sheep if x])
