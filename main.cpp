#include "datalgo.hpp"
#include <iostream>

using namespace std;

int main()
{
  DoublyLinkedList list(2);
  // for(int i = 0; i < 100; i++)
  //   list.insertTail(i);
  list.reverse();
  //list.display();
  list.testDoubleLinks();

  cout << "Done!" << endl;
  return 0;
}
