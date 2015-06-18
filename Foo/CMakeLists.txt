cmake_minimum_required(VERSION 3.0)
project(Foo)

add_library(foo foo.cpp foo.hpp boo.hpp)

install(TARGETS foo DESTINATION "lib")
install(FILES foo.hpp DESTINATION "include")
install(FILES boo.hpp DESTINATION "include/details")
