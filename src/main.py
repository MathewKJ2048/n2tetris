# hack preprocessing
import snippets
import config
import argparse
import syntax


def process(line):

    if len(line) == 0:
        return line
    if line[0] == syntax.directive:
        tokens = line[0:-1].split(" ")
        print(tokens)
        if tokens[1] == syntax.terminate:
            return snippets.terminate()
        elif tokens[1] == syntax.stack:
            return snippets.stack(tokens[2])
        elif tokens[1] == syntax.call:
            return snippets.call(tokens[2])
        elif tokens[1] == syntax.return_:
            return snippets.return_snippet()
        elif tokens[1] == syntax.push:
            return snippets.push(tokens[2])
        elif tokens[1] == syntax.pop:
            return snippets.pop(tokens[2])
        elif tokens[1] == syntax.goto:
            return snippets.goto(tokens[2])
        elif tokens[1][0] == syntax.M:
            if len(tokens) == 6:
                return snippets.general_operation(tokens[1], tokens[3], tokens[4], tokens[5])
            else:
                return snippets.general_assignment(tokens[1], tokens[3])
        elif tokens[1] == syntax.branch:
            return snippets.branch(tokens[2],tokens[3],tokens[4],tokens[5])
        else:
            print("Error - unrecognized directive")
            return "Error"
    else:
        return line
    pass



def create_and_write_file(input_file_path, output_file_path):
    try:
        # Open the input file for reading
        with open(input_file_path, 'r') as input_file:
            # Read lines from the input file, append '|' to each line, and join them
            lines = input_file.readlines()
            modified_lines = []
            for i in range(len(lines)):
                modified_lines.append(process(lines[i]))

        

        # Open the output file for writing (overwriting if it exists)
        with open(output_file_path, 'w') as output_file:
            # Write the modified lines to the output file with the original line separator
            output_file.write(''.join(modified_lines))

        print(f"Contents of {input_file_path} were processed and written to {output_file_path}")
    except FileNotFoundError:
        print(f"Error: File not found - {input_file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Process and write file contents with '|' separator.")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file (will be created/overwritten)")

    args = parser.parse_args()
    create_and_write_file(args.input_file, args.output_file)

if __name__ == "__main__":
    main()



