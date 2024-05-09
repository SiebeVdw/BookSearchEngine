"""
Group: 2
Names: Tiemen De Raedt, Siebe Vandewalle, Wolf De Waele

Template for Levenshtein distance methods. 
"""

def tail(s: str):
    return s[1:]
    """
    Extract tail of string.

    :param str s: Input string.
    :return str: Tail of s.
    """

def lev(a: str, b: str) -> int:
    if (len(a) == 0 or len(b) == 0):
        return max(len(a),len(b))
    elif (a[0] == b[0]):
        return lev(tail(a),tail(b))
    else:
        return 1 + min(lev(tail(a),b),lev(a,tail(b)),lev(tail(a),tail(b)))
    """
    Naive, recursive implementation of the Levenshtein distance.

    :param str a: First string.
    :param str b: Second string.
    :return int: Levenshtein distance between a and b.
    """

def lev_dp(a: str, b: str) -> int:
    m = len(a)
    n = len(b)
    dist = [[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dist[i][j] = j
            elif j == 0:
                dist[i][j] = i
            elif a[i-1] == b[j-1]:
                dist[i][j] = dist[i-1][j-1]
            else:
                dist[i][j] = 1 + min(dist[i][j-1],dist[i-1][j],dist[i-1][j-1])
    return dist[m][n]

    """
    Dynamic programming implementation of the Levenshtein distance.

    :param str a: First string.
    :param str b: Second string.
    :return int: Levenshtrein distance between a and b.
    """