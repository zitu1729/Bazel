# Bazel

Bazel is an open-source build and test tool similar to Make, Maven, and Gradle. It uses a human-readable, high-level build language. Bazel supports projects in multiple languages and builds outputs for multiple platforms. Bazel supports large codebases across multiple repositories, and large numbers of users.  
Bazel builds software from source code organized in directory trees called repositories. A defined set of repositories comprises the workspace. Source files in repositories are organized in a nested hierarchy of packages, where each package is a directory that contains a set of related source files and one **BUILD** file. The **BUILD** file specifies what software outputs can be built from the source.  

### Repositories
Source files used in a Bazel build are organized in repositories (often shortened to repos). A repo is a directory tree with a boundary marker file at its root; such a boundary marker file could be **MODULE.bazel**, **REPO.bazel**, or in legacy contexts, **WORKSPACE** or **WORKSPACE.bazel**.  
A workspace is the environment shared by all Bazel commands run from the same main repo. It encompasses the main repo and the set of all defined external repos.

### Packages 
The primary unit of code organization in a repository is the package. A package is a collection of related files and a specification of how they can be used to produce output artifacts.

A package is defined as a directory containing a **BUILD** file named either **BUILD** or **BUILD.bazel**. A package includes all files in its directory, plus all subdirectories beneath it, except those which themselves contain a **BUILD** file. From this definition, no file or directory may be a part of two different packages.



## To build every single target: 
  - bazel build //...

## To build any specific target: 
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

## To run any test case:
  - bazel test projects/calculator/...  
