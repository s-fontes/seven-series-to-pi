#include "bbp.h"

// Implements the Bailey-Borwein-Plouffe (BBP) series for approximating pi

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "pi_series.h"
#include "util.h"

// Internal computation using float precision.
PiResult* run_bbp_f(float eps, unsigned long* len) {
    PiResult* results = malloc(MAX_ITER * sizeof(PiResult));
    if (!results) return NULL;

    float pi = 0.0f;
    float pow16 = 1.0f;  // 16^k

    for (unsigned long k = 0; k < MAX_ITER; ++k) {
        float term = (4.0f / (8.0f * k + 1.0f) - 2.0f / (8.0f * k + 4.0f) -
                      1.0f / (8.0f * k + 5.0f) - 1.0f / (8.0f * k + 6.0f)) /
                     pow16;
        pi += term;
        results[k].k = k;
        results[k].pi = pi;
        pow16 *= 16.0f;
        if ((pi - M_PI) * (pi - M_PI) < eps) {
            *len = k + 1;
            return results;
        }
    }
    *len = MAX_ITER;
    return results;
}

// Internal computation using double precision.
PiResult* run_bbp_d(double eps, unsigned long* len) {
    PiResult* results = malloc(MAX_ITER * sizeof(PiResult));
    if (!results) return NULL;

    double pi = 0.0;
    double pow16 = 1.0;  // 16^k

    for (unsigned long k = 0; k < MAX_ITER; ++k) {
        double term = (4.0 / (8.0 * k + 1.0) - 2.0 / (8.0 * k + 4.0) - 1.0 / (8.0 * k + 5.0) -
                       1.0 / (8.0 * k + 6.0)) /
                      pow16;
        pi += term;
        results[k].k = k;
        results[k].pi = pi;
        pow16 *= 16.0;
        if ((pi - M_PI) * (pi - M_PI) < eps) {
            *len = k + 1;
            return results;
        }
    }
    *len = MAX_ITER;
    return results;
}

