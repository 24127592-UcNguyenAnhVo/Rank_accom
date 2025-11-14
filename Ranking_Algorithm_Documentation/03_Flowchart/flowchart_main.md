# FLOWCHART TỔNG THỂ - Thuật toán Ranking

**Author:** 24127592-UcNguyenAnhVo  
**Date:** 2025-11-14

---

## FLOWCHART CHÍNH

```mermaid
flowchart TD
    Start([🚀 START<br/>rank_results]) --> Input[📥 INPUT<br/>accommodations[]<br/>search_request{}]
    
    Input --> ValidateEmpty{accommodations<br/>empty?}
    ValidateEmpty -->|Yes| ReturnEmpty↩️ RETURN []]
    ReturnEmpty --> End
    
    ValidateEmpty -->|No| Extract[📦 EXTRACT DATA<br/>required_tags = search_request.tags<br/>search_type = search_request.type]
    
    Extract --> DefineWeights[⚙️ DEFINE TAG WEIGHTS<br/>hotel=3, beach=3, pool=2, wifi=1, ...]
    
    DefineWeights --> InitLoop[🔄 FOR EACH<br/>acc in accommodations]
    
    InitLoop --> InitScore[💯 score = 0.0]
    
    InitScore --> AddBase[➕ Component 1: Base<br/>score += 5.0]
    
    AddBase --> CalcProximity[📏 Component 2: Proximity<br/>distance = acc.distance<br/>proximity = 10 × e^-distance/2<br/>score += proximity]
    
    CalcProximity --> CalcTags[🏷️ Component 3: Tag Match<br/>acc_tags = SET acc.tags<br/>required = SET required_tags<br/>matching = acc_tags ∩ required<br/><br/>tag_score = Σ weight tag<br/>tag_score = MIN tag_score, 15<br/>score += tag_score]
    
    CalcTags --> CheckType{Component 4:<br/>acc.type ==<br/>search_type?}
    
    CheckType -->|Yes| AddType[➕ score += 5.0]
    CheckType -->|No| CheckName
    AddType --> CheckName
    
    CheckName{Component 5:<br/>acc.name ≠<br/>'Unnamed'?}
    
    CheckName -->|No| AssignScore
    CheckName -->|Yes| CheckLength{name length<br/>category?}
    
    CheckLength -->|> 20 chars| Add3[➕ score += 3.0]
    CheckLength -->|> 10 chars| Add2[➕ score += 2.0]
    CheckLength -->|≤ 10 chars| Add1[➕ score += 1.0]
    
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

## GIẢI THÍCH CÁC KÝ HIỆU

### Shapes:

```
([...])     = Start/End (Terminal)
[...]       = Process (Calculation/Operation)
{...}       = Decision (If/Else)
```

### Colors:

```
🟢 Green (#90EE90)  = Start/End/Return
🟡 Yellow (#FFE4B5) = Initialize
🔵 Blue (#87CEEB)   = Calculations
🟠 Orange (#FFA07A) = Decisions
🟣 Purple (#DDA0DD) = Sorting
🟢 Light Green (#98FB98) = Final Selection
```

---

## LUỒNG THỰC THI

### 1. Validation Phase
```
START → Input → Check Empty?
         ├─ Yes → Return []
         └─ No  → Continue
```

### 2. Preparation Phase
```
Extract Data → Define Weights
```

### 3. Scoring Phase (Main Loop)
```
FOR EACH accommodation:
    ├─ Initialize score = 0
    ├─ Add Base (5.0)
    ├─ Calculate Proximity (exponential)
    ├─ Calculate Tag Matches (weighted)
    ├─ Check Type Match (bonus 5.0)
    ├─ Check Name Quality (bonus 1-3)
    └─ Assign final score
```

### 4. Ranking Phase
```
Sort All → Get Top 5 → Assign Ranks (1-5) → Return
```

---

## VÍ DỤ TRACE

### Input:
```
accommodations = [
    {name: 'Hotel A', distance: 0.3, tags: ['hotel', 'beach'], type: 'hotel'}
]
search_request = {type: 'hotel', tags: ['hotel', 'beach']}
```

### Trace:

```
1. START
2. Input: 1 accommodation
3. Empty? No
4. Extract: required_tags = ['hotel', 'beach'], search_type = 'hotel'
5. Define weights: hotel=3, beach=3
6. FOR acc = 'Hotel A':
   6.1. score = 0
   6.2. score += 5.0           → score = 5.0
   6.3. proximity = 10×e^(-0.15) = 8.61
        score += 8.61          → score = 13.61
   6.4. matching = {'hotel', 'beach'}
        tag_score = 3 + 3 = 6
        score += 6             → score = 19.61
   6.5. type match? Yes
        score += 5             → score = 24.61
   6.6. name = 'Hotel A', length = 7
        score += 1             → score = 25.61
   6.7. Assign: acc.score = 25.61
7. More accs? No
8. Sort: [Hotel A: 25.61]
9. Top 5: [Hotel A]
10. Assign rank: Hotel A.rank = 1
11. Return: [{name: 'Hotel A', score: 25.61, rank: 1}]
12. END
```

---

## EDGE CASES XỬ LÝ

### Case 1: Empty List
```
Input: accommodations = []
Flow: START → Input → Empty? Yes → Return [] → END
```

### Case 2: Single Item
```
Input: accommodations = [Hotel A]
Flow: Normal flow → Sort 1 item → Top 1 → Rank = 1
```

### Case 3: Same Score
```
Input: 2 hotels with score = 20.0
Flow: Timsort (stable) → Preserve original order
```

---

## PERFORMANCE METRICS

```
┌─────────────────────────────────────────────────────────┐
│ NODE                    │ TIME COMPLEXITY │ EXECUTIONS │
├─────────────────────────┼─────────────────┼────────────┤
│ Validation              │ O(1)            │ 1          │
│ Extract                 │ O(1)            │ 1          │
│ Define Weights          │ O(1)            │ 1          │
│ Scoring Loop            │ O(n)            │ n          │
│   - Each iteration      │ O(m)            │ n          │
│ Sort                    │ O(n log n)      │ 1          │
│ Top-5                   │ O(1)            │ 1          │
│ Rank Assignment         │ O(1)            │ 1          │
└─────────────────────────────────────────────────────────┘

Total: O(n log n)
```