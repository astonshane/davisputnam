#include <iostream>
#include "literal.h"
#include "clause.h"

using namespace std;

int main(){
  Literal L('a', false);
  Literal L1('a', true);

  Clause C;
  C.addLiteral(L);
  C.addLiteral(L1);

  C.printClause();
}
