import sys
sys.setrecursionlimit(150000)
class TreeNode(object):
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

def preorder(root, out):
	if root != None:
		out.append(root.val)
		preorder(root.left, out)
		preorder(root.right, out)
	return out

def postorder(root, out):
	if root != None:
		postorder(root.left, out)
		postorder(root.right, out)
		out.append(root.val)
	return out

T = int(sys.stdin.readline())

for X in xrange(1, T+1):
	N, K = map(int, sys.stdin.readline().strip().split())
	tree = []
	pre = []
	post = []
	for i in xrange(N):
		t = TreeNode(i+1)
		tree.append(t)
	for i in xrange(N):
		l, r = map(int, sys.stdin.readline().strip().split())
		if l != 0:
			tree[i].left = tree[l-1]
		if r != 0:
			tree[i].right = tree[r-1]

	preorder(tree[0], pre)
	postorder(tree[0], post)
	#print pre
	#print post
	buckets = []
	exit = 0
	for i in xrange(N):
		pre_bucket = post_bucket = -1
		for j in xrange(len(buckets)):
			if pre[i] in buckets[j]:
				pre_bucket = j
			if post[i] in buckets[j]:
				post_bucket = j
		if pre_bucket == post_bucket:
			if pre_bucket == -1:
				buckets.append([pre[i], post[i]])
		else:
			if post_bucket == -1:
				buckets[pre_bucket].append(post[i])
			elif pre_bucket == -1:
				buckets[post_bucket].append(pre[i])
			else:
				new_bucket = buckets[pre_bucket] + buckets[post_bucket]
				if pre_bucket < post_bucket:
					buckets.pop(pre_bucket)
					buckets.pop(post_bucket-1)
				else:
					buckets.pop(pre_bucket)
					buckets.pop(post_bucket)
				buckets.append(new_bucket)
	#print buckets
	if len(buckets) < K:
		print "Case #{}: Impossible".format(X)
		continue
	keys = {}
	for i in xrange(len(buckets)):
		for j in buckets[i]:
			keys[j] = i % K + 1
	out_str = ""
	for i in xrange(1, N+1):
		out_str += " " + str(keys[i])
	out_str = out_str.strip()
	print "Case #{}: {}".format(X, out_str)

