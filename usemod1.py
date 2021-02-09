from bigloans.misc import financials
import sys

financials.spam()
financials.ham()
for color in financials.COLORS:
    print(color)

for path in sys.path:
    print(path)
