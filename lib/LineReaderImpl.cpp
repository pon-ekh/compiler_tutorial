#include "LineReaderImpl.hpp"

#include <istream>

namespace ctut {

LineReaderImpl::LineReaderImpl(std::istream& stream)
  : m_stream(stream) {
}

LineReaderImpl::~LineReaderImpl() = default;

auto
LineReaderImpl::get(std::string& buffer) -> bool {
  return static_cast<bool>(std::getline(m_stream, buffer));
}
  
}
