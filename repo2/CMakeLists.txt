project("repo2")

cmake_minimum_required(VERSION 3.10)

# Include the Conan CMake module
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(NO_OUTPUT_DIRS)


add_executable(${REPO_2} "main.cpp")

target_link_libraries(${REPO_2} PRIVATE ${CONAN_LIBS})