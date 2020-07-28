#include <ctut/IntEvalResultWriter.hpp>

#include "IntEvalResultWriterImpl.hpp"

namespace ctut {

IntEvalResultWriter::IntEvalResultWriter(std::ostream& stream)
  : m_impl(std::make_unique<IntEvalResultWriterImpl>(stream)) {
}

IntEvalResultWriter::~IntEvalResultWriter() = default;
IntEvalResultWriter::IntEvalResultWriter(IntEvalResultWriter&&) = default;
IntEvalResultWriter& IntEvalResultWriter::operator=(IntEvalResultWriter&&) = default;

auto
IntEvalResultWriter::push(const IntEvalResult& obj) -> void {
  m_impl->push(obj);
}

}
