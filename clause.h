#ifndef __clause__h__
#define __clause__h__

#include <iostream>
#include <set>
#include "literal.h"

using namespace std;

class Clause{
public:
  Clause(){}

  void printClause() const;

  void addLiteral(Literal L){ literals.insert(L); }

  int size(){ return literals.size(); }

  set<Literal> literals;

};

inline bool operator==(const Clause& lhs, const Clause& rhs){
  if(lhs.literals.size() != rhs.literals.size()){
    return false;
  }
  set<Literal>::iterator litr = lhs.literals.begin();
  set<Literal>::iterator ritr = rhs.literals.begin();
  for(; litr != lhs.literals.end(); litr++, ritr++){
    if(*litr != *ritr){
      return false;
    }
  }
  return true;
}


inline bool operator!=(const Clause& lhs, const Clause& rhs){
  return !(lhs == rhs);
}

inline bool operator< (const Clause& lhs, const Clause& rhs){
  if(lhs.literals.size() < rhs.literals.size()){
    return true;
  }
  return false;
}

#endif
