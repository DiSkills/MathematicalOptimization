#include <math.h>
#include <stdio.h>

static double f(double x)
{
    return x * x + 2;
}

static double golden_ratio_min_search(double (*f)(double),
        double delta, double a, double b)
{
    double y = a + (3 - sqrt(5)) / 2.0 * (b - a);
    double z = a + b - y;

    while (b - a >= delta) {
        double fy = f(y);
        double fz = f(z);
        if (fy <= fz) {
            b = z;
            z = y;
            y = a + b - y;
        } else {
            a = y;
            y = z;
            z = a + b - z;
        }
    }
    return (a + b) / 2;
}

int main()
{
    double x = golden_ratio_min_search(f, 0.2, -3, 7);
    printf("x = %f, f(x) = %f\n", x, f(x));
    return 0;
}
