# FLOWCHART TỔNG THỂ - Thuật toán Ranking

**Author:** 24127592-UcNguyenAnhVo  
**Created:** 2024-11-14  
**Last Updated:** 2025-01-17  
**Version:** 1.1.0

---

## FLOWCHART CHÍNH

```mermaid
flowchart TD
    Start([🚀 START<br/>rank_results]) --> Input[📥 INPUT<br/>accommodations[]<br/>search_request{}]
    
    Input --> ValidateEmpty{accommodations<br/>empty?}
    ValidateEmpty -->|Yes| ReturnEmpty[↩️ RETURN []]
    ReturnEmpty --> End
    
    ValidateEmpty -->|No| Extract[📦 EXTRACT DATA<br/>required_tags = search_request.tags<br/>search_type = search_request.type]
    
    Extract --> DefineWeights[⚙️ DEFINE TAG WEIGHTS<br/>hotel=3, beach=3, pool=2, wifi=1, ...]
    
    DefineWeights --> InitLoop[🔄 FOR EACH<br/>acc in accommodations]
    
    InitLoop --> InitScore[💯 score = 0.0]
    
    InitScore --> AddBase[➕ Component 1: Base<br/>score += 5.0]
    
    AddBase --> CalcProximity[📏 Component 2: Proximity<br/>distance = acc.distance<br/>proximity = 10 × e^(-distance/2)<br/>score += proximity]
    
    CalcProximity --> CalcTags[🏷️ Component 3: Tag Match<br/>matching = acc.tags ∩ required<br/>tag_score = Σ weights<br/>capped at 15.0<br/>score += tag_score]
    
    CalcTags --> CheckType{Component 4:<br/>acc.type ==<br/>search_type?}
    
    CheckType -->|Yes| AddType[➕ score += 5.0]
    CheckType -->|No| CheckName
    AddType --> CheckName
    
    CheckName{Component 5:<br/>acc.name ≠<br/>'Unnamed'?}
    
    CheckName -->|No| AssignScore
    CheckName -->|Yes| CheckLength{name length?}
    
    CheckLength -->|> 20 chars| Add3[➕ score += 3.0]
    CheckLength -->|10-20 chars| Add2[➕ score += 2.0]
    CheckLength -->|< 10 chars| Add1[➕ score += 1.0]
    
    Add3 --> AssignScore
    Add2 --> AssignScore
    Add1 --> AssignScore
    
    AssignScore[💾 acc.score = ROUND score, 2]
    
    AssignScore --> LoopCheck{More<br/>accommodations?}
    LoopCheck -->|Yes| InitLoop
    
    LoopCheck -->|No| Sort[📊 SORT Timsort<br/>sorted_accs = SORT accommodations,<br/>KEY=score, DESC]
    
    Sort --> GetTop5[🔝 TOP-5 SELECTION<br/>top_results = sorted_accs[0:5]]
    
    GetTop5 --> RankLoop[🔄 FOR i = 0 to 4]
    
    RankLoop --> AssignRank[🏆 top_results[i].rank = i + 1]
    
    AssignRank --> RankCheck{i < 4?}
    RankCheck -->|Yes| RankLoop
    
    RankCheck -->|No| Return[↩️ RETURN top_results]
    
    Return --> End([✅ END])
    
    style Start fill:#90EE90
    style End fill:#90EE90
    style InitScore fill:#FFE4B5
    style AddBase fill:#87CEEB
    style CalcProximity fill:#87CEEB
    style CalcTags fill:#87CEEB
    style CheckType fill:#FFA07A
    style CheckName fill:#FFA07A
    style CheckLength fill:#FFA07A
    style Sort fill:#DDA0DD
    style GetTop5 fill:#98FB98
    style Return fill:#90EE90
```

---

## LUỒNG THỰC THI

```
1. Validation:  START → Check Empty → Continue/Return []
2. Preparation: Extract tags, type → Define weights
3. Scoring:     FOR EACH acc → Calculate 5 components → Assign score
4. Ranking:     Sort DESC → Get Top 5 → Assign ranks 1-5 → Return
```

---

## SCORING COMPONENTS

```
Total Score = Base + Proximity + Tags + Type + Name
              5.0  + 0-10.0   + 0-15.0 + 0/5 + 0-3

Min: 5.0  | Max: 38.0  | Typical: 15-30
```

---

## TAG WEIGHTS

| Tag | Weight | Tag | Weight | Tag | Weight |
|-----|--------|-----|--------|-----|--------|
| hotel | 3 | pool | 2 | wifi | 1 |
| beach | 3 | spa | 2 | parking | 1 |
| resort | 3 | restaurant | 2 | gym | 1 |
| beachfront | 3 | bar | 2 | others | 1 |

**Max tag score:** 15.0 (capped)

---

## VÍ DỤ

### Input:
```json
{
  "name": "Sunset Beach Resort",
  "distance": 1.2,
  "tags": ["resort", "beach", "pool", "spa"],
  "type": "resort"
}
search_request: {type: "resort", tags: ["beach", "pool"]}
```

### Calculation:
```
Base:      5.0
Proximity: 10 × e^(-0.6) = 5.49
Tags:      beach(3) + pool(2) = 5.0
Type:      resort == resort → 5.0
Name:      len(20) → 2.0
─────────────────────────────
TOTAL:     22.49 (rank: 1)
```

---

## EDGE CASES

| Case | Behavior |
|------|----------|
| Empty list | Return `[]` |
| Single item | Return 1 item with rank 1 |
| Tie scores | Stable sort (preserve order) |
| < 5 items | Return all with ranks |
| > 5 items | Return top 5 only |

---

## PERFORMANCE

```
Time:  O(n log n)  ← Dominated by Timsort
Space: O(n)
```

---

**See also:**  
- [Components Detail](./flowchart_components.md)  
- [Code Comparison](./flowchart_comparison.md)
