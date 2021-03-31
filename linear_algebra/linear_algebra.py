# At first we need to define a helpful function that will make a zero matrix
def zero_matrix(rows, cols):
    """
    Creates a matrix whose entries are zero.

        :param rows: the number of rows in the matrix
        :param cols: the number of columns in the matrix

        :return: the matrix (list of lists)
    """
    matrix = []
    while len(matrix) < rows:
        matrix.append([])
        while len(matrix[-1]) < cols:
            matrix[-1].append(0)
    return matrix


# Addition
def add_matrix(matrix_1, matrix_2):
    """
    Adds two matrices and returns the sum

        :param matrix_1: The first matrix
        :param matrix_2: The second matrix

        :return: The sum of the matrices
    """
    rows_matrix_1 = len(matrix_1)
    cols_matrix_1 = len(matrix_1[0])
    rows_matrix_2 = len(matrix_2)
    cols_matrix_2 = len(matrix_2[0])

    if rows_matrix_1 != rows_matrix_2 or cols_matrix_1 != cols_matrix_2:
        raise ArithmeticError("You can't sum matrices of different size.")

    m_sum = zero_matrix(rows_matrix_1, cols_matrix_2)

    for i in range(rows_matrix_1):
        for j in range(cols_matrix_2):
            m_sum[i][j] = matrix_1[i][j] + matrix_2[i][j]

    return m_sum


# Subtraction
def subtract_matrix(matrix_1, matrix_2):
    """
    Subtracts second matrix from the first

        :param matrix_1: The first matrix
        :param matrix_2: The second matrix

        :return: Matrix difference
    """
    rows_matrix_1 = len(matrix_1)
    cols_matrix_1 = len(matrix_1[0])
    rows_matrix_2 = len(matrix_2)
    cols_matrix_2 = len(matrix_2[0])

    if rows_matrix_1 != rows_matrix_2 or cols_matrix_1 != cols_matrix_2:
        raise ArithmeticError("You can't sum matrices of different size.")

    m_sub = zero_matrix(rows_matrix_1, cols_matrix_2)

    for i in range(rows_matrix_1):
        for j in range(cols_matrix_2):
            m_sub[i][j] = matrix_1[i][j] - matrix_2[i][j]

    return m_sub


# Multiplication
def multiply_matrix(matrix_1, matrix_2):
    """
    Multiplies matrix_1 ans matrix_2

        :param matrix_1: The first matrix
        :param matrix_2: The second martix

        :return: Result of multiplication
    """

    rows_matrix_1 = len(matrix_1)
    cols_matrix_1 = len(matrix_1[0])
    rows_matrix_2 = len(matrix_2)
    cols_matrix_2 = len(matrix_2[0])

    if cols_matrix_1 != rows_matrix_2:
        raise ArithmeticError("Number of matrix_1 columns must equals to "
                              "number of matrix_2 rows.")

    m_multiplication = zero_matrix(rows_matrix_1, cols_matrix_2)

    for i in range(rows_matrix_1):
        for j in range(cols_matrix_2):
            result = 0
            for ii in range(cols_matrix_1):
                result += matrix_1[i][ii] * matrix_2[ii][j]
            m_multiplication[i][j] = round(result, 3)

    return m_multiplication


# We can't just divide two matrices but we can multiply one to another ^ (-1)
# Do to this we need few additional functions

# It's important that only square and not singualr matrices can be inverted
# Let's define this operations

# Copy of matrix
def copy_matrix(matrix):
    """
    Creates a copy of a matrix.

        :param matrix: The matrix you want to copy

        :return: A copy of the matrix
    """
    rows = len(matrix)
    cols = len(matrix[0])

    m_copy = zero_matrix(rows, cols)

    for i in range(rows):
        for j in range(cols):
            m_copy[i][j] = matrix[i][j]

    return m_copy


# Check matrix for squareness
def is_squared(matrix):
    """
    Checks if matrix is squared

        :param matrix: The matrix to check
    """
    if len(matrix) != len(matrix[0]):
        raise ArithmeticError('Matrix must be square to inverse.')


