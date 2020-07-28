#pragma once

#include <optional>
#include <string>

namespace ctut {
  
class IntEvalResult {
public:
  explicit IntEvalResult(int value);
  explicit IntEvalResult(std::string errmsg);
  ~IntEvalResult();
  IntEvalResult(IntEvalResult&&);
  IntEvalResult(const IntEvalResult&);
  IntEvalResult& operator=(IntEvalResult&&);
  IntEvalResult& operator=(const IntEvalResult&);

  auto getValue() const -> int;
  auto hasError() const -> bool;
  auto getError() const -> std::string;

private:
  int m_value;
  std::optional<std::string> m_errmsg;
};

auto operator<<(std::ostream& stream, const IntEvalResult& obj) -> std::ostream&;

}
