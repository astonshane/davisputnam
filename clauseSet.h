#ifndef __clauseSet__h__
#define __clauseSet__h__

#include <iostream>
#include <set>
#include <algorithm>
#include "literal.h"

using namespace std;

class ClauseSet{
public:
  ClauseSet(){}

  void insert(Clause C){
    for(int i=0; i<clause_set.size(); i++){
      if(C == clause_set[i]){
        return;
      }
    }

    clause_set.push_back(C);
    sort(clause_set.begin(), clause_set.end());
  }

  void printSet(){
    cout << "=== begin set ===" << endl;
    for(int i=0; i<clause_set.size();i++){
      clause_set[i].printClause();
    }
    cout << "=== end set ===" << endl << endl;
  }

private:
  vector<Clause> clause_set;
};

#endif
