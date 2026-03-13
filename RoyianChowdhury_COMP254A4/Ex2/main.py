from StackArray import ArrayStack


def transfer(S,T):
    while S.size() != 0:
        #as long as S is not 0
        T.push(S.pop())
        #push into t what is being taken out of s
    return T


if __name__ == "__main__":
    sStack = ArrayStack()
    tStack = ArrayStack()
    sStack.push(1)
    sStack.push(2)
    sStack.push(3)
    sStack.push(4)
    print(sStack)
    print(transfer(sStack,tStack))
    pass