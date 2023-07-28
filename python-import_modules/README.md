# python-import_modules
This is the beginning of the Module Importer project! This project focuses on the fundamentals of the import module in python enabling you to leverage existing code  

## Table of Contents

- [Python Module Importer](#python-module-importer)
    - [Table of Contents](#table-of-contents)
    - [Introduction](#introduction)
    - [Getting Started](#getting-started)
        -[Prerequsites](#prerequisites)
        -[Installation](#installation)
    - [Usage](#usage)
        - [Importing Modules](#importing-modules)
        - [Modules Aliasing](#module-aliasing)
        - [Importing All Objects](#importing-all-objects)
    - [Examples](#examples)
        - [Example 1: Basic Module Import](#example-1-basic-module-import)
        - [Example 2: Module Aliasing](#example-2-module-aliasing)
        - [Example 3: Importing Specific Objects](#example-3-importing-specific-objects)
        - [Example 4: Importing All Objects](#example-4-importing-all-objects)

## Introduction

Python is a versatile and powerful programming language that allows you to organize code into reusable modules. Modules are files containing python definitions and statements that can be imported into other python programs. By using modules, you can break your code into smaller, more manageable pieces, improve code readability and enhance overall project structure. This project aims to provide a comprehensive guide on importing modules in python. It covers various import techniques such as basic module imports, module aliasing, importing specific obejcts , and importing all obejcts from a module. Each tecnique is explained in detail, along with code examples to demonstrate their usage.

## Getting Started

### Prerequisites

To use this project, you need to have Python installed on your system. You can download the latest version of Python from the official website: [https://www.python.org/downloads]

### Installation

1. Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/your-repo.git
```

2. Navigate to the project directory:
```bash
cd your-repo
```
## Usage

This section provides an overview of different import techniques in python.

### Importing Modules
To import a module in python, you can use the `import` statement folllowed by the module name. For example:

```python
import module_name
```
This statement allows you to access the code and functions defined in the `module_name` module.

### Module Aliasing

Module Aliasing provides a way to refer to a module by a different name. It can be useful when the module name is long or conflicts with other names in your code. To alias a module, you can use the `as` keyword. For example:

```python
import module_name as alias
```
### Importing Specific objects

In addition to importing entire modules, you can also import specific objects(functions, classes or variables) from a module. This allows you to directly access those objects without referencing the module name. To import specific objects, ypou can use the `from` keyword followed by the module name and the object name. For example:

```python
from module_name import object_name
```
### Importing All Objects

Sometimes you may want to import all objects from a module without explicitly specifying each object. To achieve this, you can use the `*` wildcard character. For example:

```python
from module_name import *
```
However, it is generally recommended to import only specific objects or use module aliasing to prevent name clashes and make the code more readable.

## Examples

This section provides examples to illustrate the different import techniques discussed above.

### Example 1: Basic Module Import

```python
# Importing the math module
import math 

# Using the math module to calculate the square root of a number
result = math.sqrt(25)
print(result)
```

### Example 2: Module Aliasing

```python
# Importing the datetime module and aliasing it as dt
import datetime as dt

# Accessing the current date and time using the datetime module alias
current_time = dt.datetime.now()
print(current_time)
```

### Example 3: Importing Specific Objects

```python
# Importing only the randint function from the random module
from random import randint

# Generating a random number between 1 and 10 using thr imported function
random_number = randint(1, 10)
print(random_number)
```

### Example 4: Importing all Objects
```python
# Importing all objects from the statistics module
from statistics import *
# Calculating the mean of a list of numbers using the imported functions
numbers = [1,2,3,4,5]
mean_value = mean(numbers)
print(mean_value)
```