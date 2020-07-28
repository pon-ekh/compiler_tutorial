#include "IntEvalResultWriterImpl.hpp"

#include <ctut/IntEvalResult.hpp>

#include <ostream>

namespace ctut {

IntEvalResultWriterImpl::IntEvalResultWriterImpl(std::ostream& stream)
  : m_stream(stream) {
}

IntEvalResultWriterImpl::~IntEvalResultWriterImpl() = default;

auto
IntEvalResultWriterImpl::push(const IntEvalResult& obj) -> void {
  m_stream << obj << std::endl;
}

}
