"""
ESCAPE sybols
+------------+-------------------------------+------------------------------+-------------------+
| \newline   | Backslash and newline ignored | print("line1 \               | line1 line2 line3 |
|            |                               | line2 \                      |                   |
|            |                               | line3")                      |                   |
+------------+-------------------------------+------------------------------+-------------------+
| \\         | Backslash (\)                 | print("\\")                  | \                 |
+------------+-------------------------------+------------------------------+-------------------+
| \'         | Single quote (')              | print('\'')                  | '                 |
+------------+-------------------------------+------------------------------+-------------------+
| \"         | Double quote (")              | print("\"")                  | "                 |
+------------+-------------------------------+------------------------------+-------------------+
| \a         | ASCII Bell (BEL)              | print("\a")                  | SOUND             |
+------------+-------------------------------+------------------------------+-------------------+
| \t         | ASCII Horizontal Tab (TAB)    | print("Hello \t World!")     | Hello      World! |
+------------+-------------------------------+------------------------------+-------------------+
| \b         | ASCII Backspace (BS)          | print("Hello \b World!")     | Hello World!      |
+------------+-------------------------------+------------------------------+-------------------+
| \n         | ASCII Linefeed (LF)           | print("Hello \n World!")     | Hello             |
|            |                               |                              |  World!           |
+------------+-------------------------------+------------------------------+-------------------+
"""

t = "lkfdjhgrleiuhg;ifdjhg;iofdhg;foihg;oeirhge;roihgreo'ihjreo'ij'oife'oie" \
    "jre'eo'i;ouire\ahgpuireqhg98preytp54yhgvin54tph8wng45p]8rhgpwntgbput5wn[" \
    "hr;g;rt8owhjgjg[q45hj[g9hg9b54[iioh[b9oj[hbqt4hg9qj4]g90jgqhjv[9hq54b9[8"

print(t)
print('\\')

t = 'iuertiuw\'etuiweo'
print(t)

t = 'hgilhb5"4yt98'
print(t)

print("Hello\tWorld!")

print("Hello \n World!")