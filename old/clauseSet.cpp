#include <iostream>
#include "clauseSet.h"
#include "clause.h"
#include "literal.h"

using namespace std;

void ClauseSet::insert(Clause C){
  for(int i=0; i<clause_set.size(); i++){
    if(C == clause_set[i]){
      return;
    }
  }
  clause_set.push_back(C);
  sort(clause_set.begin(), clause_set.end());
}

//returns a set of all of the literals currently contained in the clause set
set<char> ClauseSet::literalsSet(){
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
char ClauseSet::nextLiteral(){
  for(int i=0; i<clause_set.size(); i++){
    set<Literal> clause_literals = clause_set[i].literals;
    set<Literal>::iterator itr = clause_literals.begin();
    for(; itr != clause_literals.end(); itr++){
      return itr->name;
    }
  }
  return '!';
}

ClauseSet ClauseSet::reduce(Literal L1, Literal L2){
  ClauseSet S;

  //for each clause C in clause_set:
  for(int i=0; i < size(); i++){
    Clause C = clause_set[i];

    //if L1 in C:
      //continue -- this statement has been made "true"
    if(C.contains(L1)){
      continue;
    }
    //else if L2 in C:
      //remove L2 from C
    Clause C1 = C.reduce(L2);
    //            ^^^^^^^^^^
    //            returns a copy of C with Literal L2 removed, if it was there
    //                at all

    //add C1 C to S
    S.insert(C1);
  }

  return S;
}



//outputs the current contents of the clause set
void ClauseSet::printSet(){
  cout << "=== begin set ===" << endl;
  for(int i=0; i<clause_set.size();i++){
    clause_set[i].printClause();
  }
  cout << "=== end set ===" << endl << endl;
}
