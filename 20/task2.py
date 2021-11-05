import math


def main():
    width, height = (10, 10)
    grid = {}
    tiles = parse_input_into_tiles("input.txt")
    overlapping_tiles = get_overlapping_tiles(tiles)
    corner_tiles, border_tiles, internal_tiles = classify_tiles(overlapping_tiles)


def classify_tiles(overlapping_tiles):
    corners = []
    borders = []
    internals = []
    for tile, neighbours in overlapping_tiles.items():
        neighbour_count = len(neighbours)
        if neighbour_count == 2:
            corners.append(tile)
        elif neighbour_count == 3:
            borders.append(tile)
        elif neighbour_count == 4:
            internals.append(tile)
    return corners, borders, internals


def get_overlapping_tiles(tiles):
    edges = {}
    overlapping_tiles = {}
    for tile_id, tile in tiles.items():
        edges[tile_id] = get_edges(tile)
    for tile_id, tile_edges in edges.items():
        for other_tile_id, other_tile_edges in edges.items():
            if other_tile_id == tile_id:
                continue
            for edge in tile_edges:
                if edge in other_tile_edges or edge[::-1] in other_tile_edges:
                    overlapping_tiles[tile_id] = overlapping_tiles.get(
                        tile_id, set()
                    ).add(other_tile_id)
    return overlapping_tiles


def get_edges(tile):
    top_edge = tile[0]
    bottom_edge = tile[-1]
    left_edge = ""
    right_edge = ""
    for row in tile:
        left_edge += row[0]
        right_edge += row[-1]
    return (top_edge, right_edge, bottom_edge, left_edge)


def parse_input_into_tiles(input):
    tiles = {}
    with open(input) as file:
        tiles_bare = file.read().split("\n\n")
        for tile_bare in tiles_bare:
            lines = tile_bare.splitlines()
            unique_id = int(lines[0].strip()[len("Tile ") : -1])
            tile = lines[1:]
            tiles[unique_id] = tile
    return tiles


if __name__ == "__main__":
    main()
