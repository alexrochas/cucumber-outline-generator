import sys
import re
from itertools import chain

user_input = ' '.join([line for line in sys.stdin])

pattern = re.compile("<(.*)>")

columns = pattern.findall(user_input)

formatted_columns = "|".join(chain(('', ), [column + '\t' for column in columns], ('', )))
empty_spaces = "|".join(chain(('', ), ['\t' for column in columns], ('', )))

print formatted_columns
print empty_spaces
