
from pyx2 import createElement, current

class TourTab:
    def __init__(self):
        self.tour_list = [
            {
                'name': '대전 엑스포 과학공원',
                'location': '대전광역시 유성구 엑스포로 123',
                'contact': '042-600-7000',
                'description': '대전의 대표적인 과학공원으로, 다양한 체험시설과 전시관이 있다.',
                'img_path': './sciencepark.jpg'
            },
            {
                'name': '대전 동물원',
                'location': '대전광역시 중구 동물원로 22',
                'contact': '042-580-4800',
                'description': '대전의 동물원으로, 다양한 동물들을 볼 수 있다.',
                'img_path': './zoo.jpeg'
            },
            {
                'name': '대전시립미술관',
                'location': '대전광역시 중구 대종로 471',
                'contact': '042-270-4880',
                'description': '대전의 미술관으로, 다양한 작품들을 감상할 수 있다.',
                'img_path': './artmuseum.jpeg'
            },
        ]

        from PIL import Image
        import io
        for tour in self.tour_list:
            tour['img'] = Image.open(tour['img_path'])

    def __render__(self):
        return createElement("div", {
            'style': {
                'width': '100vw',
                'display': 'flex',
                'justifyContent': 'flex-start',
                'alignItems': 'center',
                'flexDirection': 'column',
            }
        },
            [
                createElement('div', {
                    'style': {
                        'width': '100vw',
                        'height': 'max-content',
                        'paddingBottom': '2vh',
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'left',
                        'flexDirection': 'column',
                        'fontWeight': 'normal',
                        'borderBottom': '1px solid var(--text-200)',
                    }
                },
                    createElement('img', {'src': tour['img'], 'style': {'width': '100vw', 'height': '70vw', 'objectFit': 'cover'}}),
                    createElement('div', {
                        'style': {
                            'paddingLeft': '2vw',
                            'paddingRight': '2vw',
                        }
                    },
                        createElement('div', {
                            'style': {
                                'height': '5vh',
                                'display': 'flex',
                                'justifyContent': 'left',
                                'alignItems': 'center',
                                'flexDirection': 'row',
                                'fontSize': '3vh',
                                'color': 'var(--text-200)',
                                'fontWeight': 'bold',
                            }
                        },
                            tour['name'],
                        ),
                        createElement('div', {
                            'style': {
                                'height': '5vh',
                                'display': 'flex',
                                'justifyContent': 'left',
                                'flexDirection': 'column',
                                'fontSize': '2vh',
                                'marginTop': '-0.5vh',
                                'lineHeight': '2vh',
                                'color': 'var(--text-200)',
                                'opacity': '0.8',
                                'fontWeight': 'bold',
                            }
                        },
                            createElement('span', {},
                                createElement('i', {'className': 'fas fa-map-marker-alt', 'style': {
                                    'marginRight': '1vh',
                                }}),
                                tour['location'],
                            ),
                            createElement('span', {},
                                createElement('i', {'className': 'fas fa-phone-alt', 'style': {
                                    'marginRight': '1vh',
                                }}),
                                tour['contact'],
                            ),
                        ),
                        createElement('div', {
                            'style': {
                                'height': '5vh',
                                'display': 'flex',
                                'justifyContent': 'left',
                                'alignItems': 'center',
                                'flexDirection': 'row',
                                'fontSize': '2vh',
                                'color': 'var(--text-200)',
                            }
                        },
                            tour['description'],
                        ),
                    )
                )
                for tour in self.tour_list
            ],
            createElement('div', {
                'style': {
                    'height': '16vh',
                }
            })
        )
