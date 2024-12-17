from abc import ABC, abstractmethod
import sys

class Output(ABC):
    """Abstract base class for output stream."""

    @abstractmethod
    def write(self, data):
        pass


class StreamOutput(Output):
    """Concrete class that writes to a provided stream."""

    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(str(data))


class OutputDecorator(Output):
    """Base decorator class for output streams."""

    def __init__(self, decorated: Output):
        self.decorated = decorated

    @abstractmethod
    def write(self, data):
        pass


class BracketOutput(OutputDecorator):

    def write(self, data):
        self.decorated.write(f"[{data.strip()}]\n")


class NumberedOutput(OutputDecorator):

    def __init__(self, decorated: Output):
        super().__init__(decorated)
        self.line_number = 1

    def write(self, data):
        formatted_line = f"{self.line_number:5d}: {data}"
        self.line_number += 1
        self.decorated.write(formatted_line)


class TeeOutput(OutputDecorator):

    def __init__(self, decorated: Output, second_output: Output):
        super().__init__(decorated)
        self.second_output = second_output

    def write(self, data):
        self.decorated.write(data)
        self.second_output.write(data)


class FilterOutput(OutputDecorator):

    def __init__(self, decorated: Output, predicate):
        super().__init__(decorated)
        self.predicate = predicate

    def write(self, data):
        if self.predicate(data):
            self.decorated.write(data)


def contains_digit(s):
    """Returns True if the string contains any digit."""
    return any(char.isdigit() for char in s)


def longer_than_5_chars(s):
    """Returns True if the string is longer than 5 characters."""
    return len(s.strip()) > 5

def main():
    file_name = "decorator.dat"
    tee_file = None

    try:
        with open(file_name, 'r') as input_file:
            lines = input_file.readlines()

        output = StreamOutput(stream=sys.stdout)

        done = False
        while not done:
            print("Select output decorator:")
            print("1. BracketOutput")
            print("2. NumberedOutput")
            print("3. TeeOutput")
            print("4. FilterOutput")
            print("5. Exit")

            selection = input("Selection: ")

            if selection == '1':
                output = BracketOutput(output)
            elif selection == '2':
                output = NumberedOutput(output)
            elif selection == '3':
                tee_file_name = input("Enter the Tee output file name: ")
                tee_file = open(tee_file_name, 'w')
                file_output = StreamOutput(tee_file)
                output = TeeOutput(output, file_output)
            elif selection == '4':
                print("Choose a filter:")
                print("1. Contains digit")
                print("2. Longer than 5 characters")
                filter_choice = input("Selection: ")

                if filter_choice == '1':
                    output = FilterOutput(output, contains_digit)
                elif filter_choice == '2':
                    output = FilterOutput(output, longer_than_5_chars)
                else:
                    print("Invalid filter selection!")
            elif selection == '5':
                done = True
            else:
                print("Invalid selection!")

        for line in lines:
            output.write(line)

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if tee_file:
            tee_file.close()


if __name__ == "__main__":
    main()