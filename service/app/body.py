
from pyx2 import createElement, current

from .tabs import home, tour, volunteer, mypage

# add .. to the path to import the watch function from the parent directory
import sys
sys.path.append("..")
from watcher import watch


class Body:
    def __init__(self):
        self.tabs = {
            'home': home.HomeTab(),
            'tour': tour.TourTab(),
            'volunteer': volunteer.VolunteerTab(),
            'mypage': mypage.MypageTab(),
        }
        self.currentTab = 'home'
        watch(home, self.tabs['home'])
        watch(tour, self.tabs['tour'])
        watch(volunteer, self.tabs['volunteer'])
        watch(mypage, self.tabs['mypage'])

    def __render__(self):
        return createElement("div", {
            'style': {
                'width': '100vw',
                'height': '92vh',
                'backgroundColor': 'var(--bg-100)',
                'justifyContent': 'center',
                'alignItems': 'center',
                'flexDirection': 'column',
                'fontSize': '3vh',
                'fontWeight': 'bold',
                'color': 'var(--accent-200)',
                'overflow': 'auto',
            }
        },
            self.tabs[self.currentTab],
        )

