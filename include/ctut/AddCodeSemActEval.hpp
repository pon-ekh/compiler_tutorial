#pragma once

namespace ctut {

class IntEvalResultSink;
class LineSource;

namespace AddCodeSemActEval {
  
auto eval(LineSource& source, IntEvalResultSink& sink) -> void;

};

}
