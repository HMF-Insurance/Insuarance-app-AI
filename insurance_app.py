import streamlit as st
import pandas as pd
import datetime

# --- 설정 및 스타일 ---
st.set_page_config(page_title="Gemini 인슈어런스", layout="wide")

# --- 세션 상태 초기화 (데이터베이스 대용) ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'claims' not in st.session_state:
    st.session_state.claims = []

# --- 1. 로그인 시스템 ---
def login_page():
    st.title("🔐 로그인")
    with st.form("login_form"):
        user_id = st.text_input("아이디")
        password = st.text_input("비밀번호", type="password")
        submitted = st.form_submit_button("로그인")
        if submitted:
            if user_id == "admin" and password == "1234":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("아이디 또는 비밀번호가 틀렸습니다.")

# --- 2. 보험료 계산기 (로직) ---
def premium_calculator():
    st.header("🧮 실시간 보험료 계산")
    age = st.number_input("나이", min_value=18, max_value=100, value=30)
    car_type = st.selectbox("차종", ["경차", "승용차", "SUV", "수입차"])
    history = st.slider("무사고 경력 (년)", 0, 20, 5)
    
    # 간단한 계산 알고리즘
    base_price = 500000
    car_multiplier = {"경차": 0.8, "승용차": 1.0, "SUV": 1.2, "수입차": 2.5}
    age_multiplier = 1.5 if age < 26 else 1.0
    discount = history * 20000
    
    total = (base_price * car_multiplier[car_type] * age_multiplier) - discount
    st.subheader(f"예상 연간 보험료: **{max(total, 100000):,.0f}원**")

# --- 3. 사고 접수 및 청구 ---
def claim_system():
    st.header("🚨 사고 접수 및 보험료 청구")
    with st.form("claim_form"):
        claim_type = st.selectbox("접수 유형", ["자동차 사고", "대인 배상", "재물 손괴"])
        date = st.date_input("사고 일자", datetime.date.today())
        description = st.text_area("사고 경위")
        uploaded_file = st.file_uploader("현장 사진 또는 증빙 서류 업로드", type=['jpg', 'png', 'pdf'])
        
        if st.form_submit_button("접수하기"):
            new_claim = {"유형": claim_type, "날짜": date, "내용": description, "상태": "심사중"}
            st.session_state.claims.append(new_claim)
            st.success("접수가 완료되었습니다. 담당자가 곧 연락드릴 예정입니다.")

# --- 4. 고객 응대 (AI 챗봇 모사) ---
def customer_service():
    st.header("💬 고객센터 (FAQ)")
    query = st.text_input("궁금한 점을 입력하세요.")
    if query:
        if "납부" in query:
            st.info("💡 보험료 납부는 매월 5일에 자동이체됩니다.")
        elif "증명서" in query:
            st.info("💡 증명서 발급은 '마이페이지 > 서류발급' 메뉴를 이용해주세요.")
        else:
            st.write("상담원을 연결해 드릴까요? (연결 번호: 1588-0000)")

# --- 메인 네비게이션 ---
if not st.session_state.logged_in:
    login_page()
else:
    st.sidebar.title("Gemini Insurance")
    menu = st.sidebar.radio("메뉴 선택", ["대시보드", "보험료 계산", "사고 접수", "고객 센터", "로그아웃"])
    
    if menu == "대시보드":
        st.title("🏠 마이 대시보드")
        st.write("반갑습니다, 관리자님!")
        if st.session_state.claims:
            st.subheader("내 접수 내역")
            st.table(pd.DataFrame(st.session_state.claims))
        else:
            st.info("진행 중인 접수 건이 없습니다.")
            
    elif menu == "보험료 계산":
        premium_calculator()
    elif menu == "사고 접수":
        claim_system()
    elif menu == "고객 센터":
        customer_service()
    elif menu == "로그아웃":
        st.session_state.logged_in = False
        st.rerun()
