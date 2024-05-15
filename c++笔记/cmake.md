## 介绍

CMake是一个跨平台的开源构建系统，用于管理软件项目的构建过程。它可以生成适用于各种操作系统和编译器的构建文件。CMake的编译过程一般包括以下步骤：

1. 编写CMakeLists.txt文件。
2. 使用cmake命令将CMakeLists.txt文件转换为make所需的makefile文件。
3. 使用make命令编译源代码，生成可执行文件或库。

一般将CMakeLists.txt文件放在项目的根目录下。

### CMakeLists.txt常用命令及流程

- **设置project名称：** `project(xxx)`，会创建`PROJECT_SOURCE_DIR`和`PROJECT_NAME`变量，分别表示当前目录和项目名称。
- **获取源文件路径：** `aux_source_directory(路径 变量)`。
- **设置变量：** `set(变量 值)`，用于给文件名、路径名或其他字符串赋值。
- **添加编译选项：** `add_definitions(编译选项)`。
- **打印消息：** `message(消息)`。
- **编译子目录的CMakeLists.txt：** `add_subdirectory(子目录名称)`。
- **生成静态库：** `add_library(库文件名称 STATIC 文件)`，将.cpp/.c/.cc文件生成静态库。
- **生成可执行文件：** `add_executable(可执行文件名称 文件)`，将.cpp/.c/.cc文件生成可执行文件。
- **规定.h头文件路径：** `include_directories(路径)`。
- **规定.so/.a库文件路径：** `link_directories(路径)`。
- **链接库文件：** `target_link_libraries(目标文件 链接的库文件)`。

### CMakeLists.txt的基本流程

1. **声明cmake最低版本：** `cmake_minimum_required(VERSION x.x)`。
2. **添加工程名称：** `project(xxx)`。
3. **设置编译模式：** `set(CMAKE_BUILD_TYPE Debug/Release)`。
4. **添加子目录：** `add_subdirectory(子目录名称)`。
5. **添加头文件路径：** `include_directories(路径)`。
6. **添加源代码路径：** `set(SRC 文件路径)`。
7. **创建共享库/静态库：** `add_library(库文件名称 STATIC/SHARED 文件)`。
8. **链接库文件：** `target_link_libraries(目标文件 链接的库文件)`。
9. **编译主函数，生成可执行文件：** `add_executable(可执行文件名称 源文件)`。

## 具体编写步骤

### 1. 声明的cmake最低版本

```cmake
cmake_minimum_required(VERSION 3.4)
```

### 2. 设置编译模式

```cmake
set(CMAKE_BUILD_TYPE Debug)
```

### 3. 添加工程名称

```cmake
project(TEST)
```

### 4. 添加子目录

```cmake
add_subdirectory(submodule_dir)
```

### 5. 添加头文件路径

```cmake
include_directories(
    ${PROJECT_SOURCE_DIR}/include/dir1
    ${PROJECT_SOURCE_DIR}/include/dir2
)
```

### 6. 添加源代码路径

```cmake
set(SRC 
    ${PROJECT_SOURCE_DIR}/src/file1.cpp
    ${PROJECT_SOURCE_DIR}/src/file2.cpp
)
```

### 7. 创建共享库/静态库

```cmake
add_library(lib_name STATIC ${SRC})
```

### 8. 链接库文件

```cmake
target_link_libraries(executable_name lib_name)
```

### 9. 编译主函数，生成可执行文件

```cmake
add_executable(main ${SRC})
```

以上是一个简化的CMakeLists.txt的例子，希望对你有所帮助。

