from dsapy.libs.queue.queue import QueueList


class TestQueue:
    def test_is_empty(self):
        queue = QueueList()
        assert queue.is_empty

    def test_enqueue(self):
        queue = QueueList()
        queue.enqueue(1)

        assert queue.is_empty is False
        assert str(queue) == "[1]"
