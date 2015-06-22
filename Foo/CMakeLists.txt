cmake_minimum_required(VERSION 3.0)
project(Foo)

add_library(foo foo.cpp foo.hpp boo.hpp)

string(COMPARE EQUAL "${CMAKE_OSX_SYSROOT}" "iphoneos" is_ios)

if(is_ios)
  set_target_properties(
      foo
      PROPERTIES
      INSTALL_NAME_DIR "@rpath/foo.framework/foo"
      INSTALL_RPATH "@executable_path/Frameworks;@loader_path/Frameworks"
  )
endif()

install(TARGETS foo DESTINATION "lib")
install(FILES foo.hpp DESTINATION "include/foo")
install(FILES boo.hpp DESTINATION "include/foo/details")
