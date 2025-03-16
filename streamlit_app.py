import streamlit as st

st.title("🎈 My new app")
st.write(
# פונקציה לטעינת הנתונים מה-Session
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("📅 אפליקציית תזכורות לעבודה – מובייל")

# הוספת משימה חדשה
st.subheader("➕ הוספת תזכורת חדשה")
task_name = st.text_input("שם המשימה:")
task_date = st.date_input("📅 תאריך", datetime.date.today())
task_time = st.time_input("⏰ שעה")

if st.button("💾 הוסף תזכורת"):
    if task_name:
        st.session_state.tasks.append({"משימה": task_name, "תאריך": task_date, "שעה": task_time, "הושלם": False})
        st.success("✅ התזכורת נוספה בהצלחה!")
    else:
        st.warning("⚠️ אנא הזן שם משימה.")

# הצגת רשימת המשימות
st.subheader("📋 התזכורות שלך")
for task in st.session_state.tasks:
    col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
    col1.write(f"📝 {task['משימה']}")
    col2.write(f"📅 {task['תאריך']}")
    col3.write(f"⏰ {task['שעה']}")
    completed = col4.checkbox("✔️", value=task["הושלם"], key=task["משימה"])
    
    if completed:
        task["הושלם"] = True

# מחיקת משימות שהושלמו
if st.button("🗑️ מחק משימות שהושלמו"):
    st.session_state.tasks = [task for task in st.session_state.tasks if not task["הושלם"]]
    st.success("🗑️ המשימות שהושלמו נמחקו!")
    st.experimental_rerun()
)
