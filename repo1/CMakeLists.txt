cmake_minimum_required(VERSION 3.10)

project("repo1" VERSION 0.1.0)

set(CMAKE_CXX_STANDARD 17)

add_executable(hello_world hello_world.cpp)

target_link_libraries(hello_world ${CONAN_LIBS})

install(TARGETS hello_world RUNTIME DESTINATION bin)