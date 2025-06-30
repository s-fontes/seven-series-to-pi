#include "euler.h"

// Implements the Basel (Euler) series for approximating pi.
// The loop counter starts at k = 0 while the mathematical
// series index begins at 1.

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "util.h"

PiResult* run_euler_f(float eps, unsigned long* len) {
    PiResult* results = malloc(MAX_ITER * sizeof(PiResult));
    if (!results) return NULL;

    float sum = 0.0f;
    for (unsigned long k = 0; k < MAX_ITER; ++k) {
        unsigned long n = k + 1;  // series index starts at 1
        sum += 1.0f / (float)(n * n);
        float pi = sqrtf(6.0f * sum);
        results[k].k = k;
        results[k].pi = pi;
        if ((pi - M_PI) * (pi - M_PI) < eps) {
            *len = k + 1;
            return results;
        }
    }
    *len = MAX_ITER;
    return results;
}

PiResult* run_euler_d(double eps, unsigned long* len) {
    PiResult* results = malloc(MAX_ITER * sizeof(PiResult));
    if (!results) return NULL;

    double sum = 0.0;
    for (unsigned long k = 0; k < MAX_ITER; ++k) {
        unsigned long n = k + 1;
        sum += 1.0 / (double)(n * n);
        double pi = sqrt(6.0 * sum);
        results[k].k = k;
        results[k].pi = pi;
        if ((pi - M_PI) * (pi - M_PI) < eps) {
            *len = k + 1;
            return results;
        }
    }
    *len = MAX_ITER;
    return results;
}

