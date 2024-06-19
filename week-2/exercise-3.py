file_path = "P1_data.txt"


def word_count(file_path):
    res = {}
    with open(file_path, "r") as f:
        for line in f:
            for word in line.split():
                if word.lower() not in res:
                    res[word.lower()] = 1
                else:
                    res[word.lower()] += 1
        return res


word_count(file_path)
