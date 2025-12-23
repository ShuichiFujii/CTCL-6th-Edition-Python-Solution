from linked_list import SingleLinkedList
import unittest


class TestSingleLinkedList(unittest.TestCase):
    def test_new_list_is_empty(self):
        sll = SingleLinkedList()
        self.assertEqual(len(sll), 0)
        self.assertIsNone(sll.head)
        self.assertIsNone(sll.tail)
        
    def test_add_single_element(self):
        sll = SingleLinkedList()
        sll.add(10)
        self.assertEqual(len(sll), 1)
        self.assertIsNotNone(sll.head)
        self.assertIsNotNone(sll.tail)
        self.assertEqual(sll.head.value, 10)
        self.assertEqual(sll.tail.value, 10)
        
    def test_add_multiple_elements(self):
        sll = SingleLinkedList()
        values = [1, 2, 3, 4, 5]
        for v in values:
            sll.add(v)
        
        self.assertEqual(len(sll), len(values))
        
        curr = sll.head
        for v in values:
            self.assertIsNotNone(curr)
            self.assertEqual(curr.value, v)
            curr = curr.next
        
        self.assertIsNone(curr)
        
    def test_representation(self):
        sll = SingleLinkedList()
        values = [1, 2, 3]
        sll.add_multiple(values)
        self.assertEqual(str(sll), "Node(1) -> Node(2) -> Node(3)")
        
    def test_generate(self):
        sll = SingleLinkedList()
        sll.generate(5, 10, 20)
        self.assertEqual(len(sll), 5)
        for node in sll:
            self.assertGreaterEqual(node.value, 10)
            self.assertLessEqual(node.value, 20)  
    
    
    
if __name__ == "__main__":
    unittest.main()