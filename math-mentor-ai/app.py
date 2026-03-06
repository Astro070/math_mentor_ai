from utils.math_solver import solve_math
from utils.ocr import extract_text_from_image
from utils.audio_to_text import transcribe_audio
from agents.parser_agent import parse_question
from agents.router_agent import route_problem
from agents.verifier_agent import verify_solution
from agents.explainer_agent import generate_explanation
from rag.retriever import retrieve_context
from memory.memory_store import store_memory, search_memory
from memory.feedback_store import store_feedback   # ===== USER FEEDBACK SYSTEM =====

import streamlit as st

# ===== MAIN HEADER UI =====
st.set_page_config(page_title="AI Math Mentor", layout="wide")

st.title("AI Math Mentor")

st.markdown(
    "An AI-powered tutor that solves math problems using **Agents + RAG + Memory**."
)

st.divider()
# ===== SIDEBAR SYSTEM PANEL =====
st.sidebar.title("AI Math Mentor")

st.sidebar.header("Input Modes")
st.sidebar.write("✔ Text")
st.sidebar.write("✔ Image")
st.sidebar.write("✔ Audio")

st.sidebar.header("AI System Status")
st.sidebar.write("✔ Parser Agent Active")
st.sidebar.write("✔ Router Agent Active")
st.sidebar.write("✔ Solver Agent Active")
st.sidebar.write("✔ Verifier Agent Active")
st.sidebar.write("✔ Explainer Agent Active")

st.sidebar.header("AI Capabilities")
st.sidebar.write("✔ RAG Knowledge Retrieval")
st.sidebar.write("✔ Memory System")
st.sidebar.write("✔ Human-in-the-loop")
st.sidebar.write("✔ User Feedback System")
st.write("Welcome! Ask a math question.")

input_mode = st.selectbox(
    "Select Input Type",
    ["Text", "Image", "Audio"]
)

# ---------------- TEXT INPUT MODE ----------------
if input_mode == "Text":

    question = st.text_input("Enter your math question")

    if st.button("Solve"):

        # ===== MEMORY CHECK =====
        memory_result = search_memory(question)

        if memory_result:
            st.subheader("Retrieved From Memory")
            st.write(memory_result)

        else:

            # Parser Agent
            parsed = parse_question(question)

            st.subheader("Parsed Problem")
            st.json(parsed)

            # Router Agent
            route = route_problem(parsed)

            st.write("Routing Decision:", route)

            # RAG Retrieval
            context = retrieve_context(question)

            st.subheader("Retrieved Knowledge")
            st.write(context)

            # Solver Agent
            answer = solve_math(parsed["problem_text"])

            # Store result in memory
            store_memory(question, answer)

            # Verifier Agent
            verification = verify_solution(question, answer)

            st.subheader("Verification Result")
            st.json(verification)

            # ===== CONFIDENCE INDICATOR =====
            confidence = verification["confidence"]

            if confidence == "HIGH":
                st.success("Confidence Level: HIGH")
            elif confidence == "MEDIUM":
                st.warning("Confidence Level: MEDIUM")
            else:
                st.error("Confidence Level: LOW")

            # ===== HUMAN-IN-THE-LOOP =====
            if confidence == "LOW":

                st.warning("AI confidence is LOW. Please verify.")

                approve = st.button("Approve Answer")
                retry = st.button("Retry Solving")

                if approve:
                    st.subheader("Final Answer")
                    st.write(verification["verified_answer"])

                elif retry:
                    retry_answer = solve_math(parsed["problem_text"])
                    st.subheader("Retry Result")
                    st.write(retry_answer)

            else:

                # Explainer Agent
                explanation = generate_explanation(
                    question,
                    verification["verified_answer"]
                )

                st.subheader("Step-by-Step Explanation")

                for step in explanation:
                    st.write(step)

                st.subheader("Final Answer")
                st.write(verification["verified_answer"])

            # ===== AGENT TRACE PANEL =====
            st.subheader("Agent Trace")

            agent_trace = [
                "Parser Agent",
                "Router Agent",
                "RAG Retriever",
                "Solver Agent",
                "Verifier Agent",
                "Explainer Agent"
            ]

            for agent in agent_trace:
                st.write("✔", agent)

            # ===== USER FEEDBACK SYSTEM =====
            st.subheader("User Feedback")

            feedback = st.radio(
                "Was this answer correct?",
                ["Correct", "Incorrect"]
            )

            comment = st.text_input("Optional comment")

            if st.button("Submit Feedback"):

                store_feedback(
                    question,
                    verification["verified_answer"],
                    feedback,
                    comment
                )

                st.success("Feedback stored successfully!")


# ---------------- IMAGE INPUT MODE ----------------
elif input_mode == "Image":

    uploaded_file = st.file_uploader("Upload math problem image")

    if uploaded_file:

        st.image(uploaded_file)

        # OCR extraction
        extracted_text, ocr_conf = extract_text_from_image(uploaded_file)

        st.subheader("Extracted Question (OCR)")

        # User can edit extracted text
        edited_text = st.text_area(
            "Edit extracted text if needed",
            extracted_text,
            height=120
        )

        # HITL warning if OCR confidence low
        if ocr_conf < 0.6:
            st.warning(
                f"OCR confidence is low ({ocr_conf:.2f}). Please review the extracted text."
            )

        # Retrieve knowledge using edited text
        context = retrieve_context(edited_text)

        st.subheader("Retrieved Knowledge")
        st.write(context)

        if st.button("Solve Image Question"):

            answer = solve_math(edited_text)

            store_memory(edited_text, answer)

            st.subheader("Answer")
            st.write(answer)
    


# ---------------- AUDIO INPUT MODE ----------------
elif input_mode == "Audio":

    audio_file = st.file_uploader("Upload audio question")

    if audio_file:

        st.audio(audio_file)

        # Speech-to-text
        transcript = transcribe_audio(audio_file)

        st.subheader("Transcript (Editable)")

        # Allow user to edit transcript (Human-in-the-loop)
        edited_transcript = st.text_area(
            "Edit transcript if needed",
            transcript,
            height=120
        )

        # RAG retrieval using edited text
        context = retrieve_context(edited_transcript)

        st.subheader("Retrieved Knowledge")
        st.write(context)

        if st.button("Solve Audio Question"):

            answer = solve_math(edited_transcript)

            store_memory(edited_transcript, answer)

            st.subheader("Answer")
            st.write(answer)