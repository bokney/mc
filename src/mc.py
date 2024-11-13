
from random import uniform
import numpy as np
import matplotlib.pyplot as plt
import math


class Point:

    data: np.ndarray

    @property
    def x(self) -> float:
        return self.data[0]
    @x.setter
    def x(self, value: float):
        self.data[0] = value

    @property
    def y(self) -> float:
        return self.data[1]
    @y.setter
    def y(self, value: float):
        self.data[1] = value

    def __init__(self, x: float, y: float):
        self.data = np.array([x, y])


class Shape:

    position: Point
    size: float

    def __init__(self, x: float, y: float, size: float) -> None:
        self.position = Point(x, y)
        self.size = size


class Circle(Shape):

    def __init__(self, x: float, y: float, size: float) -> None:
        super().__init__(x, y, size)

    def intersects_with_point(self, point: Point) -> bool:
        distance = math.sqrt(
            (point.x - self.position.x) ** 2 +
            (point.y - self.position.y) ** 2
            )
        return distance <= self.size


class Square(Shape):

    def __init__(self, x: float, y: float, size: float) -> None:
        super().__init__(x, y, size)

    def intersects_with_point(self, point: Point) -> bool:
        half = self.size / 2
        return (
            self.position.x - half <= point.x <= self.position.x + half and
            self.position.y - half <= point.y <= self.position.y + half
            )


class TestArea:

    width: int = 1440
    height: int = 720
    size: int = 240

    square: Square
    circle: Circle

    plotted_points: np.ndarray

    def __init__(self) -> None:
        self.square = Square(self.width / 3, self.height / 2, self.size)
        self.circle = Circle(self.width / 3 * 2,self.height / 2, self.size)
        self.plotted_points = np.empty((0, 2), dtype = float)

    def clear_plotted_points(self) -> None:
        if self.plotted_points.shape[0] > 0:
            self.plotted_points = np.empty((0, 2), dtype = float)


class MonteCarloSimulation:

    test_area: TestArea
    
    def __init__(self) -> None:
        self.test_area = TestArea()

    def _random_point(self) -> Point:
        x = uniform(0., self.test_area.width)
        y = uniform(0., self.test_area.height)
        return Point(x, y)

    def _plot_point(self, point: Point) -> None:
        self.test_area.plotted_points = np.vstack([
            self.test_area.plotted_points, point.data
            ])

    def run_simulation(self, plot_count: int) -> None:
        self.test_area.clear_plotted_points()
        for i in range(plot_count):
            self._plot_point(self._random_point())

    def tally_square_intersections(self) -> int:
        tally = 0
        for i in self.test_area.plotted_points:
            if self.test_area.square.intersects_with_point(Point(i[0], i[1])):
                tally += 1
        return tally

    def tally_circle_intersections(self) -> int:
        tally = 0
        for i in self.test_area.plotted_points:
            if self.test_area.circle.intersects_with_point(Point(i[0], i[1])):
                tally += 1
        return tally

    def visualise_simulation(self) -> None:
        square_points = []
        circle_points = []

        for point in self.test_area.plotted_points:
            p = Point(point[0], point[1])
            if self.test_area.square.intersects_with_point(p):
                square_points.append(point)
            elif self.test_area.circle.intersects_with_point(p):
                circle_points.append(point)

        square_points = np.array(square_points)
        circle_points = np.array(circle_points)

        plt.scatter(square_points[:, 0], square_points[:, 1])
        plt.scatter(circle_points[:, 0], circle_points[:, 1])

        plt.legend()
        plt.show()


mc = MonteCarloSimulation()
mc.run_simulation(100000)
mc.visualise_simulation()
