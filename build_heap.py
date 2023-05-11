def build_heap(data):
    swaps = []
    n = len(data)
    # iterate over all non-leaf nodes
    for i in range(n // 2, -1, -1):
        # heapify the node
        swaps += heapify(data, i, n)
    return swaps

def heapify(data, i, n):
    """
    heapify node at index i in data of size n
    returns a list of swaps made during heapify
    """
    swaps = []
    # index of left child
    l = 2 * i + 1
    # index of right child
    r = 2 * i + 2
    # find the smallest element among node and its children
    smallest = i
    if l < n and data[l] < data[smallest]:
        smallest = l
    if r < n and data[r] < data[smallest]:
        smallest = r
    # swap node with smallest child if necessary
    if smallest != i:
        swaps.append((i, smallest))
        data[i], data[smallest] = data[smallest], data[i]
        # heapify the child
        swaps += heapify(data, smallest, n)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
