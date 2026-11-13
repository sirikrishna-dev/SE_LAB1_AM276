import math


def parse_zone(text):
    """Parse a zone name and area from the format 'name:area'."""
    try:
        if not isinstance(text, str):
            return None
        parts = text.split(":")
        if len(parts) != 2:
            return None
        name = parts[0].strip()
        area_text = parts[1].strip()
        if not name or not area_text:
            return None
        area = float(area_text)
        if not math.isfinite(area) or area < 0:
            return None
        return name.title(), area
    except (ValueError, TypeError):
        return None


def moisture_average(readings_csv):
    """Return the integer average of comma-separated integer readings."""
    try:
        if not isinstance(readings_csv, str):
            return None
        readings = readings_csv.split(",")
        if not readings or any(not reading.strip() for reading in readings):
            return None
        values = [int(reading.strip()) for reading in readings]
        return sum(values) // len(values)
    except (ValueError, TypeError, ZeroDivisionError):
        return None


def water_needed(text):
    """Calculate water needed from 'plot_area|rainfall' input."""
    try:
        if not isinstance(text, str):
            return None
        parts = text.split("|")
        if len(parts) != 2:
            return None
        plot = float(parts[0].strip())
        rain = float(parts[1].strip())
        if not math.isfinite(plot) or not math.isfinite(rain):
            return None
        if plot < 0 or rain < 0:
            return None
        return max(plot * 5 - rain, 0)
    except (ValueError, TypeError):
        return None


def main():
    print("==== Running parse_zone ====")
    user_input = input("Enter zone:area in m2 (e.g. north:120): ")
    print("Zone and Area:", parse_zone(user_input))

    print("\n==== Running moisture_average ====")
    user_input = input("Enter moisture readings as CSV (e.g. 40,35,50): ")
    print("Average Moisture:", moisture_average(user_input))

    print("\n==== Running water_needed ====")
    user_input = input("Enter area|rainfall (e.g. 120|8): ")
    print("Water Needed:", water_needed(user_input))


if __name__ == "__main__":
    main()
