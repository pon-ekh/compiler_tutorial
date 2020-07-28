#include <ctut/LineReader.hpp>

#include "LineReaderImpl.hpp"

namespace ctut {

LineReader::LineReader(std::istream& stream)
  : m_impl(std::make_unique<LineReaderImpl>(stream)) {
}

LineReader::~LineReader() = default;
LineReader::LineReader(LineReader&&) = default;
LineReader& LineReader::operator=(LineReader&&) = default;

auto
LineReader::get(std::string& buffer)-> bool {
  return m_impl->get(buffer);
}

}
