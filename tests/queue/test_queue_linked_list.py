from dsapy.libs.queue.queue import QueueLinkedList


class Test:
    def test_is_empty(self):
        queue = QueueLinkedList()
        assert queue.is_empty

    def test_enqueue(self):
        queue = QueueLinkedList()
        queue.enqueue(1)

        assert queue.is_empty is False
        assert str(queue) == "[1]"
        assert str(queue) == "[1]"

    def test_dequeue(self):
        queue = QueueLinkedList[str]()
        queue.enqueue("Bryan")
        queue.enqueue("Tom")
        queue.enqueue("David")

        assert queue.dequeue() == "Bryan"
        assert str(queue) == "[Tom, David]"
