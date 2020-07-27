#include <charconv>
#include <iostream>
#include <sstream>

void
consume_whitespace(std::string::const_iterator& ptr,
                   std::string::const_iterator last) {
  for (; ptr != last && *ptr == ' '; ++ptr);
}

int
parse_integer(std::string::const_iterator& ptr,
              std::string::const_iterator last) {
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
  (void)result;
  
  return value;
}

void
parse_plus_sign(std::string::const_iterator& ptr,
                std::string::const_iterator last) {
  if (ptr == last || *ptr != '+') {
    throw std::runtime_error("Expected +, remaining: '" + std::string(ptr, last) + "'");
  }
  ++ptr;
}

void
maybe_parse_end_of_line(std::string::const_iterator& ptr,
                    std::string::const_iterator last) {
  if (ptr != last) {
    if (*ptr != '\n') {
      throw std::runtime_error("Expected end of line, remaining: '" + std::string(ptr, last) + "'");
    } else {
      ++ptr;
    }
  }  
}

int
compute_line(std::string::const_iterator& ptr,
             std::string::const_iterator last) {
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

int
main(int argc, char** argv) {
  std::string line;
  while (std::getline(std::cin, line)) {
    if (line.empty()) {
      continue;
    }
    
    std::string::const_iterator ptr = line.cbegin();
    try {
      const int result = compute_line(ptr, line.cend());
      std::cout << result << std::endl;
    } catch (std::runtime_error& err) {
      std::cout << "ERROR: " << err.what() << std::endl;
    }
  }
  return 0;
}
