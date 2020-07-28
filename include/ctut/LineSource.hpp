#pragma once

#include <string>

namespace ctut {

class LineSource {
public:
  virtual ~LineSource();

  virtual auto get(std::string& buffer) -> bool = 0;
};

}
