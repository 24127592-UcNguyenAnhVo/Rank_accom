# SO SÁNH CODE VỚI FLOWCHART

**Author:** 24127592-UcNguyenAnhVo  
**Created:** 2024-11-14  
**Last Updated:** 2025-01-17  
**Version:** 1.1.0

---

## MỤC ĐÍCH

Chứng minh **code implementation khớp 100%** với flowchart thiết kế.

---

## BẢNG SO SÁNH

| Flowchart | Code | ✅ |
|-----------|------|---|
| **VALIDATION** |||
| Check empty | `if not accommodations: return []` | ✅ |
| **PREPARATION** |||
| Extract tags | `required_tags = search_request.get('tags', [])` | ✅ |
| Extract type | `search_type = search_request.get('type', '')` | ✅ |
| Define weights | `tag_weights = {'hotel': 3, 'beach': 3, 'pool': 2, ...}` | ✅ |
| **SCORING** |||
| FOR EACH | `for acc in accommodations:` | ✅ |
| Base +5.0 | `score += 5.0` | ✅ |
| Proximity | `proximity = 10.0 * math.exp(-distance / 2.0)` | ✅ |
| Tags intersection | `matching = acc_tags & required_tags_set` | ✅ |
| Tags sum | `for tag in matching: tag_score += weight` | ✅ |
| Tags cap | `tag_score = min(tag_score, 15.0)` | ✅ |
| Type match | `if acc.get('type') == search_type: score += 5.0` | ✅ |
| Name length | `if len > 20: +3 elif len > 10: +2 else: +1` | ✅ |
| Round | `acc['score'] = round(score, 2)` | ✅ |
| **RANKING** |||
| Sort DESC | `sorted(..., key=lambda x: x['score'], reverse=True)` | ✅ |
| Top-5 | `top_results = sorted_accs[:5]` | ✅ |
| Assign ranks | `for i, acc in enumerate(top): acc['rank'] = i + 1` | ✅ |

**Kết quả:** 16/16 bước = **100%**

---

## VÍ DỤ TRACE

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

### Tính toán:
```
Base:      5.0
Proximity: 10 × e^(-0.6) = 5.49
Tags:      beach(3) + pool(2) = 5.0
Type:      resort match → 5.0
Name:      len(20) → 2.0
─────────────────────────────
TOTAL:     22.49 → rank 1
```

### Output:
```json
[{
  "name": "Sunset Beach Resort",
  "distance": 1.2,
  "tags": ["resort", "beach", "pool", "spa"],
  "type": "resort",
  "score": 22.49,
  "rank": 1
}]
```

✅ **Khớp 100% với flowchart prediction!**

---

## EDGE CASES

| Case | Flowchart | Code | Match |
|------|-----------|------|-------|
| Empty list | Return `[]` | `return []` | ✅ |
| Single item | Rank 1 | `rank = 1` | ✅ |
| Tie scores | Stable sort | Timsort stable | ✅ |
| < 5 items | Return all | `[:5]` returns all | ✅ |
| > 5 items | Top 5 only | `[:5]` slices | ✅ |

---

## KẾT LUẬN

```
╔═══════════════════════════════════════╗
║  CODE ✅ FLOWCHART                    ║
║  Match rate: 100% (16/16 steps)      ║
║  Edge cases: All verified            ║
║  Logic: Identical                    ║
╚═══════════════════════════════════════╝
```

---

**Related documents:**
- 🗺️ [Main Flowchart](./flowchart_main.md)
- 🔍 [Component Details](./flowchart_components.md)

---

**Last Updated:** 2025-01-17  
**Maintained By:** 24127592-UcNguyenAnhVo
