#Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.
def convert(hours, minutes):
    if hours or minutes > 0:
        return (hours * 3600) + (minutes*60)
