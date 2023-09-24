test_str = "TamalBarman"
res = {i : test_str.count(i) for i in set(test_str)}
print ("The count of all characters in TamalBarman is :\n "+  str(res))