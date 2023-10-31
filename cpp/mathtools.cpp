#include "mathtools.h"
#include <cmath>
#include "common.h"

// All functions in this file should be able to compile
// to the highest SIMD (SSE2-AVX512) available on the
// platform.

f32 dotProduct(f32 v1[], f32 v2[], u64 len) {
    f32 ax = 0;
    for (u64 i = 0; i < len; ++i) {
        ax += v1[i] * v2[i];
    }
    return ax;
}

f32 vectorMagnitude(f32 v[], u64 len) {
    f32 magsq = 0;
    for (u64 i = 0; i < len; ++i) {
        f32 stack = v[i];
        magsq += stack*stack;
    }
    return std::sqrt(magsq);
}

void makeVectorUnitInPlace(f32 v[], u64 len) {
    f32 mag = vectorMagnitude(v, len);
    for (u64 i = 0; i < len; ++i) {
        v[i] /= mag;  
    }
}