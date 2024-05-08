def compute_area(a, b, c, d, alpha) :
    p = 0.5 * (a + b + c + d)
    return ((p - a) * (p - b) * (p - c) * (p - d) - a * b * c * d * (cos(alpha) ** 2)) ** 0.5