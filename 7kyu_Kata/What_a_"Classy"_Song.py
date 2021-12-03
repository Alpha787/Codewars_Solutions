class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.counter = []

    def how_many(self, array_of_people):
        count = []
        for value in array_of_people:
            if value.upper() in self.counter:
                continue
            else:
                self.counter.append(value.upper())
                count.append(value)
        return len(count)
