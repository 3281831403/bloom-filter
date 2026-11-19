# 布隆过滤器：哈希、误判率与并集

误报率比预期高一个数量级：哈希没有加盐，add 没有把所有位图位置置位，contains 漏检任意一位，误判率公式用错，并集按长度截断而不是逐位或，空过滤器崩，批量插入只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
probabilistic/__init__.py
probabilistic/bloom.py
tests/test_bloom.py
```

## 当前状态

`probabilistic/bloom.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_bloom.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 哈希加盐分散
2. add 全位置置位
3. contains 全位置检查
4. 误判率公式
5. 并集逐位或
6. 空过滤器兜底

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `probabilistic/bloom.py`
后 15 条用例应全部通过。
