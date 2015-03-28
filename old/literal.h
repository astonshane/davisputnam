#ifndef __literal__h__
#define __literal__h__

using namespace std;

class Literal{
public:
  Literal(){}
  Literal(char name, bool negated){
    this->name = name;
    this->negated = negated;
  }

  void printLiteral() const;

  char name;
  bool negated;
private:

};


inline bool operator==(const Literal& lhs, const Literal& rhs){
  if(lhs.name == rhs.name && lhs.negated == rhs.negated){
    return true;
  }else{
    return false;
  }
}
inline bool operator!=(const Literal& lhs, const Literal& rhs){return !(lhs == rhs);}

inline bool operator< (const Literal& lhs, const Literal& rhs){
  if(lhs.name < rhs.name){ //A < B
    return true;
  }else if(lhs.name == rhs.name){ //A, ~A
    if(!lhs.negated && rhs.negated){ //A < ~A == TRUE
      return true;
    }else{ //~A, ~A || ~A, A
      return false;
    }
  }else{ //B < A
    return false;
  }
}

#endif
