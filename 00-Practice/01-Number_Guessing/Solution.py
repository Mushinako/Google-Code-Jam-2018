def fprint(*args, **kwargs):
    print(*args, flush=True, **kwargs)

def do_test_case():
    a, b = [int(s) for s in input().split(' ')]
    n = int(input())

    while True:
        k = (a + b + 1) // 2
        if k <= a:
            k += 1
            if k > b:
                raise ValueError('No candidate left!')
        elif k > b:
            k -= 1
            if k <= a:
                raise ValueError('No candidate left!')

        fprint(k, flush=True)

        # Analyze feedback
        f = input()
        if f == "CORRECT":
            return True
        elif f == "WRONG_ANSWER":
            return False
        elif f == "TOO_BIG":
            b = k - 1
        elif f == "TOO_SMALL":
            a = k
        else:
            raise ValueError(f + '. Feedback not expected!')

t = int(input())

while t > 0:
    r = do_test_case()
    assert r
    t -= 1
