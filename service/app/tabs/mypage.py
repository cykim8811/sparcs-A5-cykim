
from pyx2 import createElement, current

class MypageTab:
    def __init__(self):
        pass

    def __render__(self):
        return createElement("div", {
            'style': {
                'width': '100vw',
                'height': '100vh',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'flexDirection': 'column',
            }
        },
            createElement('div', {}, "마이페이지"),
            createElement('div', {}, "봉사활동 인증사진들"),
            createElement('div', {}, "봉사활동 기록"),
            createElement('div', {}, "봉사활동 팀"),
            createElement('div', {}, "봉사활동 인증서/봉사시간"),
            createElement('div', {}, "귀여운 캐릭터 키우기"),
        )
