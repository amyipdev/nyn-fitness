#include "mathtools.h"
#include <cmath>
#include "common.h"

// All functions in this file should be able to compile
// to the highest SIMD (SSE2-AVX512) available on the
// platform.

f64 dotProduct(f64 v1[], f64 v2[], u64 len) {
    f64 ax = 0;
    for (u64 i = 0; i < len; ++i) {
        ax += v1[i] * v2[i];
    }
    return ax;
}

f64 vectorMagnitude(f64 v[], u64 len) {
    f64 magsq = 0;
    for (u64 i = 0; i < len; ++i) {
        f64 stack = v[i];
        magsq += stack*stack;
    }
    return std::sqrt(magsq);
}

void makeVectorUnitInPlace(f64 v[], u64 len) {
    f64 mag = vectorMagnitude(v, len);
    for (u64 i = 0; i < len; ++i) {
        v[i] /= mag;  
    }
}