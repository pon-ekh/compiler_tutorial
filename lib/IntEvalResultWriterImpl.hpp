#pragma once

#include <iosfwd>

namespace ctut {

class IntEvalResult;

class IntEvalResultWriterImpl {
public:
  explicit IntEvalResultWriterImpl(std::ostream& stream);
  ~IntEvalResultWriterImpl();

  auto push(const IntEvalResult& obj) -> void;

private:
  std::ostream& m_stream;
};

}
