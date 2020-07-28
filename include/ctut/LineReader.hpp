#pragma once

#include <ctut/LineSource.hpp>

#include <iosfwd>
#include <memory>

namespace ctut {

class LineReaderImpl;

class LineReader : public LineSource {
public:
  explicit LineReader(std::istream& stream);
  ~LineReader();
  LineReader(LineReader&&);
  LineReader& operator=(LineReader&&);

  auto get(std::string& buffer) -> bool override;

private:
  std::unique_ptr<LineReaderImpl> m_impl;
};

}
