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

//outputs the current contents of the clause set
void ClauseSet::printSet(){
  cout << "=== begin set ===" << endl;
  for(int i=0; i<clause_set.size();i++){
    clause_set[i].printClause();
  }
  cout << "=== end set ===" << endl << endl;
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
