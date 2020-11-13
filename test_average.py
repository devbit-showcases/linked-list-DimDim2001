from average import average
from sllist import SingleLinkedList

def test_average():
    list = SingleLinkedList().append(1).append(2).append(3).append(4)
    assert average(list) == 2.5
    list2 = SingleLinkedList().prepend(5).prepend(10).prepend(50).prepend(100).prepend(500)
    assert average(list2) == 133.0
    assert average(list.join(list2))