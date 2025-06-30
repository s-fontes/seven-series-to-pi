#ifndef BBP_H
#define BBP_H

#ifdef __cplusplus
extern "C" {
#endif

#include "pi_series.h"

PiResult* run_bbp_f(float eps, unsigned long* len);
PiResult* run_bbp_d(double eps, unsigned long* len);

#ifdef __cplusplus
}
#endif

#endif  // BBP_H
