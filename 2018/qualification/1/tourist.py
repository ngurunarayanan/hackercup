import sys

T = int(sys.stdin.readline().strip())

for X in xrange(1, T+1):
	N, K, V = map(int, sys.stdin.readline().strip().split())
	attractions = []
	out_str = ""
	for i in xrange(N):
		istr = sys.stdin.readline().strip()
		attractions.append(istr)
	start = ((V-1)*K) % N
	out_ids = []
	for i in xrange(K):
		out_ids.append((start + i) % N)
	out_ids.sort()
	for i in out_ids:
		out_str += " " + attractions[i]
	out_str = out_str.strip()
	print "Case #{}: {}".format(X, out_str)
#	print attractions, out_ids
