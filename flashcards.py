import streamlit as st

st.title("🧠 Flashcard Study App")

# Flashcard list
flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 7 x 8?", "answer": "56"},
    {"question": "Who discovered penicillin?", "answer": "Alexander Fleming"},
    {"question": "What does DNA stand for?", "answer": "Deoxyribonucleic acid"},
]

# Initialise session state
if "card_index" not in st.session_state:
    st.session_state.card_index = 0
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

# Buttons to navigate
col1, col2 = st.columns(2)
with col1:
    if st.button("⬅️ Previous"):
        if st.session_state.card_index > 0:
            st.session_state.card_index -= 1
            st.session_state.show_answer = False
with col2:
    if st.button("➡️ Next"):
        if st.session_state.card_index < len(flashcards) - 1:
            st.session_state.card_index += 1
            st.session_state.show_answer = False

# Display the current flashcard
card = flashcards[st.session_state.card_index]
st.subheader(f"Question {st.session_state.card_index + 1} of {len(flashcards)}")
st.write(card["question"])

# Toggle answer
if st.session_state.show_answer:
    st.markdown(f"**Answer:** {card['answer']}")
else:
    if st.button("👀 Show Answer"):
        st.session_state.show_answer = True
