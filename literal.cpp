#include <iostream>
#include "literal.h"

using namespace std;

void Literal::printLiteral() const {
  if(negated){
    cout << "~";
  }
  cout << name;
}
