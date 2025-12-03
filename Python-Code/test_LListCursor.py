# ----------------------------------------------------------------------

# test_LListCursor.py
# Ben Herdman
# ----------------------------------------------------------------------

from typing import List, Any
import unittest

from LListCursor import LListCursor

# ----------------------------------------------------------------------


class LListTest(unittest.TestCase):

    def checkList(self, linked: LListCursor, lst: List, cursorValue: Any):
        self.assertEqual(len(linked), len(lst), f"length is not {len(lst)}")
        items = []
        for x in linked:
            items.append(x)
        self.assertEqual(items, lst)
        if len(lst) > 0:
            headItem = linked.itemAtHead()
            tailItem = linked.itemAtTail()
            cursorItem = linked.itemAtCursor()
            self.assertEqual(headItem, lst[0], f"head wrong: should be {lst[0]}, but is {headItem}")
            self.assertEqual(tailItem, lst[-1], f"tail wrong: should be {lst[-1]}, but is {tailItem}")
            self.assertEqual(cursorItem, cursorValue, f"cursor wrong: should be {cursorValue}, but is {cursorItem}")

    def testLen0vars(self):
        items = LListCursor()
        self.assertEqual(len(items), 0)

    def testLen1var(self):
        items = LListCursor(1)
        self.assertEqual(len(items), 1)

    def testLen2vars(self):
        items = LListCursor(1, 2)
        self.assertEqual(len(items), 2)

    def testLen3vars(self):
        items = LListCursor(1, 2, 3)
        self.assertEqual(len(items), 3)

    def testLen4vars(self):
        items = LListCursor(1, 2, 3, 4)
        self.assertEqual(len(items), 4)

    def testHead1(self):
        items = LListCursor(1)
        self.assertEqual(items._head.item, 1)

    def testHead2(self):
        items = LListCursor(1, 2)
        self.assertEqual(items._head.item, 1)

    def testHead3(self):
        items = LListCursor(1, 2, 3)
        self.assertEqual(items._head.item, 1)

    def testHead4(self):
        items = LListCursor(1, 2, 3, 4)
        self.assertEqual(items._head.item, 1)

    def testHead5(self):
        items = LListCursor()
        self.assertEqual(items._head, None)

    def testTail1(self):
        items = LListCursor(1)
        self.assertEqual(items._tail.item, 1)

    def testTail2(self):
        items = LListCursor(1, 2)
        self.assertEqual(items._tail.item, 2)

    def testTail3(self):
        items = LListCursor(1, 2, 3)
        self.assertEqual(items._tail.item, 3)

    def testTail4(self):
        items = LListCursor(1, 2, 3, 4)
        self.assertEqual(items._tail.item, 4)

    def testTail5(self):
        items = LListCursor()
        self.assertEqual(items._tail, None)

    def testList1(self):
        items = LListCursor()
        self.checkList(items, [], None)

    def testList2(self):
        items = LListCursor(1)
        self.checkList(items, [1, ], 1)

    def testList3(self):
        items = LListCursor(1, 2)
        self.checkList(items, [1, 2, ], 1)

    def testList4(self):
        items = LListCursor(1, 2, 3)
        self.checkList(items, [1, 2, 3, ], 1)

    def testInitInstanceVars1(self):
        items = LListCursor()
        self.assertEqual(items._length, 0)
        self.assertEqual(items._head, None)
        self.assertEqual(items._cursor, None)
        self.assertEqual(items._tail, None)

    def testInitInstanceVars2(self):
        items = LListCursor(1)
        self.assertEqual(items._length, 1)
        self.assertEqual(items._head.item, 1)
        self.assertEqual(items._cursor.item, 1)
        self.assertEqual(items._tail.item, 1)

    def testInitInstanceVars3(self):
        items = LListCursor(1, 2)
        self.assertEqual(items._length, 2)
        self.assertEqual(items._head.item, 1)
        self.assertEqual(items._cursor.item, 1)
        self.assertEqual(items._tail.item, 2)

    def testInitInstanceVars4(self):
        items = LListCursor(1, 2, 3)
        self.assertEqual(items._length, 3)
        self.assertEqual(items._head.item, 1)
        self.assertEqual(items._cursor.item, 1)
        self.assertEqual(items._tail.item, 3)

    def testInitInstanceVars5(self):
        items = LListCursor(1, 2, 3, 4)
        self.assertEqual(items._length, 4)
        self.assertEqual(items._head.item, 1)
        self.assertEqual(items._cursor.item, 1)
        self.assertEqual(items._tail.item, 4)

    def testRemoveAtTail1(self):
        items = LListCursor(1)
        items.removeItemAtTail()
        self.checkList(items, [], None)

    def testRemoveAtTail2(self):
        items = LListCursor(1, 2)
        items.removeItemAtTail()
        self.checkList(items, [1, ], 1)

    def testRemoveAtTail3(self):
        items = LListCursor(1, 2, 3)
        items.removeItemAtTail()
        self.checkList(items, [1, 2], 1)

    def testRemoveAtTail4(self):
        items = LListCursor(1, 2, 3, 4)
        items.removeItemAtTail()
        self.checkList(items, [1, 2, 3], 1)

    def testInsertAtHead1(self):
        items = LListCursor()
        items.insertAtHead(0)
        self.checkList(items, [0, ], 0)

    def testInsertAtHead2(self):
        items = LListCursor(1)
        items.insertAtHead(0)
        self.checkList(items, [0, 1, ], 1)

    def testInsertAtHead3(self):
        items = LListCursor(1, 2)
        items.insertAtHead(0)
        self.checkList(items, [0, 1, 2, ], 1)

    def testInsertAtHead4(self):
        items = LListCursor(1, 2, 3)
        items.insertAtHead(0)
        self.checkList(items, [0, 1, 2, 3, ], 1)

    def testInsertAtHead5(self):
        items = LListCursor(1, 2, 3, 4)
        items.insertAtHead(0)
        self.checkList(items, [0, 1, 2, 3, 4], 1)

    def testInsertAtHead(self):
        items = LListCursor()
        for i in range(3, -1, -1):
            items.insertAtHead(i)
        self.checkList(items, list(range(4)), 3)

    def testItemAtHeadRaisesIndexError(self):
        items = LListCursor()
        with self.assertRaises(IndexError):
            items.itemAtHead()

    def testCursorMovement1(self):
        items = LListCursor(1, 2, 3, 4, 5)
        self.assertEqual(items.cursorForward(), True)
        self.assertEqual(items._cursor.item, 2)

    def testCursorMovement2(self):
        items = LListCursor(1, 2, 3, 4, 5)
        self.assertEqual(items.cursorForward(), True)
        items.cursorForward()
        self.assertEqual(items._cursor.item, 3)

    def testCursorMovement3(self):
        items = LListCursor(1, 2, 3, 4, 5)
        self.assertEqual(items.cursorForward(), True)
        items.cursorForward()
        items.cursorForward()
        self.assertEqual(items._cursor.item, 4)

    def testCursorMovement4(self):
        items = LListCursor(1, 2, 3, 4, 5)
        self.assertEqual(items.cursorForward(), True)
        items.cursorForward()
        items.cursorForward()
        items.cursorForward()
        self.assertEqual(items._cursor.item, 5)

    def testRemoveAtTailWithCursor(self):
        items = LListCursor(1, 2, 3, 4, 5)
        items.cursorForward()
        items.cursorForward()
        items.cursorForward()
        items.cursorForward()
        self.assertEqual(items._cursor.item, 5)
        items.removeItemAtTail()
        self.checkList(items, [1, 2, 3, 4, ], 4)

    def testRemoveAtCursor1(self):
        items = LListCursor(1, 2, 3, 4, 5)
        items.cursorForward()
        items.removeItemAtCursor()
        self.assertEqual(items._cursor.item, 3)
        self.checkList(items, [1, 3, 4, 5], 3)

    def testRemoveAtCursor2(self):
        items = LListCursor(1, 2, 3, 4, 5)
        items.removeItemAtCursor()
        self.assertEqual(items._cursor.item, 2)
        self.checkList(items, [2, 3, 4, 5], 2)

    def testRemoveAtCursor3(self):
        items = LListCursor(1, 2, 3, 4, 5)
        items.cursorForward()
        items.cursorForward()
        items.removeItemAtCursor()
        self.assertEqual(items._cursor.item, 4)
        self.checkList(items, [1, 2, 4, 5], 4)

    def testRemoveAtCursor4(self):
        items = LListCursor(1, 2, 3, 4, 5)
        items.cursorForward()
        items.cursorForward()
        items.cursorForward()
        items.removeItemAtCursor()
        self.assertEqual(items._cursor.item, 5)
        self.checkList(items, [1, 2, 3, 5], 5)

    def testRemoveAtCursor5(self):
        items = LListCursor(1, 2, 3, 4, 5)
        items.cursorForward()
        items.cursorForward()
        items.cursorForward()
        items.cursorForward()
        items.removeItemAtCursor()
        self.assertEqual(items._cursor.item, 4)
        self.checkList(items, [1, 2, 3, 4, ], 4)

    def testListPlusList1(self):
        items1 = LListCursor(1, 2, 3)
        items2 = LListCursor(4, 5, 6)
        list1 = items1 + items2
        self.checkList(list1, [1, 2, 3, 4, 5, 6], 1)

    def testListPlusLis2(self):
        items1 = LListCursor(1, 2, 3, 4, 5)
        items2 = LListCursor(6, 7, 8, 9, 10)
        list1 = items1 + items2
        self.checkList(list1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)

    def testListPlusList3(self):
        items1 = LListCursor(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        items2 = LListCursor(11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
        list1 = items1 + items2
        self.checkList(list1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 1)

    def testListPlusList4(self):
        items1 = LListCursor(1)
        items2 = LListCursor(2)
        list1 = items1 + items2
        self.checkList(list1, [1, 2], 1)

    def testListPlusList5(self):
        items1 = LListCursor(1)
        items2 = LListCursor()
        list1 = items1 + items2
        self.checkList(list1, [1], 1)


# ----------------------------------------------------------------------


def main():
    unittest.main()

# ----------------------------------------------------------------------


if __name__ == '__main__':
    main()
#