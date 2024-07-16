def count_words(string):
    words = string.split()
    return len(words)


def sort_on(dict):
    return dict["count"]


def count_characters(string):
    counts = {}
    string = string.lower()
    for c in string:
        if ord(c) > 96 and ord(c) < 123:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

    counts_list = []
    for c,count in counts.items():
        counts_list.append({"character": c, "count": count})


    counts_list.sort(reverse=True, key=sort_on)
    return counts_list


def main():
    book_location = "books/frankenstein.txt"
    with open(book_location) as f:
        file_contents = f.read()

    counts_list = count_characters(file_contents)
    word_count = count_words(file_contents)

    print(f"--- Begin report of {book_location} ---")
    print(f"{word_count} words found in the document\n")

    for ch in counts_list:
        c = ch["character"]
        count = ch["count"]
        print(f"The '{c}' character was found {count} times")

    print("--- End report ---")

if __name__ == "__main__":
    main()
