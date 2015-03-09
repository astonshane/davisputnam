#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <boost/foreach.hpp>
#include <boost/property_tree/xml_parser.hpp>
#include <boost/property_tree/ptree.hpp>

using namespace std;

string read(istream &is){
  using boost::property_tree::ptree;
  ptree pt;
  read_xml(is, pt);

  string cnf;
  BOOST_FOREACH(ptree::value_type &v, pt.get_child("queryresult.pod")){
    if(v.first == "subpod"){
      cnf = v.second.get<string>("plaintext");
    }
  }
  return cnf;
}

int main(){

  ifstream input("input.xml");

  //cout << "hello world" << endl;
  cout << read(input) << endl;

  return 0;
}
