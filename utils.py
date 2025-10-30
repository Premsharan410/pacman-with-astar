# utils.py

def grid_pos_to_pixel(grid_x, grid_y, y_offset=40):
    return grid_x * 20, grid_y * 20 + y_offset

def pixel_to_grid_pos(pixel_x, pixel_y, y_offset=40):
    return pixel_x // 20, (pixel_y - y_offset) // 20
