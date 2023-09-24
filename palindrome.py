def isPalindrome(s):
	return s == s[::-1]
s = "SNS"
ans = isPalindrome(s)
if ans:
	print("Yes")
else:
	print("No")