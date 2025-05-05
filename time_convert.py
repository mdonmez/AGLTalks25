def convert_time(start_time: str, end_time: str) -> tuple[int, int]:
    """
    It will get start and end time from string and return them as start second and duration.
    """
    start_time = start_time.split(":")
    end_time = end_time.split(":")
    start_second = int(start_time[0]) * 60 + int(start_time[1])
    end_second = int(end_time[0]) * 60 + int(end_time[1])
    duration = end_second - start_second
    return start_second, duration


if __name__ == "__main__":
    print(convert_time("00:20", "00:40"))
