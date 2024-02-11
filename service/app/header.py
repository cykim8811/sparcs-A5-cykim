
from pyx2 import createElement, current

class Header:
    def __init__(self):
        pass

    def __render__(self):
        return createElement("div", {
            'style': {
                'width': '100vw',
                'height': '7vh',
                'backgroundColor': 'var(--primary-100)',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
                'flexDirection': 'row',
                'fontSize': '2.3vh',
                'fontWeight': 'bold',
                'color': 'var(--accent-200)',
            }
        },
        "대전 문화멘토링",
            createElement('div', {
                'style': {
                    'position': 'absolute',
                    'right': '0',
                }
            },
                createElement('i', {'className': 'fas fa-bars', 'style': {'fontSize': '3vh', 'marginRight': '2vh'}}),
            )
        )

