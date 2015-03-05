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


bool Clause::contains(Literal L){
  set<Literal>::iterator itr = literals.find(L);
  if(itr != literals.end()){
    return true;
  }else{
    return false;
  }
}

Clause Clause::reduce(Literal L){

  Clause C;

  set<Literal> cpy = literals;
  set<Literal>::iterator itr = cpy.find(L);
  if(itr != cpy.end()){
    cpy.erase(itr);
  }

  C.literals = cpy;

  return C;
}
