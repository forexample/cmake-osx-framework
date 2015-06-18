cmake_minimum_required(VERSION 3.0)
project(Boo)

add_executable(boo boo.cpp)

get_filename_component(
    framework_dir
    "${CMAKE_CURRENT_LIST_DIR}/../_framework/${POLLY_TOOLCHAIN_TAG}"
    ABSOLUTE
)

target_compile_options(boo PUBLIC "-F" "${framework_dir}")
target_link_libraries(boo "-F ${framework_dir} -framework Foo")

string(COMPARE EQUAL "${CMAKE_OSX_SYSROOT}" "iphoneos" is_ios)
if(NOT is_ios)
  enable_testing()
  add_test(NAME BooTest COMMAND boo)
endif()
