# PHÂN TÍCH ĐỘ PHỨC TẠP

**Author:** 24127592-UcNguyenAnhVo  
**Date:** 2025-11-14

---

## 1. TIME COMPLEXITY (Độ phức tạp thời gian)

### Phân tích từng phase:

```
┌───────────────────────────────────────────────────────────────────┐
│ PHASE                          │ OPERATIONS        │ COMPLEXITY   │
├────────────────────────────────┼───────────────────┼──────────────┤
│ 1. Input Validation            │ Check empty       │ O(1)         │
│ 2. Extract Data                │ Get dict values   │ O(1)         │
│ 3. Scoring Loop                │ For each acc      │ O(n × m)     │
│    - Base score                │   Constant        │   O(1)       │
│    - Proximity                 │   Math.exp()      │   O(1)       │
│    - Tag matching              │   Set ∩           │   O(m)       │
│    - Type check                │   Comparison      │   O(1)       │
│    - Name check                │   Length          │   O(1)       │
│ 4. Sorting (Timsort)           │ Sort n items      │ O(n log n)   │
│ 5. Top-5 Selection             │ Slice [0:5]       │ O(1)         │
│ 6. Rank Assignment             │ Loop 5 times      │ O(1)         │
│ 7. Return                      │ Return list       │ O(1)         │
└───────────────────────────────────────────────────────────────────┘

Trong đó:
- n = số lượng accommodations
- m = số lượng tags trung bình (thường m << 10, xem như constant)
```

### Kết luận Time Complexity:

```
T(n) = O(1) + O(1) + O(n×m) + O(n log n) + O(1) + O(1) + O(1)
     = O(n×m) + O(n log n)

Vì m là constant (thường ≤ 10):
     = O(n) + O(n log n)
     = O(n log n)  ← DOMINATED BY SORTING

→ TOTAL TIME COMPLEXITY: O(n log n)
```

---

## 2. SPACE COMPLEXITY (Độ phức tạp không gian)

### Phân tích bộ nhớ:

```
┌───────────────────────────────────────────────────────────────────┐
│ VARIABLE                       │ SIZE              │ COMPLEXITY   │
├────────────────────────────────┼───────────────────┼──────────────┤
│ tag_weights (dict)             │ ~20 entries       │ O(1)         │
│ acc_tags (set)                 │ ≤ m tags          │ O(m)         │
│ required_tags_set (set)        │ ≤ m tags          │ O(m)         │
│ matching_tags (set)            │ ≤ m tags          │ O(m)         │
│ sorted_accs (list)             │ n items           │ O(n)         │
│ top_results (list)             │ 5 items           │ O(1)         │
│ Timsort temp space             │ n/2 worst case    │ O(n)         │
└───────────────────────────────────────────────────────────────────┘

Vì m là constant:
```

### Kết luận Space Complexity:

```
S(n) = O(1) + O(m) + O(m) + O(m) + O(n) + O(1) + O(n)
     = O(n) + O(m)
     
Vì m << n:
     = O(n)

→ TOTAL SPACE COMPLEXITY: O(n)
```

---

## 3. SO SÁNH VỚI THUẬT TOÁN KHÁC

### 3.1. Linear Search (Không sort)

```
Algorithm: Tìm Top-5 bằng 5 lần scan
Time: O(5n) = O(n)
Space: O(1)

Nhược điểm:
- Phải scan 5 lần
- Không stable
- Code phức tạp hơn
```

### 3.2. Heap-based Selection (Priority Queue)

```
Algorithm: Min-heap size 5
Time: O(n log 5) = O(n)
Space: O(5) = O(1)

Ưu điểm:
- Nhanh hơn khi n rất lớn
- Space efficient

Nhược điểm:
- Code phức tạp
- Constant factor lớn hơn
- Chỉ tốt khi n > 10,000
```

### 3.3. Full Sort (Timsort - SELECTED) ✅

```
Algorithm: Sort toàn bộ rồi lấy top 5
Time: O(n log n)
Space: O(n)

Ưu điểm:
- Code đơn giản
- Stable sort
- Tối ưu cho n < 10,000
- Python built-in (highly optimized)

Lý do chọn:
- n thường < 100 (kết quả search OSM)
- O(n log n) vs O(n): chênh lệch nhỏ với n nhỏ
- Timsort rất nhanh với real-world data
```

---

## 4. BEST/AVERAGE/WORST CASE

### 4.1. Best Case

