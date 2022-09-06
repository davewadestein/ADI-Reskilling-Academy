import sys
import code_runner, parser

# Check for command line argument representing file of code to open
if len(sys.argv) < 2:
    print("No code file to open!")
    sys.exit(1)

code = parser.parse(sys.argv[1])
code_runner.run_code(code)
