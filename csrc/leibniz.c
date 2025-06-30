#include "leibniz.h"

// Implements the Leibniz series for approximating pi

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "pi_series.h"
#include "util.h"

PiResult* run_leibniz_f(float eps, unsigned long* len) {
    PiResult* results = malloc(MAX_ITER * sizeof(PiResult));
    if (!results) return NULL;

    float sum = 0.0f;
    for (unsigned long k = 0; k < MAX_ITER; ++k) {
        float term = (k % 2 == 0 ? 1.0f : -1.0f) / (2.0f * k + 1.0f);
        sum += term;
        double pi_val = 4.0f * sum;
        results[k].k = k;
        results[k].pi = pi_val;
        if ((pi_val - M_PI) * (pi_val - M_PI) < eps) {
            *len = k + 1;
            return results;
        }
    }
    *len = MAX_ITER;
    return results;
}

PiResult* run_leibniz_d(double eps, unsigned long* len) {
    PiResult* results = malloc(MAX_ITER * sizeof(PiResult));
    if (!results) return NULL;

    double sum = 0.0;
    for (unsigned long k = 0; k < MAX_ITER; ++k) {
        double term = (k % 2 == 0 ? 1.0 : -1.0) / (2.0 * k + 1.0);
        sum += term;
        double pi_val = 4.0 * sum;
        results[k].k = k;
        results[k].pi = pi_val;
        if ((pi_val - M_PI) * (pi_val - M_PI) < eps) {
            *len = k + 1;
            return results;
        }
    }
    *len = MAX_ITER;
    return results;
}
