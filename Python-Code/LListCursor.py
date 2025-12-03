#!/usr/bin/env python3

# ----------------------------------------------------------------------
# LListCursor.py
# Ben Herdman
# ----------------------------------------------------------------------


from __future__ import annotations
from typing import Optional, Any

from ListNode import ListNode


# ----------------------------------------------------------------------


class LListCursor:
    """LListCursor is a linked list where you can add/remove/access
    items at beginning, end, and a _cursor position in the list

    class invariant:

        1. if the list is empty, self._head, self._cursor, self._tail are
        all None

        2. if the list is not empty, self._head, self._cursor, and
        self._tail all point to an appropriate ListNode; self._head
        points to the first ListNode; self._tail points to the last
        ListNode; self._cursor points to a ListNode in the list

        3. inserting an item should not change self._cursor unless the
        list was empty, in which case self._cursor points to the one
        item in the list

        4. when deleting at the _head or _tail, self._cursor stays where
        it is unless it was at the _head or _tail; if _cursor was at the
        _head and the _head was deleted, self._cursor now refers to the
        ListNode after it. if self._cursor was at the _tail and the _tail
        is deleted, self._cursor now refers to the ListNode before it

        5. when deleting the item at the _cursor, self._cursor now
        refers to the ListNode after it, unless there is no ListNode
        after it in which case it refers to the ListNode before it.

        6. self._length indicates the number of items in the LListCursor
        """

    # ------------------------------------------------------------------

    def __init__(self, *args):
        """
        initializes empty list or list with items in args if it is not None; the _cursor
        will be the first node
        :param args: sequence of items to insert into the list
        """
        self._head: Optional[ListNode] = None
        self._cursor: Optional[ListNode] = None
        self._tail: Optional[ListNode] = None
        self._length: int = 0
        # if only one argument, see if it is iterable
        if len(args) == 1:
            try:
                # try to insert each item
                for x in args[0]:
                    self.insertAtTail(x)
            except TypeError:
                # exception raised if item not iterable so just insert it
                self.insertAtTail(args[0])
        else:
            # 0 or 2 or more arguments so iterate over them and insert them
            for x in args:
                self.insertAtTail(x)
        self.cursorToStart()

    def __len__(self) -> int:
        """
        :return: number of items in the list
        """
        return self._length

    def __iter__(self):
        """
        iterates over items in list yielding one item at a time
        """
        # start at beginning of list
        node = self._head
        # while nodes left
        while node is not None:
            # yield item
            yield node.item
            # and move node forward
            node = node.link

    def __add__(self, other: LListCursor) -> LListCursor:
        """
        returns a new LListCursor that is the concatenation of self and other
        :param other: another LListCursor to concatenate with self
        :return: a new LListCursor that is concatenation of self and other; the
        _cursor of it should be at the beginning of the list
        """
        # make a new LList
        newList = LListCursor()

        # append the objects from the first list
        for x in self:
            newList.insertAtTail(x)

        # append the objects from the second list
        for x in other:
            newList.insertAtTail(x)

        # point the cursor to the head of the new list and return it
        newList._cursor = newList._head
        return newList

    # ------------------------------------------------------------------

    def insertAtHead(self, item: Any) -> None:
        """
        inserts item at the beginning of the list
        :param item: value to insert
        :return: None
        """
        # if length is 0 then the list is empty
        if self._length == 0:
            # insert in the item and point everything to the head
            self._head = ListNode(item)
            self._tail = self._head
            self._cursor = self._head

        else:
            # create a "temp" var to store the old head
            prevHead = self._head
            # create the new head
            self._head = ListNode(item)
            # link the old head to the new head
            self._head.link = prevHead

        self._length += 1

    def insertAfterCursor(self, item: Any) -> None:
        """
        insert item after the _cursor position
        :param item: value to insert
        :return: None
        """
        if self._cursor == self._tail:
            self.insertAtTail(item)
        else:
            self._length += 1
            # list is not empty since _cursor == _tail if it is and _cursor not at _tail
            # create node
            node = ListNode(item, self._cursor.link)
            # connect _cursor to the new node
            self._cursor.link = node

    def insertAtTail(self, item: Any) -> None:
        """
        insert item at the end of the list
        :param item: value to insert
        :return: None
        """
        # if the length is zero the list is empty
        if self._length == 0:
            # create the head and point all other vars to it
            self._head = ListNode(item)
            self._tail = self._head
            self._cursor = self._head

        else:
            # list is not empty, create the tail and link it to the structure
            self._tail.link = ListNode(item)
            self._tail = self._tail.link

        self._length += 1

    def removeItemAtHead(self) -> Any:
        """
        removes first item in the list; IndexError is raised if list is empty
        :return: the item that was removed
        """
        if self._length == 0:
            # raise IndexError if list is empty
            raise IndexError('removeItemAtHead called on empty LListCursor')
        else:
            self._length -= 1
            # get item so can return it later
            item = self._head.item
            # if list is empty after the deletion
            if self._length == 0:
                # make all ListNode instance vars None
                self._head = self._cursor = self._tail = None
            else:
                # if _cursor was at _head
                if self._cursor == self._head:
                    # move _cursor forward to new first item
                    self._cursor = self._cursor.link
                # move _head forward to new first item
                self._head = self._head.link

            return item

    def removeItemAtCursor(self) -> Any:
        """
        removes item in the list that is at the _cursor; IndexError is raised if list is empty;
        the _cursor now points to the node after the original _cursor unless the _cursor was the
        last item in which case the _cursor is now the new last item
        :return: the item that was removed
        """

        # Raise exception if length is zero
        if self._length == 0:
            raise IndexError('removeItemAtCursor called on empty LListCursor')

        # if the cursor is at the tail call the tail function
        elif self._cursor == self._tail:
            item = self.removeItemAtTail()

        # if the cursor is at the head call the head function
        elif self._cursor == self._head:
            item = self.removeItemAtHead()

        else:
            # otherwise decrement the length
            self._length -= 1
            # save the item for return
            item = self._cursor.item

            # if the length is zero after decrement destroy the list
            if self._length == 0:
                self._head = self._tail = self._cursor = None

            # if deleting one of two items, destroy the list and leave the head
            elif self._length == 1:
                self._head.link = None
                self._cursor = self._tail = self._head
                return item

            else:
                # create variables to call out of conditionals
                tracker = self._head
                nodeLinkToDestroy = tracker
                # go forwards through links
                while not (tracker == self._cursor):
                    # make a copy of the previous node
                    nodeLinkToDestroy = tracker
                    # move the tracker forward
                    tracker = tracker.link

                # move the cursor forward as per the conditions of Invariant
                properCursorLocation = self._cursor.link

                # destroy the prevNode's link
                nodeLinkToDestroy.link = None
                # relink the list
                nodeLinkToDestroy.link = properCursorLocation
                # set the cursor to the proper node
                self._cursor = properCursorLocation

        return item

    def removeItemAtTail(self) -> Any:
        """
        removes last item in the list; IndexError is raised if list is empty
        :return: the item that was removed
        """

        # list is empty, throw error to crash gracefully
        if self._length == 0:
            raise IndexError('removeItemAtTail called on empty LListCursor')

        else:
            # create proper length since we are removing an item
            self._length -= 1
            # save the item for return
            item = self._tail.item

            # if deleting the last item destroy the list
            if self._length == 0:
                self._head = self._cursor = self._tail = None
                return item

            # if deleting one of two items, destroy the list and leave the head
            elif self._length == 1:
                self._head.link = None
                self._cursor = self._tail = self._head
                return item

            else:
                # create variables to call out of conditionals
                tracker = self._head
                prevNode = tracker
                count = 0
                flagOnCursor = False
                # if the cursor is at the end, send it to the start
                if self._cursor == self._tail:
                    self.cursorToStart()
                    # flag that the cursor needs moved
                    flagOnCursor = True

                # go forwards through links
                while tracker != self._tail:
                    # make a copy of the previous node
                    prevNode = tracker
                    # move the tracker forward
                    tracker = tracker.link
                    # keep track of how many links there are to move the cursor if needed
                    count += 1

        # if the cursor was flagged for being at the end of the list
        if flagOnCursor:
            for i in range(count):
                # move the cursor forward based on count variable
                self.cursorForward()

        # destroy the prevNode's link
        prevNode.link = None
        # set the tail to the unlinked node
        self._tail = prevNode
        if flagOnCursor:
            self._cursor = self._tail
        # return the item
        return item

    def itemAtHead(self) -> Any:
        """
        returns first item; IndexError is raised if list is empty
        :return: first item in list
        """
        # Raise exception if length is zero, otherwise return item
        if self._length == 0:
            raise IndexError('itemAtHead called on empty LListCursor')

        return self._head.item

    def itemAtCursor(self) -> Any:
        """
        returns item at _cursor; IndexError is raised if list is empty
        :return: item at _cursor
        """
        # Raise exception if length is zero, otherwise return item
        if self._length == 0:
            raise IndexError('itemAtCursor called on empty LListCursor')

        return self._cursor.item

    def itemAtTail(self) -> Any:
        """
        returns list item; IndexError is raised if list is empty
        :return: first last in list
        """

        if self._length == 0:
            raise IndexError('itemAtTail called on empty LListCursor')

        return self._tail.item

    def cursorToStart(self) -> None:
        """
        move _cursor to start/_head of list
        :return:
        """
        # sends the cursor to the head to re-iterate
        self._cursor = self._head

    def cursorForward(self) -> bool:
        """
        move _cursor forward one item
        :return: True if _cursor was moved forward or False if list empty or _cursor already at end of list
        """
        # set the cursor move check to false as it hasn't been updated
        # if the length is zero the list is empty
        if self._length == 0:
            didCursorMove = False

        # if the cursor isn't at the tail move the cursor forward
        elif self._cursor != self._tail:
            self._cursor = self._cursor.link
            didCursorMove = True

        # meant to handle if the cursor is at the tail, but acts as catch for other edge incidents
        else:
            didCursorMove = False

        return didCursorMove
# ----------------------------------------------------------------------