class Solution(object):
    def findTarget(self, root, k):
        self.a = set()
        self.found = False
        self.dfs(root, k)
        return self.found

    def dfs(self, root, k):
        if not root:
            return
        if root.val not in self.a:
            self.a.add(k - root.val)
        else:
            self.found = True
        self.dfs(root.left, k)
        self.dfs(root.right, k)


def main():
    try:
        s = Solution()
        answer = s.twoSumII([2, 7, 11, 15], 9)
    except Exception as e:
        exit(1)

if __name__ == '__main__':
    main()
