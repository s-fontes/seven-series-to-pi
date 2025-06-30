#include "chudnovsky.h"

// Implements the Chudnovsky series for approximating pi

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "pi_series.h"
#include "util.h"

// Internal computation using float precision.
PiResult* run_chudnovsky_f(float eps, unsigned long* len) {
    PiResult* results = malloc(MAX_ITER * sizeof(PiResult));
    if (!results) return NULL;

    const float base = 640320.0f;
    const float base_cubed = base * base * base;  // 640320^3
    const float sqrt_term = base * sqrtf(base);   // 640320^(3/2)
    float pow_base = 1.0f;                        // current base^(3k)
    float sum = 0.0f;

    for (unsigned long k = 0; k < MAX_ITER; ++k) {
        float sign = (k % 2 == 0) ? 1.0f : -1.0f;
        float num = tgammaf(6.0f * k + 1.0f) * (545140134.0f * k + 13591409.0f);
        float kfact = tgammaf(k + 1.0f);
        float denom = tgammaf(3.0f * k + 1.0f) * kfact * kfact * kfact * pow_base * sqrt_term;
        float term = sign * num / denom;
        sum += term;

        float pi_val = 1.0f / (12.0f * sum);
        results[k].k = k;
        results[k].pi = pi_val;

        pow_base *= base_cubed;
        if ((pi_val - M_PI) * (pi_val - M_PI) < eps) {
            *len = k + 1;
            return results;
        }
    }
    *len = MAX_ITER;
    return results;
}

// Internal computation using double precision.
PiResult* run_chudnovsky_d(double eps, unsigned long* len) {
    PiResult* results = malloc(MAX_ITER * sizeof(PiResult));
    if (!results) return NULL;

    const double base = 640320.0;
    const double base_cubed = base * base * base;
    const double sqrt_term = base * sqrt(base);
    double pow_base = 1.0;
    double sum = 0.0;

    for (unsigned long k = 0; k < MAX_ITER; ++k) {
        double sign = (k % 2 == 0) ? 1.0 : -1.0;
        double num = tgamma(6.0 * k + 1.0) * (545140134.0 * k + 13591409.0);
        double kfact = tgamma(k + 1.0);
        double denom = tgamma(3.0 * k + 1.0) * kfact * kfact * kfact * pow_base * sqrt_term;
        double term = sign * num / denom;
        sum += term;

        double pi_val = 1.0 / (12.0 * sum);
        results[k].k = k;
        results[k].pi = pi_val;

        pow_base *= base_cubed;
        if ((pi_val - M_PI) * (pi_val - M_PI) < eps) {
            *len = k + 1;
            return results;
        }
    }
    *len = MAX_ITER;
    return results;
}

// Convenience wrappers that write CSV output.
