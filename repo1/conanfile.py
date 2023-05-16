from conans import ConanFile, CMake, tools


class HelloConan(ConanFile):
    name = "hello"
    version = "1.1.0"
    license = "<Insert the license here>"
    author = "<Insert your name here>"
    url = "<Insert URL here>"
    description = "<Insert description here>"
    topics = ("<Insert topics here>", "<insert topics here>")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def requirements(self):
        self.requires("openssl/1.1.1t")

    def build(self):
        # cmake = CMake(self)
        # cmake.configure()
        # cmake.build()
        self.run(f"cp -r /home/julianmr/eclypsium/oss_famaf_demo/oss_demo_cpp/repo1 .")
        self.run(f"pwd")
        self.run(f"ls")
        self.run(f"cmake -S ./repo1/ -B .")
        self.run(f"make -j8 hello --help")

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]