#include <ctut/AddCodeSemActEval.hpp>

#include <ctut/IntEvalResult.hpp>
#include <ctut/IntEvalResultSink.hpp>
#include <ctut/LineSource.hpp>

#include <charconv>
#include <stdexcept>

namespace ctut {
namespace AddCodeSemActEval {
namespace {

auto
consume_whitespace(std::string::const_iterator& ptr,
                   std::string::const_iterator last)
  -> void {
  
  for (; ptr != last && *ptr == ' '; ++ptr);
}

auto
parse_integer(std::string::const_iterator& ptr,
              std::string::const_iterator last)
  -> int {
  
  if (ptr == last) {
    throw std::runtime_error("Expected integer, remaining: ''");
  }
  
  int value;
  const char* start = &*ptr;
  auto result = std::from_chars(start, &*last, value);
  if (start == result.ptr) {
    throw std::runtime_error("Expected integer, remaining: '" + std::string(ptr, last) + "'");
  }
  
  ptr += (result.ptr - start);
  return value;
}

auto
parse_plus_sign(std::string::const_iterator& ptr,
                std::string::const_iterator last)
  -> void {
  
  if (ptr == last || *ptr != '+') {
    throw std::runtime_error("Expected +, remaining: '" + std::string(ptr, last) + "'");
  }
  ++ptr;
}

auto
maybe_parse_end_of_line(std::string::const_iterator& ptr,
                        std::string::const_iterator last)
  -> void {
  
  if (ptr != last) {
    if (*ptr != '\n') {
      throw std::runtime_error("Expected end of line, remaining: '" + std::string(ptr, last) + "'");
    } else {
      ++ptr;
    }
  }  
}

auto 
compute_line(std::string::const_iterator& ptr,
             std::string::const_iterator last)
  -> int {
  
    consume_whitespace(ptr, last);
    const int x = parse_integer(ptr, last);
    consume_whitespace(ptr, last);
    parse_plus_sign(ptr, last);
    consume_whitespace(ptr, last);
    const int y = parse_integer(ptr, last);
    consume_whitespace(ptr, last);
    maybe_parse_end_of_line(ptr, last);
    return x + y;
}

auto
do_eval(const std::string& buffer)
  -> IntEvalResult {
  
  try {
    std::string::const_iterator ptr = buffer.cbegin();
    const int result = compute_line(ptr, buffer.cend());
    return IntEvalResult(result);
  } catch (std::runtime_error& err) {
    return IntEvalResult(err.what());
  }

}
  
}
  
auto
eval(LineSource& source, IntEvalResultSink& sink)
  -> void {
  
  std::string buffer;
  while (source.get(buffer)) {
    if (buffer.empty()) {
      continue;
    }
    
    IntEvalResult result = do_eval(buffer);
    sink.push(result);
  }
}

};

}
