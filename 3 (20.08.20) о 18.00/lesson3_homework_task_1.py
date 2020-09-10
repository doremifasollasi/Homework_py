# Record Python's philosophy in a tape.
zen_python = """
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# Find the number of occurrences of words (better, never, is) in the given tape.
quantity_better = zen_python.count("better")
quantity_never = zen_python.count("never")
quantity_is = zen_python.count("is")
#print("Quantity word 'better':", quantity_better)
#print("Quantity word 'never':", quantity_never)
#print("Quantity word 'is':", quantity_never)

# Print all uppercase text (all uppercase letters).
upper_zen_pyton = zen_python.upper()
#print("This text is in uppercase:", upper_zen_pyton)

# Replace all occurrences of the "and" character with "&".
replase_zen_python = zen_python.replace("i","&")
#print("Replaced in this text from 'i' to '&':", replase_zen_python)