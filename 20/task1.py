import math


def main():
    tiles = parse_input_into_tiles("input.txt")
    edges = {}
    for tile_id, tile in tiles:
        edges[tile_id] = get_edges(tile)
    tile_degree = {}
    for tile_id, tile_edges in edges.items():
        connected_tiles = 0
        for tile, other_edges in edges.items():
            if tile == tile_id:
                continue
            for edge in tile_edges:
                if edge in other_edges or edge[::-1] in other_edges:
                    connected_tiles += 1
        tile_degree[tile_id] = connected_tiles
    corners = [tile for tile in tile_degree if tile_degree[tile] == 2]
    print(corners)
    print(f"solution part1 [{math.prod(corners)}]")


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
    tiles = []
    with open(input) as file:
        tiles_bare = file.read().split("\n\n")
        for tile_bare in tiles_bare:
            lines = tile_bare.splitlines()
            unique_id = int(lines[0].strip()[len("Tile ") : -1])
            tile = lines[1:]
            tiles.append((unique_id, tile))
    return tiles


if __name__ == "__main__":
    main()
