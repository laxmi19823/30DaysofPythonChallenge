# app.py (Streamlit UI)
import streamlit as st
from utils import load_questions, evaluate_answer
from style import set_background, custom_success, custom_warning, apply_custom_styles

set_background("bg.png")
apply_custom_styles()


# --- App Logic ---
data = load_questions()

st.markdown("""
    <h1 style='color: white; text-align: center;'>💼 InterviewMate</h1>
    <p style='color: white; text-align: center;'>Get Interview Ready with InterviewMate</p>
""", unsafe_allow_html=True)


# --- Select Category ---
categories = list(data.keys())
selected_category = st.selectbox("Choose a category:", categories)

# --- Select Topic within the chosen category ---
topics = list(data[selected_category].keys())
selected_topic = st.selectbox("Choose a topic:", topics)

# --- Load Questions ---
questions = data[selected_category][selected_topic]
total_questions = len(questions)

# --- Session state to track progress ---
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.show_feedback = False
    st.session_state.last_result = {}

# Show current question
if st.session_state.index < total_questions:
    qa = questions[st.session_state.index]
    st.markdown(f"<h3 style='color: white;'>Q{st.session_state.index + 1}: {qa['q']}</h3>", unsafe_allow_html=True)
    user_input = st.text_area("Your Answer:", key=st.session_state.index)

    if st.button("Submit Answer"):
        matched, total = evaluate_answer(user_input, qa.get("keywords", []))
        st.session_state.last_result = {
            "matched": matched,
            "total": total,
            "correct_answer": qa["a"],
            "was_correct": (total > 0 and matched / total >= 0.6)
        }
        if st.session_state.last_result["was_correct"]:
            st.session_state.score += 1
        st.session_state.show_feedback = True

    if st.session_state.show_feedback:
        res = st.session_state.last_result
        st.markdown(f"<p style='color: white;'>✅ Correct Answer: {res['correct_answer']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: white;'>🔍 Keywords matched: {res['matched']}/{res['total']}</p>", unsafe_allow_html=True)

        if res["was_correct"]:
            custom_success("🟢Excellent! This answer meets the expected criteria.")
        else:
            custom_warning("🟠 “Needs more depth. Try adding relevant keywords.")

        if st.button("Next Question"):
            st.session_state.index += 1
            st.session_state.show_feedback = False
            st.rerun()
else:
    custom_success(
    f"That’s the end of your interview session for the topic <b>{selected_topic}</b>.<br>"
    f"Hope the questions were helpful in getting you interview ready!"
)

    st.markdown(
    f"<p style='color: white; font-size: 18px;'>You answered <b>{st.session_state.score}</b> out of <b>{total_questions}</b> questions correctly. </p>",
    unsafe_allow_html=True
)



    if st.button("Practice Again"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.show_feedback = False
        st.rerun()
