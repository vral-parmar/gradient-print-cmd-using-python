from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText(" H  A  P  P  Y ", font='big'),
            int(screen.height / 3 - 5)),
        Cycle(
            screen,
            FigletText(" B  I  R  T  H  D  A  Y ", font='big'),
            int(screen.height / 2 - 1)),
        Cycle(
            screen,
            FigletText(" V  I  R  A  L ", font='big'),
            int(screen.height / 2 + 8)),
        Stars(screen, 300)
    ]
    screen.play([Scene(effects, 500)])


Screen.wrapper(demo)
