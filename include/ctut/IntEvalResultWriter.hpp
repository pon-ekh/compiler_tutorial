#pragma once

#include <ctut/IntEvalResultSink.hpp>

#include <iosfwd>
#include <memory>

namespace ctut {

class IntEvalResultWriterImpl;
  
class IntEvalResultWriter : public IntEvalResultSink {
public:
  explicit IntEvalResultWriter(std::ostream& stream);
  ~IntEvalResultWriter();
  IntEvalResultWriter(IntEvalResultWriter&&);
  IntEvalResultWriter& operator=(IntEvalResultWriter&&);

  auto push(const IntEvalResult& obj) -> void override;

private:
  std::unique_ptr<IntEvalResultWriterImpl> m_impl;
};

}