```cmake
cmake_minimum_required(VERSION 3.4)  # 指定所需的 CMake 最低版本

project(sasu CXX)  # 指定项目名称和使用的语言

set(CMAKE_CXX_STANDARD 17)  # 设置 C++ 标准版本为 C++17

set(CMAKE_CXX_FLAGS "-O3 -Wall -mcpu=native -flto -pthread")  # 设置编译器标志

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)  # 生成编译命令数据库，用于一些编辑器和 IDE

set(INCLUDE_PATH "/usr/local/include")  # 定义包含文件的路径
set(LIB_PATH "/usr/local/lib")  # 定义库文件的路径

#---------------------------------------------------------------------
#       [ Include、Lib  : Define ] ==> []
#---------------------------------------------------------------------

set(COMMON_LIB_DIR "${PROJECT_SOURCE_DIR}/lib/")  # 定义通用库文件目录

set(COMMON_INCLUDE_DIR "${PROJECT_SOURCE_DIR}/include"
                        "${PROJECT_SOURCE_DIR}/config"
                        "${PROJECT_SOURCE_DIR}/src"
                        "${PROJECT_SOURCE_DIR}/tool")  # 定义通用的包含文件目录

link_directories(${COMMON_LIB_DIR})  # 添加通用库文件目录
include_directories(${COMMON_INCLUDE_DIR})  # 添加通用的包含文件目录

#---------------------------------------------------------------------
#       [ Include、Lib  : Path ] ==> [ glib opencv ]
#---------------------------------------------------------------------

find_package(PkgConfig)  # 寻找和载入 pkg-config 软件包
pkg_search_module(GLIB REQUIRED glib-2.0)  # 寻找 glib 软件包
include_directories(${GLIB_INCLUDE_DIRS})  # 添加 glib 包含文件目录

find_package(OpenCV REQUIRED)  # 寻找 OpenCV 软件包
include_directories(${OpenCV_INCLUDE_DIRS})  # 添加 OpenCV 包含文件目录

pkg_search_module(SERIAL REQUIRED libserial)  # 寻找 libserial 软件包
include_directories(${SERIAL_INCLUDE_DIRS})  # 添加 libserial 包含文件目录
link_directories(${SERIAL_LIBRARY_DIRS})  # 添加 libserial 库文件目录

# 寻找 ppnc 软件包
pkg_search_module(PPNC REQUIRED ppnc)
include_directories(${PPNC_INCLUDE_DIRS})  # 添加 ppnc 包含文件目录
link_directories(${PPNC_LIBRARY_DIRS})  # 添加 ppnc 库文件目录

# 寻找 onnx 软件包
pkg_search_module(ONNX REQUIRED onnx)
include_directories(${ONNX_INCLUDE_DIRS})  # 添加 onnx 包含文件目录
link_directories(${ONNX_LIBRARY_DIRS})  # 添加 onnx 库文件目录

#---------------------------------------------------------------------
#               [ bin ] ==> [ demo ]
#---------------------------------------------------------------------

# 图像采集
set(COL_PROJECT_NAME "collection")
set(COL_PROJECT_SOURCES ${PROJECT_SOURCE_DIR}/tool/collection.cpp)
add_executable(${COL_PROJECT_NAME} ${COL_PROJECT_SOURCES})  # 添加可执行文件
target_link_libraries(${COL_PROJECT_NAME} pthread ${OpenCV_LIBS} ${SERIAL_LIBRARIES})  # 链接需要的库文件

# 图像合成
set(IMG2V_PROJECT_NAME "img2video")
set(IMG2V_PROJECT_SOURCES ${PROJECT_SOURCE_DIR}/tool/img2video.cpp)
add_executable(${IMG2V_PROJECT_NAME} ${IMG2V_PROJECT_SOURCES})  # 添加可执行文件
target_link_libraries(${IMG2V_PROJECT_NAME} pthread ${OpenCV_LIBS})  # 链接需要的库文件

# 相机标定
set(CAL_PROJECT_NAME "calibration")
set(CAL_PROJECT_SOURCES ${PROJECT_SOURCE_DIR}/tool/calibration.cpp)
add_executable(${CAL_PROJECT_NAME} ${CAL_PROJECT_SOURCES})  # 添加可执行文件
target_link_libraries(${CAL_PROJECT_NAME} pthread ${OpenCV_LIBS})  # 链接需要的库文件

# 相机测试
set(CAM_PROJECT_NAME "camera")
set(CAM_PROJECT_SOURCES ${PROJECT_SOURCE_DIR}/tool/camera.cpp)
add_executable(${CAM_PROJECT_NAME} ${CAM_PROJECT_SOURCES})  # 添加可执行文件
target_link_libraries(${CAM_PROJECT_NAME} pthread ${OpenCV_LIBS})  # 链接需要的库文件

#---------------------------------------------------------------------
#               [ bin ] ==> [ main ]
#---------------------------------------------------------------------

set(ICAR_PROJECT_NAME "icar")
set(ICAR_PROJECT_SOURCES ${PROJECT_SOURCE_DIR}/src/icar.cpp)
add_executable(${ICAR_PROJECT_NAME} ${ICAR_PROJECT_SOURCES})
target_link_libraries(${ICAR_PROJECT_NAME} ${PPNC_LIBRARIES})
target_link_libraries(${ICAR_PROJECT_NAME} ${ONNX_LIBRARIES})
target_link_libraries(${ICAR_PROJECT_NAME} ${OpenCV_LIBS})
target_link_libraries(${ICAR_PROJECT_NAME} pthread )
target_link_libraries(${ICAR_PROJECT_NAME} ${SERIAL_LIBRARIES})

```



