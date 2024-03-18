def words_b(filename):
    """
    Find 3 letter words in the file
    :param filename: Name of the file
    :return: Nothinf
    """
    # open the file
    with open(filename, "r") as file:
        # go over the file line by line
    for line in file:
        # get the words in the line
    words = line.split(" ")
    for words in words:
    return