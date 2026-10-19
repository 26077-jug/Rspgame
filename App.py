
import random
import streamlit as st

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="가위바위보 챌린지",
    page_icon="✊",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# 세션 상태 초기화
# -----------------------------
if "wins" not in st.session_state:
    st.session_state.wins = 0

if "losses" not in st.session_state:
    st.session_state.losses = 0

if "draws" not in st.session_state:
    st.session_state.draws = 0

if "rounds" not in st.session_state:
    st.session_state.rounds = 0

if "last_result" not in st.session_state:
    st.session_state.last_result = None

# -----------------------------
# 디자인 CSS
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #10172a 0%, #172554 100%);
        color: #f8fafc;
    }

    .main .block-container {
        max-width: 760px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3, p, label {
        color: #f8fafc;
    }

    .subtitle {
        color: #cbd5e1;
        text-align: center;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }

    .game-card {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 22px;
        text-align: center;
        margin: 10px 0;
    }

    .choice-emoji {
        font-size: 4rem;
        margin-bottom: 8px;
    }

    .choice-label {
        color: #cbd5e1;
        font-size: 1rem;
    }

    .result-card {
        background: rgba(255, 255, 255, 0.10);
        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        margin-top: 18px;
    }

    .result-title {
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .result-description {
        color: #e2e8f0;
        font-size: 1rem;
    }

    div.stButton > button {
        width: 100%;
        min-height: 3rem;
        border-radius: 12px;
        border: 1px solid #64748b;
        font-size: 1rem;
        font-weight: 700;
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        border-color: #38bdf8;
        color: #38bdf8;
        transform: translateY(-2px);
    }

    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.07);
        padding: 14px;
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.12);
    }

    div[data-testid="stMetricLabel"] {
        color: #cbd5e1;
    }

    div[data-testid="stMetricValue"] {
        color: #f8fafc;
    }

    hr {
        border-color: rgba(255, 255, 255, 0.15);
    }

    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 0.85rem;
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# 게임 데이터
# -----------------------------
choices = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋",
}

# -----------------------------
# 제목
# -----------------------------
st.markdown(
    "<h1 style='text-align:center;'>✊ 가위바위보 챌린지</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    "<p class='subtitle'>컴퓨터를 이기고 최고의 챔피언에 도전하자! 🏆</p>",
    unsafe_allow_html=True,
)

st.divider()

# -----------------------------
# 사용자 선택
# -----------------------------
st.subheader("🎮 무엇을 낼까?")
st.write("아래 버튼 중 하나를 눌러 컴퓨터와 대결해 봐!")

col1, col2, col3 = st.columns(3)

with col1:
    scissors_clicked = st.button(
        "✌️ 가위",
        use_container_width=True,
        key="scissors",
    )

with col2:
    rock_clicked = st.button(
        "✊ 바위",
        use_container_width=True,
        key="rock",
    )

with col3:
    paper_clicked = st.button(
        "✋ 보",
        use_container_width=True,
        key="paper",
    )

# -----------------------------
# 게임 실행
# -----------------------------
user_choice = None

if scissors_clicked:
    user_choice = "가위"
elif rock_clicked:
    user_choice = "바위"
elif paper_clicked:
    user_choice = "보"

if user_choice is not None:
    computer_choice = random.choice(list(choices.keys()))
    st.session_state.rounds += 1

    if user_choice == computer_choice:
        result = "draw"
        st.session_state.draws += 1
        result_title = "🤝 무승부!"
        result_message = "비겼어! 다시 도전해 봐."
        result_icon = "🤝"

    elif (
        (user_choice == "가위" and computer_choice == "보")
        or (user_choice == "바위" and computer_choice == "가위")
        or (user_choice == "보" and computer_choice == "바위")
    ):
        result = "win"
        st.session_state.wins += 1
        result_title = "🎉 승리!"
        result_message = "대단해! 컴퓨터를 이겼어!"
        result_icon = "🏆"

    else:
        result = "loss"
        st.session_state.losses += 1
        result_title = "😵 패배!"
        result_message = "아쉽다! 다음 판에는 이길 수 있어!"
        result_icon = "💪"

    st.session_state.last_result = {
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result,
        "result_title": result_title,
        "result_message": result_message,
        "result_icon": result_icon,
    }

# -----------------------------
# 대결 결과 표시
# -----------------------------
last = st.session_state.last_result

if last is not None:
    st.markdown("---")
    st.subheader("⚔️ 대결 결과")

    user_col, vs_col, computer_col = st.columns([2, 1, 2])

    with user_col:
        st.markdown(
            f"""
            <div class="game-card">
                <div class="choice-emoji">{choices[last["user_choice"]]}</div>
                <h3>나</h3>
                <div class="choice-label">{last["user_choice"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with vs_col:
        st.markdown(
            """
            <div style="text-align:center; padding-top:50px;">
                <span style="font-size:1.6rem; font-weight:900;
                color:#38bdf8;">VS</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with computer_col:
        st.markdown(
            f"""
            <div class="game-card">
                <div class="choice-emoji">{choices[last["computer_choice"]]}</div>
                <h3>컴퓨터</h3>
                <div class="choice-label">{last["computer_choice"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
        <div class="result-card">
            <div style="font-size:2.5rem;">{last["result_icon"]}</div>
            <div class="result-title">{last["result_title"]}</div>
            <div class="result-description">{last["result_message"]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if last["result"] == "win":
        st.balloons()

else:
    st.info("👆 가위, 바위, 보 중 하나를 선택하면 대결이 시작돼!")

# -----------------------------
# 점수판
# -----------------------------
st.markdown("---")
st.subheader("📊 나의 전적")

metric1, metric2, metric3 = st.columns(3)

with metric1:
    st.metric("🏆 승리", st.session_state.wins)

with metric2:
    st.metric("😵 패배", st.session_state.losses)

with metric3:
    st.metric("🤝 무승부", st.session_state.draws)

if st.session_state.rounds > 0:
    win_rate = (
        st.session_state.wins / st.session_state.rounds
    ) * 100

    st.progress(win_rate / 100)
    st.caption(
        f"총 {st.session_state.rounds}판 · "
        f"승률 {win_rate:.1f}%"
    )

    if st.session_state.wins >= 5:
        st.success("🌟 대단해! 5승을 달성했어!")
    elif st.session_state.rounds >= 10:
        st.info("🔥 10판을 완료했어! 계속 도전해 봐!")

else:
    st.caption("아직 대결 기록이 없어. 첫 판을 시작해 봐!")

# -----------------------------
# 다시 시작 버튼
# -----------------------------
st.markdown("")

if st.button(
    "🔄 기록 초기화",
    use_container_width=True,
    key="reset_game",
):
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.draws = 0
    st.session_state.rounds = 0
    st.session_state.last_result = None
    st.rerun()

# -----------------------------
# 하단 문구
# -----------------------------
st.markdown(
    """
    <div class="footer">
        🎮 ROCK · PAPER · SCISSORS<br>
        운도 실력! 오늘의 챔피언은 바로 너!
    </div>
    """,
    unsafe_allow_html=True,
)
