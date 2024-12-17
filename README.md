# Stream Decorator System

This Python project demonstrates the Decorator design pattern by enhancing a basic output stream with various decorators. The decorators dynamically add features to the stream, such as numbering lines, adding brackets, duplicating output to multiple streams, and filtering lines based on conditions.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Overview](#project-overview)
4. [Key Features](#key-features)
5. [Purpose and Lessons Learned](#purpose-and-lessons-learned)

## Installation

To set up and run this project locally:

1. **Clone the Repository:**  
```bash
git clone https://github.com/alex-nin/decorator-design-pattern.git
cd decorator-design-pattern
```
2. **Install Dependencies:** Ensure you have Python 3.x installed.

## Usage

To run the program, execute the following command in your terminal in the program directory, depending on your Python environment:

```bash
python decorator.py
```
or
```bash
python3 decorator.py
```

## Project Overview

The main components include:
- **Output Interface:** An abstract base class for all output streams, defining the `write` method.
- **StreamOutput:** A concrete output class that writes data to a specified stream (like `sys.stdout`).
- **Output Decorators:** In the program, you can chain decorators to modify the stream’s behavior:
    - **BracketOutput:** Wraps each line with brackets.
    - **NumberedOutput:** Adds line numbers to each line of output.
    - **TeeOutput:** Sends the output to multiple streams.
    - **FilterOutput:** Filters output based on a provided condition.

Each decorator inherits from `OutputDecorator`, allowing dynamic, layered modifications to the output stream.

## Key Features

1. **Dynamic Stream Enhancement:** Each decorator enhances the output stream without altering the original `StreamOutput` class.
2. **Flexible Layering:** Multiple decorators can be layered to combine functionalities, such as numbering and bracket-wrapping output lines.
3. **Output Duplication:** Using `TeeOutput`, data can be written to two different streams, enabling multi-destination logging.
4. **Conditional Output:** `FilterOutput` selectively processes lines, adding functionality based on user-defined conditions.

## Purpose and Lessons Learned

This project gave me hands-on experience with the Decorator design pattern, showing how it can add functionality to objects dynamically. By implementing multiple decorators, I learned how decorators can be layered to create flexible, reusable components. This approach made it easy to extend functionality without modifying existing code, highlighting the Decorator pattern’s value in building adaptable and maintainable systems.
