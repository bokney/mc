
import pytest
from src.mc import Point, Square, Circle, MonteCarloSimulation


class TestSquare:

    def setup_method(self):
        self.square = Square(100, 100, 50)

    def test_not_intersecting(self):
        point = Point(0, 0)
        assert not self.square.intersects_with_point(point)
        point = Point(74, 125)
        assert not self.square.intersects_with_point(point)
        point = Point(126, 125)
        assert not self.square.intersects_with_point(point)
        point = Point(100, 74)
        assert not self.square.intersects_with_point(point)
        point = Point(100, 126)
        assert not self.square.intersects_with_point(point)

    def test_intersecting(self):
        point = Point(100, 100)
        assert self.square.intersects_with_point(point)
        point = Point(76, 125)
        assert self.square.intersects_with_point(point)
        point = Point(124, 125)
        assert self.square.intersects_with_point(point)
        point = Point(100, 76)
        assert self.square.intersects_with_point(point)
        point = Point(100, 124)
        assert self.square.intersects_with_point(point)

    def test_edge_case(self):
        point = Point(75, 125)
        assert self.square.intersects_with_point(point)
        point = Point(125, 125)
        assert self.square.intersects_with_point(point)
        point = Point(125, 75)
        assert self.square.intersects_with_point(point)
        point = Point(75, 75)
        assert self.square.intersects_with_point(point)


class TestCircle:
    
    def setup_method(self):
        self.circle = Circle(100, 100, 50)

    def test_not_intersecting(self):
        point = Point(0, 0)
        assert not self.circle.intersects_with_point(point)
        point = Point(100, 151)
        assert not self.circle.intersects_with_point(point)

    def test_intersecting(self):
        point = Point(100, 100)
        assert self.circle.intersects_with_point(point)
        point = Point(100, 149)
        assert self.circle.intersects_with_point(point)
        point = Point(100, 51)
        assert self.circle.intersects_with_point(point)

    def test_edge_case(self):
        point = Point(100, 150)
        assert self.circle.intersects_with_point(point)
        point = Point(100, 50)
        assert self.circle.intersects_with_point(point)
        point = Point(150, 100)
        assert self.circle.intersects_with_point(point)
        point = Point(50, 100)
        assert self.circle.intersects_with_point(point)


class TestMonteCarloSimulation:

    def setup_method(self):
        self.mc = MonteCarloSimulation()
    
    def test_plot_point_appends_coordinate_array(self):
        num_rows, num_cols = self.mc.test_area.plotted_points.shape
        assert num_cols == 2
        assert num_rows == 0
        assert self.mc.test_area.plotted_points.size == 0
        self.mc._plot_point(self.mc._random_point())
        num_rows, num_cols = self.mc.test_area.plotted_points.shape
        assert num_cols == 2
        assert num_rows == 1
        assert self.mc.test_area.plotted_points.size == 2
        self.mc._plot_point(self.mc._random_point())
        num_rows, num_cols = self.mc.test_area.plotted_points.shape
        assert num_cols == 2
        assert num_rows == 2
        assert self.mc.test_area.plotted_points.size == 4

    def test_run_simulation_plots_points(self):
        num_rows, num_cols = self.mc.test_area.plotted_points.shape
        assert num_cols == 2
        assert num_rows == 0
        assert self.mc.test_area.plotted_points.size == 0
        self.mc.run_simulation(100)
        num_rows, num_cols = self.mc.test_area.plotted_points.shape
        assert num_cols == 2
        assert num_rows == 100
        assert self.mc.test_area.plotted_points.size == 200
        self.mc.run_simulation(303)
        num_rows, num_cols = self.mc.test_area.plotted_points.shape
        assert num_cols == 2
        assert num_rows == 303
        assert self.mc.test_area.plotted_points.size == 606
