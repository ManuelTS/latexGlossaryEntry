# Creates a full Latex Glossary Entry (LGE) code by the arguments
import sys
import pyperclip

# Check arguments
if len(sys.argv) != 4:
    print("\nThree string arguments are required!\nFirst the words, second their abbreviation, and third their description but without the words and their abbreviation at the start.\n")
    sys.exit()

# Create string
abbrv = sys.argv[2].upper()
index = abbrv + "G"
first = sys.argv[1] + " " + "(" + abbrv + ") "

entry = "\\newglossaryentry{" + index + "}{\n" \
    "    name={" + abbrv + "},\n" \
    "    description={" + first + sys.argv[3] + "}\n" \
    "}\n" \
    "\\newglossaryentry{" + abbrv + "}{\n" \
    "    type=\\acronymtype,\n" \
    "    name={" + abbrv + "},\n" \
    "    description={" + sys.argv[1] + "},\n" \
    "    first={" + first +  "\\glsadd{" + index + "}},\n" \
    "    see=[Glossary:]{" + index + "}\n" \
    "}"

pyperclip.copy(entry)
print("\n" + entry + "\n")


