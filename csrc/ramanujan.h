#ifndef RAMANUJAN_H
#define RAMANUJAN_H

#ifdef __cplusplus
extern "C" {
#endif

#include "pi_series.h"

PiResult* run_ramanujan_f(float eps, unsigned long* len);
PiResult* run_ramanujan_d(double eps, unsigned long* len);

#ifdef __cplusplus
}
#endif

#endif  // RAMANUJAN_H
