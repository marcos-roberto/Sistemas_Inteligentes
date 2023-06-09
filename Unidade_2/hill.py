def goal(x):
	return x*x*(x-1)*(x-2)*(x-3)*(x-4)


class State:
    def __init__(self, x):
        self.x = x
        self.f = goal(x)


def succ(s):
    x1 = s.x + 0.0001
    neighboor1 = State(x1)
    x2 = s.x - 0.0001
    neighboor2 = State(x2)

    if(neighboor1.f < neighboor2.f):
        return neighboor1
    return neighboor2

def initialState():
    return State(1)

current = initialState()
while True:
    neighboor = succ(current)
    if(neighboor.f >= current.f):
        break
    current = neighboor


print('x = ', current.x, 'f = ', current.f)
