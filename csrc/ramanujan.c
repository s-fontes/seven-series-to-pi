#include "ramanujan.h"

// Implements Ramanujan's series for approximating pi

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "util.h"

PiResult* run_ramanujan_f(float eps, unsigned long* len) {
    PiResult* results = malloc(MAX_ITER * sizeof(PiResult));
    if (!results) return NULL;

    const float factor = (2.0f * sqrtf(2.0f)) / 9801.0f;
    const float base_pow = 396.0f * 396.0f * 396.0f * 396.0f;
    float pow396 = 1.0f;
    float sum = 0.0f;

    for (unsigned long k = 0; k < MAX_ITER; ++k) {
        float num = tgammaf(4.0f * k + 1.0f) * (1103.0f + 26390.0f * k);
        float kfact = tgammaf(k + 1.0f);
        float denom = kfact * kfact * kfact * kfact * pow396;
        sum += num / denom;

        double S = (double)factor * (double)sum;
        double pi = 1.0 / S;
        results[k].k = k;
        results[k].pi = pi;

        pow396 *= base_pow;
        if ((pi - M_PI) * (pi - M_PI) < eps) {
            *len = k + 1;
            return results;
        }
    }
    *len = MAX_ITER;
    return results;
}

PiResult* run_ramanujan_d(double eps, unsigned long* len) {
    PiResult* results = malloc(MAX_ITER * sizeof(PiResult));
    if (!results) return NULL;

    const double factor = (2.0 * sqrt(2.0)) / 9801.0;
    const double base_pow = 396.0 * 396.0 * 396.0 * 396.0;
    double pow396 = 1.0;
    double sum = 0.0;

    for (unsigned long k = 0; k < MAX_ITER; ++k) {
        double num = tgamma(4.0 * k + 1.0) * (1103.0 + 26390.0 * k);
        double kfact = tgamma(k + 1.0);
        double denom = kfact * kfact * kfact * kfact * pow396;
        sum += num / denom;

        double S = factor * sum;
        double pi = 1.0 / S;
        results[k].k = k;
        results[k].pi = pi;

        pow396 *= base_pow;
        if ((pi - M_PI) * (pi - M_PI) < eps) {
            *len = k + 1;
            return results;
        }
    }
    *len = MAX_ITER;
    return results;
}

