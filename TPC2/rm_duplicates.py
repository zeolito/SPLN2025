import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Remove duplicate lines from file(s) with extra options.')
    parser.add_argument('input_files', nargs='*', help='Path(s) to the input file(s). If omitted, reads from stdin.')
    parser.add_argument('-o', '--output_file', default=None, help='Path to the output file. If omitted, results are printed to stdout.')
    parser.add_argument('-s', '--keep-spaces', action='store_true', 
                        help='Keep the original spaces from each line. (Default: trim leading/trailing whitespace)')
    parser.add_argument('-e', '--remove-empty', action='store_true', 
                        help='Remove empty lines (lines that are empty or contain only whitespace).')
    parser.add_argument('-p', '--prefix-duplicate', action='store_true', 
                        help='Instead of removing duplicates, prefix them with a "#" to comment them out.')
    args = parser.parse_args()

    # Set to keep track of normalized (i.e. comparison) lines that have been seen.
    seen_lines = set()

    try:
        # Open output stream if an output file is specified, otherwise use stdout.
        outstream = open(args.output_file, 'w') if args.output_file else sys.stdout

        # Process each input file; if none provided, read from stdin.
        if args.input_files:
            for input_file in args.input_files:
                with open(input_file, 'r') as infile:
                    process_lines(infile, seen_lines, outstream, 
                                  keep_spaces=args.keep_spaces, 
                                  remove_empty=args.remove_empty, 
                                  prefix_duplicate=args.prefix_duplicate)
        else:
            process_lines(sys.stdin, seen_lines, outstream, 
                          keep_spaces=args.keep_spaces, 
                          remove_empty=args.remove_empty, 
                          prefix_duplicate=args.prefix_duplicate)

        if args.output_file:
            outstream.close()

    except IOError as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)

def process_lines(file_handle, seen_lines, outstream, keep_spaces, remove_empty, prefix_duplicate):
    for original_line in file_handle:
        # Normalize the line: if not keeping spaces, strip leading/trailing whitespace.
        normalized_line = original_line if keep_spaces else original_line.strip()

        # If removing empty lines, skip any line that is empty (or only whitespace).
        if remove_empty and normalized_line == '':
            continue

        if normalized_line not in seen_lines:
            seen_lines.add(normalized_line)
            # Output the original line if keeping spaces; otherwise output the normalized version.
            if keep_spaces:
                outstream.write(original_line)
            else:
                outstream.write(normalized_line + "\n")
        else:
            # Duplicate line detected.
            if prefix_duplicate:
                # Prefix with '#' and output the duplicate.
                if keep_spaces:
                    outstream.write("#" + original_line)
                else:
                    outstream.write("#" + normalized_line + "\n")
            # If not prefixing duplicates, do nothing (i.e. the duplicate is skipped).

if __name__ == '__main__':
    main()
