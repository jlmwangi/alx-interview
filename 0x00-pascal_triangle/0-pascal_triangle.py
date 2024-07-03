""" generate pascals triangle """
def pascal_triangle(n):
    """implementation of a pascals triangle given number of rows"""
    if n <= 0:
        print("[]")

    triangle = []

    for i in range(n):
        row = [1]   # start each row with 1
        if triangle:   # if there ae previous rows
            last_row = triangle[-1]   # access the previous last row
            row.extend([last_row[j] + last_row[j + 1]   # sum adjacent values
                       for j in range(len(last_row) - 1)])   # depending length
            row.append(1)   # add 1 to end of row
        triangle.append(row)   # append each row to triangle

    return triangle
