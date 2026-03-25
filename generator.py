import random
import streamlit as st

# 1. Data Ingestion Function
def load_list(filename):
    try:
        # 'r' strictly opens the file in read-only mode to prevent accidental deletion
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        # Error handling prevents the server from crashing silently
        st.error(f"Critical Failure: {filename} not found.")
        return []

# 2. Variable Assignment via File Extraction
list_a = load_list("list_a.txt")
list_b = load_list("list_b.txt")
list_c = load_list("list_c.txt")

# 3. Session State Initialization
if 'history' not in st.session_state:
    st.session_state.history = {}

st.title("Thematic Prompt Generator")

# 4. Execution Firewall
# Stops the script immediately if the text files are missing or empty
if not list_a or not list_b or not list_c:
    st.stop()

if st.button("Generate"):
    word_a = random.choice(list_a)
    word_b = random.choice(list_b)
    word_c = random.choice(list_c)

    vowels = ["A", "E", "I", "O", "U"]
    determiner = "an" if word_c[0].upper() in vowels else "a"

    raw_prompt = f"{word_a} {word_b} in {determiner} {word_c} setting."

    base_prompt = raw_prompt.capitalize()

    if base_prompt in st.session_state.history:
        st.session_state.history[base_prompt] += 1
        final_output = f"{base_prompt} ({st.session_state.history[base_prompt]})"
    else:
        st.session_state.history[base_prompt] = 0
        final_output = base_prompt
        
    st.success(final_output)