# Check matrix for singularity
def is_not_singular(matrix):
    """
    Checks if matrix not singular

        :param matrix: The matrix to check

        :return: Determinant of the matrix or raise an ArithmeticError
    """
    m_det = determinant_matrix(matrix)
    if m_det != 0:
        return m_det
    else:
        raise ArithmeticError('The matrix is singular.')


# Identity matrix (square matrix with ones on the diagonal)
def identity_matrix(size):
    """
    Creates a square identity matrix.

        :param size: the square size of the matrix

        :return: a square identity matrix
    """
    id_matrix = zero_matrix(size, size)
    for i in range(size):
        id_matrix[i][i] = 1

    return id_matrix


# Matrix inversion (matrix ^ (-1))
def invert_matrix(matrix):
    """
    Returns the inverse of the passed in matrix.
        :param matrix: The matrix to be inverted

        :return: The inverse of the matrix A
    """
    # Note that we only can invert squared and non singular matrices
    # dg: diagonal of the matrix
    is_squared(matrix)
    is_not_singular(matrix)

    n = len(matrix)
    new_m = copy_matrix(matrix)
    id_m = identity_matrix(n)
    new_id = copy_matrix(id_m)

    indices = list(range(n))
    for dg in range(n):
        diagonal = 1 / new_m[dg][dg]
        for j in range(n):
            new_m[dg][j] *= diagonal
            new_id[dg][j] *= diagonal
        for i in indices[0:dg] + indices[dg + 1:]:
            scaler = new_m[i][dg]
            for j in range(n):
                new_m[i][j] = new_m[i][j] - scaler * new_m[dg][j]
                new_id[i][j] = new_id[i][j] - scaler * new_id[dg][j]

    return new_id


# Now we can define 'division' of matrices
def divide_matrix(matrix_1, matrix_2):
    """
    We can't divide two matrices but we can
    multiply matrix_1 ans matrix_2 ^ (-1)

        :param matrix_1: The first matrix
        :param matrix_2: The second matrix

        :return: Result of multiplication
    """
    inv_matrix = invert_matrix(matrix_2)

    rows_matrix_1 = len(matrix_1)
    cols_matrix_1 = len(matrix_1[0])
    rows_matrix_2 = len(matrix_2)
    cols_matrix_2 = len(matrix_2[0])

    if cols_matrix_1 != rows_matrix_2:
        raise ArithmeticError("Number of matrix_1 columns must equals to "
                              "number of matrix_2 rows.")

    m_multiplication = zero_matrix(rows_matrix_1, cols_matrix_2)

    for i in range(rows_matrix_1):
        for j in range(cols_matrix_2):
            result = 0
            for ii in range(cols_matrix_1):
                result += matrix_1[i][ii] * inv_matrix[ii][j]
            m_multiplication[i][j] = round(result, 3)

    return m_multiplication


# Transpose of matrix
def transpose_matrix(matrix):
    """
    Return a transposed matrix

        :param matrix: The matrix to transpose

        :return: The transpose of the matrix
    """
    if not isinstance(matrix[0], list):
        matrix = [matrix]

    rows = len(matrix)
    cols = len(matrix[0])

    m_transposed = zero_matrix(cols, rows)

    for i in range(rows):
        for j in range(cols):
            m_transposed[j][i] = matrix[i][j]

    return m_transposed


# Determinant of matrix
def determinant_matrix(matrix):
    """
    Finds the determinant of a square matrix

        :param matrix: The matrix to find the determinant

        :return: The determinant
    """
    x = len(matrix)
    new_matrix = copy_matrix(matrix)

    for dg in range(x):
        if new_matrix[dg][dg] == 0:
            new_matrix[dg][dg] = 1.0e-18
        for i in range(dg+1, x):
            scaler = new_matrix[i][dg] / new_matrix[dg][dg]
            for j in range(x):
                new_matrix[i][j] = new_matrix[i][j] - scaler * new_matrix[dg][j]

    result = 1
    for i in range(x):
        result *= new_matrix[i][i]

    return result


# Bonus! Print the matrix by rows
def print_matrix(matrix):
    """
    Prints a matrix

        :param matrix: The matrix to print
    """
    for row in matrix:
        print([x + 0 for x in row])
