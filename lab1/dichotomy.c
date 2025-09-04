#include <stdio.h>

static double f(double x)
{
    return x * x + 2;
}

static double dichotomy_min_search(double (*f)(double),
        double eps, double delta, double a, double b)
{
    eps /= 2;
    while (b - a >= delta) {
        double mid = (a + b) / 2;

        double y = mid - eps;
        double fy = f(y);

        double z = mid + eps;
        double fz = f(z);

        if (fy < fz) {
            b = z;
        } else if (fy > fz) {
            a = y;
        } else {
            a = y;
            b = z;
        }
    }
    return (a + b) / 2;
}

int main()
{
    double x = dichotomy_min_search(f, 0.5, 1, -3, 7);
    printf("x = %f, f(x) = %f\n", x, f(x));
    return 0;
}
