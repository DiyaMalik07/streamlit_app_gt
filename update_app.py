import os

app_file = r"c:\Users\diyam\Documents\College\SEM 4\Graph Theory\Lab\Codes\app.py"
with open(app_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if i == 0:
        new_lines.append("import streamlit as st\nimport os\nimport re\n")
        continue
    if "import streamlit as st" in line:
        continue
        
    if "with col2:" in line:
        new_lines.append(line)
        new_lines.append('    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/Goa_College_of_Engineering_logo.png/250px-Goa_College_of_Engineering_logo.png", width=120)\n')
        skip = True
        continue
    
    if skip and "st.divider()" in line:
        skip = False
        
    if "st.sidebar.header(\"Navigation\")" in line:
        new_lines.append(line)
        
        dynamic_code = """
current_dir = os.path.dirname(os.path.abspath(__file__))
all_files = [f for f in os.listdir(current_dir) if f.endswith('.py') and f not in ('app.py', 'get_logo.py', 'update_app.py', 'tempCodeRunnerFile.py')]

def sort_key(f):
    nums = re.findall(r'\d+', f)
    return int(nums[0]) if nums else f

all_files.sort(key=lambda x: (sort_key(x), x))

experiment = st.sidebar.selectbox(
    "Select an Experiment:",
    all_files
)
"""
        new_lines.append(dynamic_code)
        skip = True
        continue
        
    if skip and "def run_and_display_code(" in line:
        skip = False
        
    if not skip and "if experiment ==" in line:
        # replace the if experiment == ... block with dynamic running
        dynamic_run = """
if experiment:
    st.header(f"🔬 Selected: {experiment}")
    
    file_path = os.path.join(current_dir, experiment)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code_content = f.read()
            
        st.header("💻 Source Code")
        st.code(code_content, language="python")
        
        st.header("📊 Output")
        output = run_and_display_code(code_content)
        if output:
            st.code(output, language="text")
        else:
            st.info("No output returned.")
    except Exception as e:
        st.error(f"Error reading file: {e}")
"""
        new_lines.append(dynamic_run)
        skip = True
        continue
        
    if skip and "4. FOOTER" in line:
        skip = False
        
    if not skip:
        new_lines.append(line)

with open(app_file, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
