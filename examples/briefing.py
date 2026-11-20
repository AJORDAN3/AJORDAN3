"""Render an offline daily briefing from independent providers."""
def briefing(providers):
    lines = []
    for name, fetch in providers.items():
        try:
            value = fetch()
        except (TimeoutError, ConnectionError):
            value = "Temporarily unavailable"
        lines.append(f"{name}: {value}")
    return "\n".join(lines)


def offline_weather():
    raise TimeoutError("Simulated upstream timeout")


if __name__ == "__main__":
    print(briefing({"Weather": offline_weather, "Calendar": lambda: "2 events",
                    "Inbox": lambda: "3 unread"}))
