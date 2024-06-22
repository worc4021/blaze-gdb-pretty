set(CMAKE_TOOLCHAIN_FILE "${CMAKE_CURRENT_SOURCE_DIR}/vcpkg/scripts/buildsystems/vcpkg.cmake" CACHE STRING "Vcpkg toolchain file")
cmake_minimum_required(VERSION 3.25)
project(blaze-prettyprint)

find_package(blaze CONFIG REQUIRED)

add_executable(blaze-prettyprint src/bb.cpp)
target_link_libraries(blaze-prettyprint PRIVATE blaze::blaze)
