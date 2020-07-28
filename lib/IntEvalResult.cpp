#include <ctut/IntEvalResult.hpp>

#include <ostream>

namespace ctut {

IntEvalResult::IntEvalResult(int value)
  : m_value(value) {
}

IntEvalResult::IntEvalResult(std::string errmsg)
  : m_errmsg(errmsg) {
}

IntEvalResult::~IntEvalResult() = default;
IntEvalResult::IntEvalResult(IntEvalResult&&) = default;
IntEvalResult::IntEvalResult(const IntEvalResult&) = default;
IntEvalResult& IntEvalResult::operator=(IntEvalResult&&) = default;
IntEvalResult& IntEvalResult::operator=(const IntEvalResult&) = default;

auto
IntEvalResult::getValue() const -> int {
  return m_value;
}

auto
IntEvalResult::hasError() const -> bool {
  return m_errmsg.has_value();
}

auto
IntEvalResult::getError() const -> std::string {
  return *m_errmsg;
}

auto
operator<<(std::ostream& stream, const IntEvalResult& obj) -> std::ostream& {
  if (obj.hasError()) {
    stream << "ERROR: " << obj.getError();
  } else {
    stream << obj.getValue();
  }
  return stream;
}

}
