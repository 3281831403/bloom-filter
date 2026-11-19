"""布隆过滤器：哈希、误判率与并集：待实现的核心模块。"""


def hashes(key, count, size):
    """生成多个位图下标。"""
    raise NotImplementedError

def add(bits, key, count):
    """加入元素。"""
    raise NotImplementedError

def contains(bits, key, count):
    """检查元素。"""
    raise NotImplementedError

def false_positive_rate(n, m, k):
    """误判率。"""
    raise NotImplementedError

def union(a, b):
    """并集。"""
    raise NotImplementedError
