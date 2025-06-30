#include "nilakantha.h"

// Implements the Nilakantha series for approximating pi

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "util.h"

/*
 * Compute \pi via the Nilakantha series:
 *   \pi = 3 + \sum_{k=1}^N 4 (-1)^{k+1} / ((2k)(2k+1)(2k+2))
 * The implementation iterates from k = 0, mapping to series term k + 1.
 * Results are returned as an array of PiResult for Python interoperability.
 */
PiResult* run_nilakantha_f(float eps, unsigned long* len) {
    PiResult* results = malloc(MAX_ITER * sizeof(PiResult));
    if (!results) return NULL;

    float pi = 3.0f;
    for (unsigned long k = 0; k < MAX_ITER; ++k) {
        unsigned long n = k + 1;  // Nilakantha series starts at k=1
        float term = 4.0f / ((2.0f * n) * (2.0f * n + 1.0f) * (2.0f * n + 2.0f));
        pi += (n % 2 == 1) ? term : -term;
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

PiResult* run_nilakantha_d(double eps, unsigned long* len) {
    PiResult* results = malloc(MAX_ITER * sizeof(PiResult));
    if (!results) return NULL;

    double pi = 3.0;
    for (unsigned long k = 0; k < MAX_ITER; ++k) {
        unsigned long n = k + 1;
        double term = 4.0 / ((2.0 * n) * (2.0 * n + 1.0) * (2.0 * n + 2.0));
        pi += (n % 2 == 1) ? term : -term;
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

