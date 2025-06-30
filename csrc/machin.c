#include "machin.h"

// Implements Machin's formula for approximating pi

#include <math.h>
#include <stdio.h>

// Internal computation using float precision. Returns an array of PiResult.

#include "util.h"
PiResult* run_machin_f(float eps, unsigned long* len) {
    PiResult* results = malloc(MAX_ITER * sizeof(PiResult));
    if (!results) return NULL;

    const float x1 = 1.0f / 5.0f;    // x for atan(1/5)
    const float x2 = 1.0f / 239.0f;  // x for atan(1/239)

    float pow1 = x1;  // current power of x1^(2k+1)
    float pow2 = x2;  // current power of x2^(2k+1)
    float atan1 = 0.0f;
    float atan2 = 0.0f;

    for (unsigned long k = 0; k < MAX_ITER; ++k) {
        float sign = (k % 2 == 0) ? 1.0f : -1.0f;
        atan1 += sign * pow1 / (2.0f * k + 1.0f);
        atan2 += sign * pow2 / (2.0f * k + 1.0f);

        float pi = 4.0f * (4.0f * atan1 - atan2);
        results[k].k = k;
        results[k].pi = pi;

        pow1 *= x1 * x1;
        pow2 *= x2 * x2;
        if ((pi - M_PI) * (pi - M_PI) < eps) {
            *len = k + 1;
            return results;
        }
    }
    *len = MAX_ITER;
    return results;
}

// Internal computation using double precision. Returns an array of PiResult.
PiResult* run_machin_d(double eps, unsigned long* len) {
    PiResult* results = malloc(MAX_ITER * sizeof(PiResult));
    if (!results) return NULL;

    const double x1 = 1.0 / 5.0;    // x for atan(1/5)
    const double x2 = 1.0 / 239.0;  // x for atan(1/239)

    double pow1 = x1;  // current power x1^(2k+1)
    double pow2 = x2;  // current power x2^(2k+1)
    double atan1 = 0.0;
    double atan2 = 0.0;

    for (unsigned long k = 0; k < MAX_ITER; ++k) {
        double sign = (k % 2 == 0) ? 1.0 : -1.0;
        atan1 += sign * pow1 / (2.0 * k + 1.0);
        atan2 += sign * pow2 / (2.0 * k + 1.0);

        double pi = 4.0 * (4.0 * atan1 - atan2);
        results[k].k = k;
        results[k].pi = pi;

        pow1 *= x1 * x1;
        pow2 *= x2 * x2;
        if ((pi - M_PI) * (pi - M_PI) < eps) {
            *len = k + 1;
            return results;
        }
    }
    *len = MAX_ITER;
    return results;
}

