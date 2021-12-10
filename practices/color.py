from abc import ABC, abstractmethod


class ComputerColor(ABC):
    @abstractmethod
    def __str__(self) -> str:
        raise ValueError()

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __eq__(self, o: object) -> bool:
        pass

    @abstractmethod
    def __add__(self, other) -> "ComputerColor":
        pass

    @abstractmethod
    def __mul__(self, other) -> "ComputerColor":
        pass

    @abstractmethod
    def __rmul__(self, other) -> "ComputerColor":
        pass

    @abstractmethod
    def __hash__(self) -> int:
        pass


class RGBColor(ComputerColor):
    END = "\033[0"
    START = "\033[1;38;2"
    MOD = "m"

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f"{self.START};{self.red};{self.green};{self.blue}{self.MOD}●{self.END}{self.MOD}"

    __repr__ = __str__

    def __eq__(self, other):
        if not isinstance(other, RGBColor):
            return False
        return (
                self.blue == other.blue
                and self.green == other.green
                and self.red == other.red
        )

    def __add__(self, other):
        if not isinstance(other, RGBColor):
            raise ValueError(f"Сложение цвета с {type(other)} недопустимо")
        return RGBColor(
            min(self.red + other.red, 255),
            min(self.green + other.green, 255),
            min(self.blue + other.blue, 255),
        )

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def __mul__(self, c):
        if c < 0 or c > 1:
            raise ValueError("Число от 0 до 1")
        cl = -256 * (1 - c)
        f = (259 * (cl + 255)) / (255 * (259 - cl))
        return RGBColor(
            int(f * (self.red - 128) + 128),
            int(f * (self.green - 128) + 128),
            int(f * (self.blue - 128) + 128),
        )

    __rmul__ = __mul__


class HSBColor(ComputerColor):
    pass


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix:
        print("".join(str(ptr) for ptr in row))


if __name__ == "__main__":
    r = RGBColor(255, 0, 0)
    g = RGBColor(0, 255, 0)
    b = RGBColor(0, 0, 255)

    print_a(0.5 * (g + b))
