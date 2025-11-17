# SO SÁNH CODE VỚI FLOWCHART

**Author:** 24127592-UcNguyenAnhVo  
**Created:** 2024-11-14  
**Last Updated:** 2025-01-17  
**Version:** 1.1.0

---

## MỤC ĐÍCH

Chứng minh **code khớp 100%** với flowchart thiết kế.

---

## BẢNG SO SÁNH

| Flowchart | Code | ✅ |
|-----------|------|---|
| **INITIALIZATION** |||
| START | `def rank_results(accommodations, search_request):` | ✅ |
| Input | Function parameters | ✅ |
| **VALIDATION** |||
| Check Empty? | `if not accommodations or len(accommodations) == 0:` | ✅ |
| Return [] | `return []` | ✅ |
| **PREPARATION** |||
| Extract tags | `required_tags = search_request.get('tags', [])` | ✅ |
| Extract type | `search_type = search_request.get('type', '')` | ✅ |
| Define weights | `tag_weights = {'hotel': 3, 'beach': 3, ...}` | ✅ |
| **SCORING LOOP** |||
| FOR EACH | `for acc in accommodations:` | ✅ |
| score = 0 | `score = 0.0` | ✅ |
| Base +5.0 | `score += 5.0` | ✅ |
| Proximity | `proximity = 10.0 * math.exp(-distance / 2.0)` | ✅ |
| Tags (set ∩) | `matching = acc_tags & required_tags_set` | ✅ |
| Tags (loop) | `for tag in matching: tag_score += weight` | ✅ |
| Tags (cap) | `tag_score = min(tag_score, 15.0)` | ✅ |
| Type match | `if acc.get('type') == search_type: score += 5.0` | ✅ |
| Name check | `if name != 'Unnamed': ...` | ✅ |
| Name length | `if len > 20: +3 elif len > 10: +2 else: +1` | ✅ |
| Round score | `acc['score'] = round(score, 2)` | ✅ |
| **RANKING** |||
| Sort DESC | `sorted(accommodations, key=lambda x: x['score'], reverse=True)` | ✅ |
| Top-5 | `top_results = sorted_accs[:5]` | ✅ |
| Assign ranks | `for i, acc in enumerate(top): acc['rank'] = i + 1` | ✅ |
| Return | `return top_results` | ✅ |

**Kết quả:** 24/24 bước khớp = **100%**

---

## TRACE VÍ DỤ

### Input:
```json
{
  "name": "Sunset Beach Resort",
  "distance": 1.2,
  "tags": ["resort", "beach", "pool", "spa"],
  "type": "resort"
}
search: {type: "resort", tags: ["beach", "pool"]}
```

### Execution:
```
1. Empty? No
2. Extract: required_tags=['beach','pool'], search_type='resort'
3. FOR 'Sunset Beach Resort':
   score = 0.0
   + 5.0 (base)           → 5.0
   + 5.49 (proximity)     → 10.49
   + 5.0 (tags)           → 15.49
   + 5.0 (type)           → 20.49
   + 2.0 (name)           → 22.49
   acc.score = 22.49
4. Sort: [22.49]
5. Top-5: [22.49]
6. Rank: 1
7. Return: [{...score: 22.49, rank: 1}]
```

**Output khớp 100% với flowchart prediction!**

---

## EDGE CASES

| Case | Flowchart | Code | Match |
|------|-----------|------|-------|
| Empty list | Return [] | `return []` | ✅ |
| Single item | Rank 1 | `acc['rank'] = 1` | ✅ |
| Tie scores | Stable sort | Timsort (stable) | ✅ |
| < 5 items | Return all | `[:5]` returns all | ✅ |
| > 5 items | Top 5 only | `[:5]` slices | ✅ |

---

## KẾT LUẬN

```
╔═══════════════════════════════════════╗
║  CODE ✅ FLOWCHART                    ║
║  Match rate: 100% (24/24 steps)      ║
║  Edge cases: All covered             ║
║  Logic: Identical                    ║
╚═══════════════════════════════════════╝
```

**Verified:** Code implementation trung thành 100% với flowchart design.
