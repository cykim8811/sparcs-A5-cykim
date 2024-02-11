
from pyx2 import createElement, current

class Nav:
    def __init__(self, body):
        self.body = body
    
    def changeTab(self, tab):
        self.body.currentTab = tab
        current.app.rerender(self)
        current.app.rerender(self.body)

    def __render__(self):
        return createElement("div", {
            'style': {
                'position': 'fixed',
                'bottom': '0',
                'left': '0',
                'width': '100vw',
                'height': '8vh',
                'backgroundColor': 'var(--bg-200)',
                'display': 'flex',
                'justifyContent': 'space-evenly',
                'alignItems': 'center',
                'flexDirection': 'row',
                'fontSize': '3vh',
                'fontWeight': 'bold',
                'color': 'var(--text-200)',
                'userSelect': 'none',
            }
        },
            createElement('style', {}, '''
                .tab {
                    transition: color 0.25s, transform 0.25s;
                    user-select: none;
                }
                .selected-tab {
                    color: var(--accent-200);
                    transform: translateY(-0.8vh);
                }
            '''),
            createElement('div', {}, createElement('i', {'onClick': lambda: self.changeTab('home'), 'className': 'tab fas fa-home' + (' selected-tab' if self.body.currentTab == 'home' else ''), 'style': {'fontSize': '3vh'}})),
            createElement('div', {}, createElement('i', {'onClick': lambda: self.changeTab('volunteer'), 'className': 'tab fas fa-hands-helping' + (' selected-tab' if self.body.currentTab == 'volunteer' else ''), 'style': {'fontSize': '3vh'}})),
            createElement('div', {}, createElement('i', {'onClick': lambda: self.changeTab('tour'), 'className': 'tab fas fa-map-marked-alt' + (' selected-tab' if self.body.currentTab == 'tour' else ''), 'style': {'fontSize': '3vh'}})),
            createElement('div', {}, createElement('i', {'onClick': lambda: self.changeTab('mypage'), 'className': 'tab fas fa-user' + (' selected-tab' if self.body.currentTab == 'mypage' else ''), 'style': {'fontSize': '3vh'}})),
        )

