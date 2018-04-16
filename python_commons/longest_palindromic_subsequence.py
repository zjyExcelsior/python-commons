# coding=utf-8
"""longest palindromic subsequence: manacher算法"""


def manacher(s):
    # 预处理
    s = '#' + '#'.join(s) + '#'

    rl = [0] * len(s)
    max_right = 0
    pos = 0
    max_len = 0
    for i in xrange(len(s)):
        # 2*pos-i 是i关于pos的对称点j(j=pos-(i-pos))
        rl[i] = min(rl[2 * pos - i], max_right - i) if i < max_right else 1
        # 尝试扩展，注意处理边界
        while i - rl[i] >= 0 and i + rl[i] < len(
                s) and s[i - rl[i]] == s[i + rl[i]]:
            rl[i] += 1
        # 更新max_right, pos
        if rl[i] + i - 1 > max_right:
            max_right = rl[i] + i - 1
            pos = i
        # 更新max_len
        max_len = max(max_len, rl[i])
    return max_len - 1


if __name__ == '__main__':
    assert 3 == manacher('aba')
    assert 12 == manacher('tattarrattat')
