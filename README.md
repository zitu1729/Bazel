# Bazel

Bazel is an open-source build and test tool similar to Make, Maven, and Gradle. It uses a human-readable, high-level build language. Bazel supports projects in multiple languages and builds outputs for multiple platforms. Bazel supports large codebases across multiple repositories, and large numbers of users.

## To Build every single target: 
  - bazel build //...

## To Build any specific target: 
  - bazel build //projects/...  
  - bazel build //projects/projectA/...  
  - bazel build //projects/projectB/...  
  #### or  
  - bazel build //projects/projectA:foo  
  - bazel build //projects/projectB:bar  
  #### or  
  - bazel build projects/projectA:foo  
  - bazel build projects/projectB:bar  

## To run any script generated via gen rule: 
  - bazel run //projects/projectA:foo  

  Here, 'foo' or 'bar' denotes the package name inside  
   - genrule(name="foo")  
   - genrule(name="bar")  
  in a BUILD file.  