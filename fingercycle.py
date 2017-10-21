# solution to hand cycle problem presented by Juan

# n number of steps, t fingers
def formula(n, t):
    if n < 1: return n # before start of hand ..
    n, t = n - 1, t - 1
    return (n%t if n%(2*t) < t else t-n%t) + 1

if __name__ == '__main__':
    # test 50 steps with 5 fingers
    for n in range(50):
        print(formula(n, 5))
