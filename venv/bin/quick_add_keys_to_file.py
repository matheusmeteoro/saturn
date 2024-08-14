#!/home/meteoro/Documentos/saturn/venv/bin/python
# -*- coding: utf-8 -*-
import re
import sys
from msumastro.scripts.quick_add_keys_to_file import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
