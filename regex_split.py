regex_pattern = r"(?<=\d)[,.](?=\d)"

import re
print("\n".join(re.split(regex_pattern, input())))
