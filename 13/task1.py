def main():
    input = "input.txt"
    with open(input) as file:
        earliest_possible_timestamp = int(next(file))
        bus_ids = next(file).split(",")
        bus_ids_in_service = [int(id) for id in bus_ids if id != "x"]
        closest_multiple_of_each_bus_id = [
            find_closest_multiple(earliest_possible_timestamp, bus_id)
            for bus_id in bus_ids_in_service
        ]
        min_time_to_wait = min(closest_multiple_of_each_bus_id)
        bus_to_take = bus_ids_in_service[
            closest_multiple_of_each_bus_id.index(min_time_to_wait)
        ]
        print(f"bus {bus_to_take} wait_time {min_time_to_wait}")
        print(f"product {bus_to_take * min_time_to_wait}")


def find_closest_multiple(target, multiple_base):
    floored_multiple = target // multiple_base
    return ((floored_multiple + 1) * multiple_base) - target


if __name__ == "__main__":
    main()
