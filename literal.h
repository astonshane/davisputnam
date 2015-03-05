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

  void printLiteral() const {
    if(negated){
      cout << "~";
    }
    cout << name;
  }

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
  if(lhs.name < rhs.name){
    return true;
  }
  return false;
}

#endif
