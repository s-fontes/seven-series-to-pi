#ifndef EULER_H
#define EULER_H

#ifdef __cplusplus
extern "C" {
#endif

#include "pi_series.h"

PiResult* run_euler_f(float eps, unsigned long* len);
PiResult* run_euler_d(double eps, unsigned long* len);

#ifdef __cplusplus
}
#endif

#endif  // EULER_H
