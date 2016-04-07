from conans import ConanFile, CMake
   
class HelloConan(ConanFile):
   name = "Hello"
   version = "0.1"
   license="MIT"
   settings = "os", "compiler", "build_type", "arch"
   url = "https://github.com/memsharded/conan-hello-embed.git"

   def build(self):
       cmake = CMake(self.settings)
       self.run('cmake . %s' % cmake.command_line)
       self.run("cmake --build . %s" % cmake.build_config)

   def package(self):
       self.copy("*.h", dst="include", src="hello")
       self.copy("*.lib", dst="lib", src="hello/lib")
       self.copy("*.a", dst="lib", src="hello/lib")

   def package_info(self):
       self.cpp_info.libs = ["hello"]
