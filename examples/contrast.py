"""Check a pair of six-digit hex colors against 4.5:1 for normal text."""
import argparse
import re


def luminance(color):
    if not re.fullmatch(r"#?[0-9a-fA-F]{6}", color):
        raise ValueError("Use six hexadecimal digits, optionally prefixed with #")
    digits = color.lstrip("#")
    channels = [int(digits[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
              for v in channels]
    return sum(v * weight for v, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("foreground")
    parser.add_argument("background")
    args = parser.parse_args()
    try:
        dark, light = sorted(map(luminance, (args.foreground, args.background)))
    except ValueError as error:
        parser.error(str(error))
    ratio = (light + 0.05) / (dark + 0.05)
    print(f"{ratio:.2f}:1")
    raise SystemExit(0 if ratio >= 4.5 else 1)
