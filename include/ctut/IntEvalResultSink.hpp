#pragma once

namespace ctut {

class IntEvalResult;
  
class IntEvalResultSink {
public:
  virtual ~IntEvalResultSink();

  virtual auto push(const IntEvalResult& obj) -> void = 0;
};

}
