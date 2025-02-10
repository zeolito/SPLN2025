import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Filter out repeated lines from a file.')
    parser.add_argument('input_file', help='Path to the input file.')
    parser.add_argument('output_file', nargs='?', default=None,
                        help='(Optional) Path to the output file. If omitted, results are printed to stdout.')
    parser.add_argument('output_file', nargs='?', default=None,
                        help='(Optional) Path to the output file. If omitted, results are printed to stdout.')
    parser.add_argument('--count', '-c', action='store_true',
                        help='Prepend each output line with the count of its occurrences.')
    args = parser.parse_args()

    seen_line = set()
    seen_dict = {}

    try:
        with open(args.input_file, 'r') as infile:
            if args.output_file:
                outstream = open(args.output_file, 'w')
            else:
                outstream = sys.stdout

            if args.count:
                for line in infile:
                    if line not in seen_dict:
                        seen_dict[line] = 0
                    else:
                        seen_dict[line] = seen_dict[line] + 1

                for line, count in seen_dict.items():
                    if count > 0:
                        final = (str(count) + ": " + line)
                    else:
                        final =line
                    outstream.write(final)
            else:
                for line in infile:
                    if line not in seen_line:
                        outstream.write(line)
                        seen_line.add(line)

            if args.output_file:
                outstream.close()

    except IOError as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)

if __name__ == '__main__':
    main()