| 命令                                                         | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| cmake_minimum_required(VERSION 3.4...3.18)                   | 指定项目所需的 CMake 最低版本范围为 3.4 到 3.18              |
| project(sasu CXX)                                            | 指定项目的名称为 "sasu"，并且使用 C++ 语言                   |
| set(CMAKE_CXX_STANDARD 17)                                   | 设置 C++ 标准版本为 C++17                                    |
| set(CMAKE_CXX_FLAGS "-O3 -Wall -mcpu=native -flto -pthread") | 设置编译器选项，包括优化级别、警告开关、CPU 架构优化、链接时优化和线程支持 |
| set(CMAKE_EXPORT_COMPILE_COMMANDS ON)                        | 启用生成编译命令数据库                                       |
| set(INCLUDE_PATH "/usr/local/include")                       | 设置包含文件路径为 /usr/local/include                        |
| set(LIB_PATH "/usr/local/lib")                               | 设置库文件路径为 /usr/local/lib                              |
| find_package(PkgConfig)                                      | 寻找并载入 pkg-config 软件包                                 |
| pkg_search_module(GLIB REQUIRED glib-2.0)                    | 查找并存储 glib-2.0 软件包信息                               |
| pkg_search_module(SERIAL REQUIRED libserial)                 | 查找并存储 libserial 软件包信息                              |
| pkg_search_module(PPNC REQUIRED ppnc)                        | 查找并存储 ppnc 软件包信息                                   |
| pkg_search_module(ONNX REQUIRED onnx)                        | 查找并存储 onnx 软件包信息                                   |
| include_directories()                                        | 添加包含文件目录                                             |
| link_directories()                                           | 添加库文件目录                                               |
| find_package(OpenCV REQUIRED)                                | 在系统中查找并存储 OpenCV 库信息                             |
| add_executable()                                             | 添加可执行文件                                               |
| target_link_libraries()                                      | 链接目标文件与库文件                                         |

## 构建和编译项目

下面是将项目编译的基本步骤：

1. **在项目中创建build目录并进入：**

```bash
mkdir build && cd build
```

这个命令将会在当前目录下创建一个名为 `build` 的文件夹，并且进入到这个文件夹中。

2. **运行 CMake 生成 Makefile：**

```bash
cmake ..  #.. 是指项目所在的相对位置
```

这个命令会在 `build` 文件夹中生成 Makefile，以便后续的编译。

3. **使用 Make 编译项目：**

```bash
make
```

这个命令会根据生成的 Makefile 编译项目，生成可执行文件或者库文件。

这些步骤是在命令行中执行的，确保你在项目的根目录下执行这些命令，并且已经安装了 CMake 和 Make 工具。

```
./可执行文件   #运行生成的项目文件
```

