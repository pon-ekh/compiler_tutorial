add_test(
  NAME simple_adder_test_simple_addition
  COMMAND ${CMAKE_SOURCE_DIR}/test/test_simple_addition ${CMAKE_BINARY_DIR}/bin/simple_adder
  )