```
Scenario: Data đã sorted sẵn
Time: O(n) - Timsort adaptive
Space: O(n)

Example:
accommodations = [
    {score: 30}, {score: 25}, {score: 20}, ...
]  // Đã sorted

Timsort nhận diện → O(n)
```

### 4.2. Average Case

```
Scenario: Data random order
Time: O(n log n)
Space: O(n)

Most common case trong production
```

### 4.3. Worst Case

```
Scenario: Data reverse sorted
Time: O(n log n)
Space: O(n)

Example:
accommodations = [
    {score: 1}, {score: 2}, {score: 3}, ...
]  // Ngược chiều

Timsort vẫn O(n log n)
```

---

## 5. BIG-O NOTATION SUMMARY

```
┌─────────────────────────────────────────────────────────────┐
│                    COMPLEXITY ANALYSIS                      │
├─────────────────────────────────────────────────────────────┤
│ Time Complexity:                                            │
│   - Best Case:    O(n)        (sorted input)                │
│   - Average Case: O(n log n)  (random input)                │
│   - Worst Case:   O(n log n)  (reverse sorted)              │
│                                                             │
│ Space Complexity:                                           │
│   - Auxiliary:    O(n)        (Timsort temp array)          │
│   - Total:        O(n)                                      │
│                                                             │
│ Stability:        YES (Timsort is stable)                   │
│ In-place:         NO (requires O(n) extra space)            │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. PERFORMANCE BENCHMARKS

### Test với n = 100 accommodations:

```
n = 100
Operations:
- Scoring: 100 iterations × 5 components = 500 ops
- Sorting: 100 log2(100) ≈ 664 comparisons
- Total: ~1,200 operations

Estimated time: < 1ms trên CPU hiện đại
```

### Scalability:

```
┌─────────┬──────────────┬──────────────┬──────────────┐
│    n    │  Operations  │  Time (est)  │  Acceptable? │
├─────────┼──────────────┼──────────────┼──────────────┤
│     10  │        ~70   │     < 0.1ms  │      ✅       │
│    100  │     ~1,200   │     < 1ms    │      ✅       │
│  1,000  │    ~15,000   │     < 10ms   │      ✅       │
│ 10,000  │   ~200,000   │     < 100ms  │      ✅       │
│100,000  │ ~2,500,000   │     ~   1s   │      ⚠️       │
└─────────┴──────────────┴──────────────┴──────────────┘

Kết luận: Tối ưu cho n < 10,000 (typical use case)
```

---

## 7. OPTIMIZATION OPPORTUNITIES

### 7.1. Nếu cần tối ưu cho n rất lớn (> 10,000):

```python
# Option 1: Partial sort (heapq)
import heapq

def rank_results_optimized(accommodations, search_request):
    # Score tất cả - O(n)
    for acc in accommodations:
        acc['score'] = calculate_score(acc, search_request)
    
    # Top-5 bằng heap - O(n log 5) = O(n)
    top_5 = heapq.nlargest(5, accommodations, key=lambda x: x['score'])
    
    return top_5

# Time: O(n) vs O(n log n)
# Improvement: 10x faster khi n = 100,000
```

### 7.2. Nếu gọi nhiều lần với cùng data:

```python
# Option 2: Memoization
from functools import lru_cache

@lru_cache(maxsize=128)
def calculate_proximity_score(distance):
    return 10.0 * math.exp(-distance / 2.0)

# Cache exponential calculations
```

### 7.3. Parallel processing:

```python
# Option 3: Multi-threading cho scoring
from concurrent.futures import ThreadPoolExecutor

def rank_results_parallel(accommodations, search_request):
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Score parallel - O(n/4) with 4 cores
        scored = list(executor.map(
            lambda acc: score_accommodation(acc, search_request),
            accommodations
        ))
    
    # Sort - O(n log n)
    sorted_accs = sorted(scored, key=lambda x: x['score'], reverse=True)
    return sorted_accs[:5]

# Speedup: ~3x với 4 cores
```

---

## 8. REFERENCES

1. **Cormen, T. et al. (2009).** *Introduction to Algorithms (3rd ed.)*
   - Chapter 2: Sorting Algorithms
   - Chapter 6: Heapsort

2. **Python Time Complexity:** https://wiki.python.org/moin/TimeComplexity

3. **Timsort Analysis:** https://github.com/python/cpython/blob/main/Objects/listsort.txt

---

**Tóm tắt:**
- ✅ Time: O(n log n) - Tối ưu cho n < 10,000
- ✅ Space: O(n) - Chấp nhận được
- ✅ Stable sort - Quan trọng cho UX
- ✅ Simple code - Dễ maintain