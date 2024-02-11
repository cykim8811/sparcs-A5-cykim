
from pyx2 import createElement, current

class VolunteerTab:
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
            createElement('div', {}, "봉사할 장소 목록"),
            createElement('div', {}, "-> 봉사할 시간"),
            createElement('div', {}, "or 다른 봉사자들과 팀으로"),
            createElement('div', {}, "네트워킹이 가능하다"),
        )
