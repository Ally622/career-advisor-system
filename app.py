import streamlit as st

# ---------------------------
# Career Advisor Expert System
# ---------------------------

# Title
st.set_page_config(page_title="Career Advisor", page_icon="🎯")
st.title("🎯 Career Advisor Expert System")
st.write("Select your interests, skills, and preferences to get a recommended career path.")

# ---------------------------
# Define careers and rules
# ---------------------------

careers = [
    "Software Engineer",
    "Data Analyst",
    "Civil Engineer",
    "Accountant",
    "Graphic Designer"
]

rules = [
    # Software Engineer Rules
    {"career": "Software Engineer", "conditions": ["likes_programming", "likes_math", "good_at_problem_solving"]},
    {"career": "Software Engineer", "conditions": ["likes_programming", "interested_in_computers", "enjoys_independent_work"]},
    {"career": "Software Engineer", "conditions": ["likes_programming", "likes_math", "good_at_critical_thinking"]},

    # Data Analyst Rules
    {"career": "Data Analyst", "conditions": ["likes_statistics", "likes_math", "good_at_analysis"]},
    {"career": "Data Analyst", "conditions": ["interested_in_data", "likes_numbers", "good_at_analysis"]},
    {"career": "Data Analyst", "conditions": ["likes_statistics", "good_at_critical_thinking", "prefers_indoor_work"]},

    # Civil Engineer Rules
    {"career": "Civil Engineer", "conditions": ["likes_math", "likes_building", "prefers_field_work"]},
    {"career": "Civil Engineer", "conditions": ["likes_building", "enjoys_teamwork", "prefers_field_work"]},
    {"career": "Civil Engineer", "conditions": ["likes_math", "enjoys_teamwork", "prefers_field_work"]},

    # Accountant Rules
    {"career": "Accountant", "conditions": ["likes_numbers", "likes_accounting", "prefers_indoor_work"]},
    {"career": "Accountant", "conditions": ["likes_accounting", "good_at_analysis", "enjoys_independent_work"]},
    {"career": "Accountant", "conditions": ["likes_numbers", "good_at_critical_thinking", "prefers_indoor_work"]},

    # Graphic Designer Rules
    {"career": "Graphic Designer", "conditions": ["likes_design", "likes_drawing", "good_at_creativity"]},
    {"career": "Graphic Designer", "conditions": ["likes_design", "interested_in_design_tools", "enjoys_independent_work"]},
    {"career": "Graphic Designer", "conditions": ["likes_drawing", "good_at_creativity", "prefers_indoor_work"]},
]

# ---------------------------
# Define all possible facts
# ---------------------------

all_facts = [
    "likes_programming", "likes_math", "likes_statistics", "likes_design", "likes_drawing",
    "likes_building", "likes_numbers", "likes_accounting",
    "good_at_problem_solving", "good_at_analysis", "good_at_creativity", "good_at_critical_thinking",
    "prefers_indoor_work", "prefers_field_work", "enjoys_teamwork", "enjoys_independent_work",
    "interested_in_computers", "interested_in_data", "interested_in_design_tools"
]

# Friendly labels for display
fact_labels = {
    "likes_programming": "I like programming",
    "likes_math": "I like math",
    "likes_statistics": "I like statistics",
    "likes_design": "I like design",
    "likes_drawing": "I like drawing",
    "likes_building": "I like building/construction",
    "likes_numbers": "I like working with numbers",
    "likes_accounting": "I like accounting",
    "good_at_problem_solving": "I am good at problem solving",
    "good_at_analysis": "I am good at analysis",
    "good_at_creativity": "I am creative",
    "good_at_critical_thinking": "I have good critical thinking",
    "prefers_indoor_work": "I prefer indoor work",
    "prefers_field_work": "I prefer field work",
    "enjoys_teamwork": "I enjoy teamwork",
    "enjoys_independent_work": "I enjoy independent work",
    "interested_in_computers": "I am interested in computers",
    "interested_in_data": "I am interested in data",
    "interested_in_design_tools": "I am interested in design tools"
}

# ---------------------------
# User input
# ---------------------------

st.subheader("Select your facts:")
user_facts = st.multiselect(
    "Pick all that apply:",
    options=all_facts,
    format_func=lambda x: fact_labels[x]
)

# ---------------------------
# Career recommendation logic
# ---------------------------

career_scores = {career: 0 for career in careers}

for rule in rules:
    match_count = sum([1 for cond in rule["conditions"] if cond in user_facts])
    if match_count == len(rule["conditions"]):
        career_scores[rule["career"]] += match_count

# ---------------------------
# Display recommendation
# ---------------------------

st.subheader("Recommended Career:")

if any(score > 0 for score in career_scores.values()):
    recommended = max(career_scores, key=career_scores.get)
    st.success(f"🎉 You should consider a career as a **{recommended}**!")
else:
    st.info("⚠️ No recommendation could be made. Try selecting more facts.")

# Optional: Show all scores for transparency
with st.expander("See career scores"):
    for career, score in career_scores.items():
        st.write(f"{career}: {score}")
