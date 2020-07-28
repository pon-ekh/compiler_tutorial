#include <ctut/AddCodeSemActEval.hpp>
#include <ctut/IntEvalResultWriter.hpp>
#include <ctut/LineReader.hpp>

#include <charconv>
#include <iostream>
#include <sstream>


namespace ctut {

int
do_main(int argc, char** argv) {
  LineReader reader(std::cin);
  IntEvalResultWriter writer(std::cout);

  AddCodeSemActEval::eval(reader, writer);
  return 0;
}
  
}

int
main(int argc, char** argv) {
  return ctut::do_main(argc, argv);
}
