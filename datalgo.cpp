#include "datalgo.hpp"
#include <iostream>

using namespace std;

/////////////////////DATA STRUCTURES///////////////////////////
SinglyLinkedList::SinglyLinkedList()
{
  head = NULL;
}

SinglyLinkedList::SinglyLinkedList(int val)
{
  Node* node = new Node;
  node->val = val;
  head = node;
  head->next = NULL;
}

void SinglyLinkedList::insertHead(int val)
{
  Node* node = new Node;
  node->val = val;
  node->next = head;
  head = node;
}

void SinglyLinkedList::insertTail(int val)
{
  Node* node = new Node;
  node->val = val;
  node->next = NULL;

  if(head)
  {
    Node* next = head;
    while(next->next)
      next = next->next;
    next->next = node;
  }
  else
  {
    head = node;
  }
}

void SinglyLinkedList::find(int val)
{
  Node* next = head;

  while(next)
  {
    if(next->val == val)
      return;

    next = next->next;
  }
}

void SinglyLinkedList::display()
{
  Node* next = head;

  while(next)
  {
    cout << next->val << " ";
    next = next->next;
  }

  cout << "END" << endl;
}

void SinglyLinkedList::deleteNode()
{
  Node* temp = head->next;
  delete head;
  head = temp;
}

void SinglyLinkedList::deleteNode(int val)
{
  Node* prev = NULL;
  Node* curr = head;

  while(curr)
  {
    if(curr->val == val)
    {
      if(!prev)
      {
        delete head;
        head = NULL;
      }
      else
      {
        prev->next = curr->next;
        delete curr;
      }

      return;
    }
    prev = curr;
    curr = curr->next;
  }
}

SinglyLinkedList::~SinglyLinkedList()
{
  Node* next = head;

  while(next)
  {
    Node* current = next;
    next = next->next;
    delete current;
  }
}


DoublyLinkedList::DoublyLinkedList()
{
  head = NULL;
}

DoublyLinkedList::DoublyLinkedList(int val)
{
  Node* node = new Node;
  node->val = val;
  node->prev = NULL;
  node->next = NULL;
  head = node;
}

void DoublyLinkedList::display()
{
  Node* curr = head;

  while(curr)
  {
    cout << curr->val << " ";
    curr = curr->next;
  }

  cout << "END" << endl;
}

void DoublyLinkedList::insertHead(int val)
{
  Node* node = new Node;
  node->val = val;

  if(head)
  {
    head->prev = node;
    node->next = head;
    head = node;
  }
  else
  {
    node->prev = NULL;
    node->next = NULL;
    head = node;
  }
}

void DoublyLinkedList::insertTail(int val)
{
  Node* node = new Node;
  node->val = val;

  if(head)
  {
    Node* curr = head;

    while(curr->next)
      curr = curr->next;
    curr->next = node;
    node->prev = curr;
    node->next = NULL;
  }
  else
  {
    node->prev = NULL;
    node->next = NULL;
    head = node;
  }
}

void DoublyLinkedList::find(int val)
{
  Node* curr = head;

  while(curr)
  {
    if(curr->val == val)
    {
      cout << "Found value: " << val <<  endl;
      return;
    }
    curr = curr->next;
  }

  cout << "Value not found." << endl;
}

void DoublyLinkedList::testDoubleLinks()
{
  Node* curr = head;

  while(curr->next)
  {
    cout << curr->val << " ";
    curr = curr->next;
  }

  cout << curr->val << " ";

  while(curr)
  {
    cout << curr->val << " ";
    curr = curr->prev;
  }

  cout << endl;
}

void DoublyLinkedList::deleteNode(int val)
{
  Node* curr = head;

  if(!head) return;

  while(curr)
  {
    if(curr->val == val)
    {
      Node* previous = curr->prev;
      Node* next = curr->next;
      previous->next = next;
      next->prev = previous;
      delete curr;
      return;
    }
    curr = curr->next;
  }
}

void DoublyLinkedList::deleteNode()
{
  Node* temp = head;
  head = head->next;
  head->prev = NULL;
  delete temp;
}

void DoublyLinkedList::reverse()
{
  if(!head->next) return;

  Node* newHead = NULL;

  //Take head node and insert it into new list
  //Pop head in the old list
  //Assign newHead to head

  while(head)
  {
    Node* temp = new Node;
    if(!newHead)
    {
      temp->val = head->val;
      temp->prev = NULL;
      temp->next = NULL;
      newHead = temp;
    }
    else
    {
      temp->val = head->val;
      temp->prev = NULL;
      temp->next = newHead;
      newHead->prev = temp;
      newHead = temp;
    }

    temp = head;
    head = head->next;
    delete temp;
  }

  head = newHead;
}

DoublyLinkedList::~DoublyLinkedList()
{
  Node* curr = head;

  while(curr)
  {
    Node* temp = curr;
    curr = curr->next;
    delete temp;
  }
}
