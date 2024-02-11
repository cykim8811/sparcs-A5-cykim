
from pyx2 import createElement, current

class HomeTab:
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
            createElement('div', {}, "메인페이지"),
            createElement('div', {}, "봉사활동 인증사진들"),
            createElement('div', {}, "추천하는 관광지들"),
            createElement('div', {}, "소식 및 공지"),
        )
