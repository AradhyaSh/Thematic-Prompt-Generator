import random
import streamlit as st

def load_list(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        st.error(f"Critical Failure: {filename} not found.")
        return []

# Helper function to assign the correct determiner
def get_article(word):
    vowels = ["A", "E", "I", "O", "U"]
    return "an" if word[0].upper() in vowels else "a"

# Helper function to dynamically conjugate verbs for singular subjects
def conjugate_verb(verb):
    verb = verb.strip()
    vowels = ["a", "e", "i", "o", "u"]
    
    if verb.endswith('y'):
        if verb[-2].lower() not in vowels:
            return verb[:-1] + "ies"  # Defy -> Defies
        else:
            return verb + "s"         # Destroy -> Destroys
    elif verb.endswith(('sh', 'ch', 's', 'x', 'z')):
        return verb + "es"            # Relinquish -> Relinquishes
    else:
        return verb + "s"             # Endure -> Endures

list_a = load_list("list_a.txt")
list_b = load_list("list_b.txt")
list_c = load_list("list_c.txt")
list_d = load_list("list_d.txt")
list_e = load_list("list_e.txt")

if 'history' not in st.session_state:
    st.session_state.history = {}

st.title("Thematic Prompt Generator")

if not all([list_a, list_b, list_c, list_d, list_e]):
    st.stop()

if st.button("Generate"):
    # 1. Determine Character Count (1 or 2)
    num_chars = random.choice([1, 2])
    
    # 2. Extract traits without replacement to prevent repetition
    adjectives = random.sample(list_d, num_chars)
    professions = random.sample(list_e, num_chars)
    
    word_a = random.choice(list_a)
    word_b = random.choice(list_b)
    word_c = random.choice(list_c)

# 3. Construct Character String and Conjugate Verb
    # Do not capitalize the article here; it is mathematically redundant now.
    char1 = f"{get_article(adjectives[0])} {adjectives[0]} {professions[0]}"
    
    if num_chars == 2:
        char2 = f"and {get_article(adjectives[1])} {adjectives[1]} {professions[1]}"
        subject = f"{char1} {char2}"
        verb = word_a  
    else:
        subject = char1
        verb = conjugate_verb(word_a)  
        
    genre_phrase = f"in {get_article(word_c)} {word_c} setting."
    
    # 4. Compile the final syntax and enforce sentence case
    # The .lower() on the verb is removed as the capitalization method handles it automatically
    raw_prompt = f"{subject} {verb} {word_b} {genre_phrase}"
    base_prompt = raw_prompt.capitalize()
    
    if base_prompt in st.session_state.history:
        st.session_state.history[base_prompt] += 1
        final_output = f"{base_prompt} ({st.session_state.history[base_prompt]})"
    else:
        st.session_state.history[base_prompt] = 0
        final_output = base_prompt
        
    st.success(final_output)
