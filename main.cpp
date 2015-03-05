#include <iostream>
#include <vector>
#include "literal.h"
#include "clause.h"
#include "clauseSet.h"


using namespace std;

/*
vector<clause> S;
bool satisfiable(S){
  if S == {}:
    return true; // open clause
  if S = {{}}:
    return false;
  if {} in S:
    return false //closed branch
  if {L} in S:
    return satisfiable(S_L)
  select L in Literals(S)

  return satisfiable(S_L) || satisfiable(S_L`)
}
*/

bool satisfiable(ClauseSet S){
  //if S == {}
  //  return true
  if(S.size() == 0){
    return true;
  }

  //if {} in S:
  //  return false: //closed branch
  vector<Clause> cs = S.clauseSet();
  for(int i=0; i<cs.size(); i++){
    Clause c = cs[i];
    if(c.size() == 0){
      return false;
    }
  }

  //if {L} in S:
  //  return satisfiable(S_L)

  //else
  //  select L in Literals(S)
  //  satisfiable(S_L) || satisfiable(S_L`)
  char L = S.nextLiteral();
  cout << L << endl;
  Literal L1(L, false); //A
  Literal L2(L, true);  //~A


  return false;

}


int main(){
  Literal a('A', false);
  Literal nota('A', true);
  Literal n('N', false);
  Literal notn('N', true);
  Literal q('Q', false);
  Literal notq('Q', true);

  Clause C1;
  C1.addLiteral(nota);
  C1.addLiteral(n);
  C1.addLiteral(q);
  //C1.printClause();

  Clause C2;
  C2.addLiteral(notn);
  //C2.printClause();

  Clause C3;
  C3.addLiteral(a);
  //C3.printClause();

  Clause C4;
  C4.addLiteral(notq);
  //C4.printClause();

  Clause C5; //empty set

  //cout << endl << endl;

  ClauseSet S;
  S.insert(C1);

  S.insert(C2);

  S.insert(C3);

  S.insert(C3);

  S.insert(C4);
  //S.insert(C5);
  S.printSet();

  bool sat = satisfiable(S);
  if(sat){
    cout << "S was satisfiable!" << endl;
  }else{
    cout << "S was not satisfiable!" << endl;
  }


}
