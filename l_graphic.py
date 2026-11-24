from mlx import Mlx


class ml_graphic():
    def __init__(self, param: dict):
        self.height = param['height']
        self.width = param['width']
        self.rect_w = param['x_size']
        self.rect_h = param['y_size']
        self.addr = 0
        self.size_line = 0
        self.bpp = 0
        self.x = 0
        self.y = 0

    def colors(self, color: str):
        self.colors: dict = {
            'red': 0xFF0000,
            'green': 0x00FF00,
            'blue': 0x0000FF,
            'yellow': 0xFFFF00,
            'cyan': 0x00FFFF,
            'magenta': 0xFF00FF,
            'orange': 0xFF8000,
            'purple': 0x8000FF,
            'pink': 0xFF69B4,
            'white': 0xFFFFFF
        }
        return self.colors[color]

    """Prototipo (addr, size_line, bpp, x, y, length, color)"""
    def draw_west(self, color: str):
        """
        if (temp[0] == "1"):
             pygame.draw.line(self.screen, cl, (x, y),
             (x, y + self.rect_h),
             self.border_thickness)
        """
        
        """
          def draw_vertical_line(addr, size_line, bpp, x, y, length, color):
          bytes_per_pixel = bpp // 8
          color_bytes = color.to_bytes(4, byteorder="little")

          for row in range(y, y + length):
              offset = (row * size_line) + (x * bytes_per_pixel)
              addr[offset: offset + 4] = color_bytes
        """

    def draw_east(self, color: str):
        clr = self.colors(color)
        print(clr)
        """
        if (temp[2] == "1"):
            pygame.draw.line(self.screen, cl, (x + self.rect_w, y),
            (x + self.rect_w, y + self.rect_h),
            self.border_thickness)
        """

    def draw_north(self,  color: str):
        clr = self.colors(color)
        print(clr)
        """
        if (temp[3] == "1"):
        pygame.draw.line(self.screen, cl, (x, y),
        ((x + self.rect_w, y)),
        self.border_thickness)
        """

    def draw_south(self,  color: str):
        clr = self.colors(color)
        print(clr)
        """
        if (temp[1] == "1"):
           pygame.draw.line(self.screen, cl, (x, y + self.rect_h),
           (x + self.rect_w, y + self.rect_h),
           self.border_thickness)
        """

    def draw_maze(self, file: str):
        pass

    def run_program(self):
        pass


config = {
    'height': 600,
    'width': 400,
    'x_size': 45,
    'y_size': 45,
}


def close_window(keycode, param):
    if keycode == 65307:
        m.mlx_loop_exit(mlx_ptr)


"""----------------------------ZONA DE TESTES----------------------------"""
try:
    m = Mlx()
    mlx_ptr = m.mlx_init()
    window = m.mlx_new_window(
        mlx_ptr, config['width'], config['height'], "Amazing")

    image = m.mlx_new_image(mlx_ptr, config['width'], config['height'])
    addr, bpp, size_line, endian = m.mlx_get_data_addr(image)
    """ Por executar as funcoes North, East, West and East"""
    m.mlx_put_image_to_window(mlx_ptr, window, image, 0, 0)
    m.mlx_key_hook(window, close_window, None)
    m.mlx_loop(mlx_ptr)
    m.mlx_destroy_window(mlx_ptr)
except RuntimeError as e:
    print(e)
