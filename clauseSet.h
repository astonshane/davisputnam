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
  void insert(Clause C){
    for(int i=0; i<clause_set.size(); i++){
      if(C == clause_set[i]){
        return;
      }
    }
    clause_set.push_back(C);
    sort(clause_set.begin(), clause_set.end());
  }

  //outputs the current contents of the clause set
  void printSet(){
    cout << "=== begin set ===" << endl;
    for(int i=0; i<clause_set.size();i++){
      clause_set[i].printClause();
    }
    cout << "=== end set ===" << endl << endl;
  }

  //returns a set of all of the literals currently contained in the clause set
  set<char> literalsSet(){
    set<char> lits;
    for(int i=0; i<clause_set.size(); i++){
      set<Literal> clause_literals = clause_set[i].literals;
      set<Literal>::iterator itr = clause_literals.begin();
      for(; itr != clause_literals.end(); itr++){
        lits.insert(itr->name);
      }
    }
    return lits;
  }

  //returns the next literal to be branched on in the clause set
  //for now, just returns the first that it finds, should be optimized later
  char nextLiteral(){
    for(int i=0; i<clause_set.size(); i++){
      set<Literal> clause_literals = clause_set[i].literals;
      set<Literal>::iterator itr = clause_literals.begin();
      for(; itr != clause_literals.end(); itr++){
        return itr->name;
      }
    }
    return '!';
  }

  //returns the size of the clause set
  int size(){ return clause_set.size();}

  //returns a copy of the vector containing the clause set
  vector<Clause> clauseSet(){ return clause_set;}

private:
  vector<Clause> clause_set;
};

#endif
