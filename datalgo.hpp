#ifndef datalgo_H
#define datalgo_H

/////////////////////DATA STRUCTURES///////////////////////////
class SinglyLinkedList
{
  struct Node
  {
    int val;
    Node* next;
  };

  Node* head;

public:
  SinglyLinkedList();
  SinglyLinkedList(int val);
  void insertHead(int val);
  void insertTail(int val);
  void find(int val);
  void deleteNode(int val);
  void deleteNode();
  void display();
  ~SinglyLinkedList();
};

class DoublyLinkedList
{
  struct Node
  {
    int val;
    Node* prev;
    Node* next;
  };

  Node* head;

public:
  DoublyLinkedList();
  DoublyLinkedList(int val);
  void display();
  void reverse();
  void testDoubleLinks();
  void insertHead(int val);
  void insertTail(int val);
  void find(int val);
  void deleteNode(int val);
  void deleteNode();
  ~DoublyLinkedList();
};

#endif
