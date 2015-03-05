#ifndef __clause__h__
#define __clause__h__

#include <iostream>
#include <set>
#include "literal.h"

using namespace std;

class Clause{
public:
  Clause(){}

  void printClause(){
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

  void addLiteral(Literal L){
    literals.insert(L);
  }


private:
  set<Literal> literals;

};

#endif
