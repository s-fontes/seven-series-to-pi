#ifndef NILAKANTHA_H
#define NILAKANTHA_H

#ifdef __cplusplus
extern "C" {
#endif

#include "pi_series.h"

PiResult* run_nilakantha_f(float eps, unsigned long* len);
PiResult* run_nilakantha_d(double eps, unsigned long* len);

#ifdef __cplusplus
}
#endif

#endif  // NILAKANTHA_H
