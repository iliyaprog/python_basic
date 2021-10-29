import math


class MyMath:

    """Класс формул математики"""

    @staticmethod
    def circle_len(radius: (int, float)) -> (int, float):
        result = 2 * math.pi * radius
        return result

    @staticmethod
    def circle_sq(radius: (int, float)) -> (int, float):
        result = math.pi * (radius ** 2)
        return result

    @staticmethod
    def cube_volume(
            len_cube: (int, float), width: (int, float), height: (int, float)) -> (int, float):
        result = len_cube * width * height
        return result

    @staticmethod
    def sphere_sq(radius: (int, float)) -> (int, float):
        result = 4 * math.pi * (radius ** 2)
        return result

    @staticmethod
    def triangle_sq(height: (int, float), base_triangle: (int, float)) -> (int, float):
        result = height * base_triangle / 2
        return result


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_volume(len_cube=7, width=5, height=10)
res_4 = MyMath.sphere_sq(radius=8)
res_5 = MyMath.triangle_sq(height=10, base_triangle=14)
print(res_1)
print(res_2)
print(res_3)
print(res_4)
print(res_5)