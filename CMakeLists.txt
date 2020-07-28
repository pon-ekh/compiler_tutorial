project(pmdp)
cmake_minimum_required(VERSION 3.2)

enable_testing()

if(COVERAGE)
  add_definitions("-fprofile-arcs -ftest-coverage")
  set(GCC_COVERAGE_LINK_FLAGS "-fprofile-arcs -lgcov")
  set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${GCC_COVERAGE_LINK_FLAGS}" )
  set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} ${GCC_COVERAGE_LINK_FLAGS}" )
  
  add_custom_target(clean_lcov ${CMAKE_SOURCE_DIR}/clean_lcov.sh)
  add_custom_target(clean_gcov ${CMAKE_SOURCE_DIR}/clean_gcov.sh)
  add_custom_target(clean_coverage make clean_lcov && make clean_gcov)
  add_custom_target(clean_all make clean && make clean_coverage)

  add_custom_target(gcov ${CMAKE_SOURCE_DIR}/make_gcov.sh)
  add_custom_target(lcov ${CMAKE_SOURCE_DIR}/make_lcov.sh)
endif()

set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -Wl,--no-undefined" )
add_definitions("-pthread --std=c++17 -Wall -Werror")

include_directories(${CMAKE_SOURCE_DIR}/include)
add_subdirectory(bin)
add_subdirectory(lib)
add_subdirectory(test)
