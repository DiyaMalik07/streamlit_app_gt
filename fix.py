import textwrap, re

with open('streamlit.py', 'r', encoding='utf-8') as f:
    code = f.read()

def dedent_str(m):
    return textwrap.dedent(m.group(0))

code = re.sub(r'f?\"\"\"[\s\S]*?\"\"\"', dedent_str, code)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(code)
