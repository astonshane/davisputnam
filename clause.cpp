#include <iostream>
#include "clause.h"

using namespace std;

void Clause::printClause() const{
  cout << "{";
  set<Literal>::iterator itr = literals.begin();

  for(; itr != literals.end(); ){
    itr->printLiteral();
    itr++;
    if(itr != literals.end()){
      cout << ", ";
    }
  }
  cout << "}" << endl;
}
