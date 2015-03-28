#ifndef __clauseSet__h__
#define __clauseSet__h__

#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include "literal.h"
#include "clause.h"

using namespace std;

class ClauseSet{
public:
  ClauseSet(){}

  //adds a Clause C to the existing clause set
  //works like std::set would: sorted, with no duplicates
  //didn't use std::set becuase of some strange errors that I didn't feel
  //like debugging at the time
  void insert(Clause C);

  //returns a set of all of the literals currently contained in the clause set
  set<char> literalsSet();

  //returns the next literal to be branched on in the clause set
  //for now, just returns the first that it finds, should be optimized later
  char nextLiteral();

  ClauseSet reduce(Literal L1, Literal L2);

  //returns the size of the clause set
  int size(){ return clause_set.size();}

  //outputs the current contents of the clause set
  void printSet();


  //returns a copy of the vector containing the clause set
  vector<Clause> clauseSet(){ return clause_set;}

private:
  vector<Clause> clause_set;
};

#endif
