def Hanoi02(n, src, dest, other):
	if n == 0:
		return

	Hanoi02(n-1, src, dest, other)
	print("Move disk", n, "from peg", src, "to peg", other)
	Hanoi02(n-1, dest, src, other)
	print("Move disk", n, "from peg", other, "to peg", dest)
	Hanoi02(n-1, src, dest, other)

#test call
n = 3
Hanoi02(n, 1, 3, 2)
print("\nsolved.\n")
