#pragma once

#include <iosfwd>

namespace ctut {

class LineReaderImpl {
public:
  explicit LineReaderImpl(std::istream& stream);
  ~LineReaderImpl();

  auto get(std::string& buffer) -> bool;

private:
  std::istream& m_stream;
};

}
