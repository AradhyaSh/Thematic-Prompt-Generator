import random
import streamlit as st

list_a = ["Endure", "Surrender", "Confront", "Evolve", "Defy", "Relinquish", "Avenge", "Submit", "Corrupt", "Redeem", "Destroy", "Consume", "Assimilate", "Isolate", "Sacrifice"]
list_b = ["Absurdism", "Dissonance", "Determinism", "Autonomy", "Complicity", "Hubris", "Apathy", "Altruism", "Dogma", "Paranoia", "Solipsism", "Martyrdom", "Alienation", "Ego", "Stoicism", "Narcissism", "Entropy", "Atonement", "Nihilism", "Hypocrisy"]
list_c = ["Acid Western", "Action Comedy", "Action Thriller", "Animal Horror", "Anime", "Apocalyptic", "Art House", "Avant-Garde", "Backstage Musical", "Biographical (Biopic)", "Biopunk", "Black Comedy", "Blaxploitation", "Body Horror", "Bromantic Comedy", "Buddy Cop", "Buddy Film", "Camp", "Caper", "Chambara", "Chick Flick", "Children's Film", "Cinema Verité", "Classic Western", "Comedy Horror", "Comedy of Errors", "Coming-of-Age", "Concert Film", "Conspiracy Thriller", "Contemporary Fantasy", "Cozy Mystery", "Crime Thriller", "Cyberpunk", "Dance Film", "Dark Fantasy", "Dark Humor", "Disaster Film", "Docudrama", "Domestic Drama", "Dystopian", "Elevated Horror", "Epic", "Epic Fantasy", "Erotic Romance", "Erotic Thriller", "Escape Room", "Espionage", "Essay Film", "Experimental", "Exploitation", "Fairy Tale", "Farce", "Feminist Film", "Financial Thriller", "First Contact", "Folk Horror", "Found Footage", "Giallo", "Girls with Guns", "Gothic Horror", "Gothic Romance", "Gore / Splatter", "Grindhouse", "Gun Fu", "Hard Sci-Fi", "Hardboiled", "Heist", "Heroic Bloodshed", "High Fantasy", "Historical Drama", "Historical Romance", "Holiday Movie", "Home Invasion", "Hood Film", "Idol Drama", "Independent (Indie)", "Integrated Musical", "Isekai", "Jukebox Musical", "Kaiju", "Kitchen Sink Realism", "Legal Drama", "Legal Thriller", "Locked-Room Mystery", "Low Fantasy", "Magical Realism", "Martial Arts", "Mecha", "Medical Drama", "Melodrama", "Military Fiction", "Mockumentary", "Mondo", "Monster Movie", "Mumblecore", "Mumblegore", "Musical Comedy", "Mystery Thriller", "Neo-Noir", "Neo-Western", "New French Extremity", "Noir", "Observational Documentary", "Ozploitation", "Paranormal Horror", "Paranormal Romance", "Parody / Spoof", "Period Piece", "Poetic Documentary", "Police Procedural", "Political Thriller", "Post-Apocalyptic", "Prison Break", "Propaganda", "Psychological Horror", "Psychological Thriller", "Pulp", "Revisionist Western", "Road Movie", "Romantic Comedy (Rom-Com)", "Romantic Drama", "Romantic Fantasy", "Romantic Thriller", "Samurai Cinema", "Satire", "Science Fantasy", "Screwball Comedy", "Sexploitation", "Shoot 'em up", "Slapstick", "Slasher", "Slice of Life", "Snuff (Fictional)", "Social Problem Film", "Soft Sci-Fi", "Space Opera", "Space Western", "Spaghetti Western", "Splatterpunk", "Sports Drama", "Spy Film", "Steampunk", "Stoner Comedy", "Supernatural Horror", "Superhero Film", "Surrealist Film", "Survival Film", "Survival Horror", "Sword and Sandal", "Sword and Sorcery", "Tech Noir", "Techno-Horror", "Techno-Thriller", "Teen Drama", "Time Travel", "Tokusatsu", "Tragedy", "Tragicomedy", "Urban Fantasy", "Vampire Film", "War Drama", "Weird West", "Werewolf Film", "Whodunit", "Wuxia", "Zombie Comedy", "Zombie Film"]

# UI Element: Main Title
st.title("Thematic Prompt Generator")

# UI Element: Interactive Button & Conditional Logic
if st.button("Generate"):
    word_a = random.choice(list_a)
    word_b = random.choice(list_b)
    word_c = random.choice(list_c)

    vowels = ["A", "E", "I", "O", "U"]
    determiner = "an" if word_c[0].upper() in vowels else "a"

    prompt = f"{word_a} {word_b} in {determiner} {word_c} setting."
    
    # UI Element: Render the final string to the screen in a green success box
    st.success(prompt)