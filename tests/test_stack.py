def test_stack1():
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'

def test_stack2():
    stack = []
    stack.append('one')
    stack.append('two')

    stack.pop()
    assert stack.pop() == 'one'
