from linked_list import SingleLinkedList
import unittest

def return_kth_to_last(obj, k):
    if obj.size == 0 or k <= 0 or obj.size < k:
        return None 
    
    slow = obj.head 
    fast = obj.head
    
    for _ in range(k):
        if fast is None:
            return None
        
        fast = fast.next 
    
    while fast:
        slow = slow.next 
        fast = fast.next 
        
    return slow.value


class Test(unittest.TestCase):
    def test_true(self):
        obj = SingleLinkedList()
        values = list(range(1, 11))
        
        for v in values:
            obj.add(v)
            
        self.assertEqual(return_kth_to_last(obj, 1), 10)
        self.assertEqual(return_kth_to_last(obj, 3), 8)
        
    def test_false(self):
        obj = SingleLinkedList() 
        obj.generate(10, 1, 100)
        
        self.assertIsNone(return_kth_to_last(obj, 11))
        self.assertNotEqual(return_kth_to_last(obj, 2), 200)
        
    def test_empty_list(self):
        obj = SingleLinkedList()
        self.assertIsNone(return_kth_to_last(obj, 1))
        
    def test_k_less_equal_zero(self):
        obj = SingleLinkedList()
        obj.generate(5, 1, 10)
        
        self.assertIsNone(return_kth_to_last(obj, 0))
        self.assertIsNone(return_kth_to_last(obj, -3))


if __name__ == "__main__":
    unittest.main()