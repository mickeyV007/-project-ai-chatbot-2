import streamlit as st
from backend import ChatbotBackend
from datetime import datetime

st.set_page_config(page_title="Chat AI", page_icon="💬", layout="wide")

# ตรวจสอบว่า session state มี chatbot และ chat history หรือยัง
if "chatbot" not in st.session_state:
    st.session_state.chatbot = ChatbotBackend("phi3")  # chatbot model ที่ใช้รองรับภาษาไทย
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# เพิ่ม Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()
    st.markdown("---")
    st.write("🔹 **Chat AI** by Streamlit")

# ฟังก์ชันสำหรับแสดงหัวข้อแชท
def get_chat_header():
    return f"💬 Chat AI"

# แสดงหัวข้อแชทให้อยู่ตรงกลางและมีสีพื้นหลัง
st.markdown(f"""
    <div style="
        text-align: center; 
        background-color: #007bff; 
        color: white; 
        padding: 15px; 
        border-radius: 10px; 
        font-size: 24px; 
        font-weight: bold; 
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        margin-bottom: 20px;">
        {get_chat_header()}
    </div>
""", unsafe_allow_html=True)

# แสดงประวัติแชท
for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f'''
            <div style="display: flex; justify-content: flex-end; align-items: center; margin-bottom: 10px;">
                <div style="background-color: #00BFFF; padding: 10px 20px; border-radius: 15px; max-width: 70%; text-align: right; 
                            box-shadow: 0 4px 6px rgba(10, 10, 10, 10); font-family: 'Arial', sans-serif;">
                    <strong style="color: white;">Mickey:</strong> {message}
                </div>
                <img src="https://cdn-icons-png.flaticon.com/512/847/847969.png" width="40" 
                     style="border-radius: 50%; margin-left: 10px;">
            </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown(f'''
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <img src="https://cdn-icons-png.flaticon.com/512/4712/4712034.png" width="40" 
                     style="border-radius: 50%; margin-right: 10px;">
                <div style="background-color: #FF4500; padding: 10px 20px; border-radius: 15px; max-width: 70%;
                            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); font-family: 'Arial', sans-serif;">
                    <strong style="color: white;">Bot 🤖:</strong> {message}
                </div>
            </div>
        ''', unsafe_allow_html=True)

# ฟอร์มสำหรับพิมพ์ข้อความ
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:", key="user_input", placeholder="Type something...")
    submitted = st.form_submit_button('Send')

# ส่งข้อความไปยัง backend และอัปเดตแชท
if submitted and user_input:
    chatbot = st.session_state.chatbot
    response = chatbot.get_response(user_input)  # ฟังก์ชันนี้ควรรองรับภาษาไทย
    
    # บันทึกประวัติแชท
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response))
    
    # อัปเดต UI ทันที
    st.rerun()
