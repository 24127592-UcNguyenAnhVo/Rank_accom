# FLOWCHART CHI TIẾT TỪNG COMPONENT

**Author:** 24127592-UcNguyenAnhVo  
**Date:** 2025-11-14

---

## COMPONENT 1: BASE SCORE

```mermaid
flowchart LR
    Start([Component 1]) --> Init[score = 0.0]
    Init --> AddBase[score += 5.0]
    AddBase --> End([Continue])
    
    style Start fill:#FFE4B5
    style AddBase fill:#87CEEB
    style End fill:#90EE90
```

**Mô tả:**
- Đơn giản nhất
- Mọi accommodation đều được 5 điểm base

---

## COMPONENT 2: PROXIMITY SCORE

```mermaid
flowchart TD
    Start([Component 2]) --> GetDist[distance = acc.distance]
    GetDist --> CalcExp[proximity = 10 × e^-distance/2]
    CalcExp --> AddScore[score += proximity]
    AddScore --> End([Continue])
    
    style Start fill:#FFE4B5
    style CalcExp fill:#87CEEB
    style AddScore fill:#87CEEB
    style End fill:#90EE90
```

**Công thức:**
```
proximity_score = 10 × e^(-distance/2)

Examples:
- distance = 0.0km → 10.00 điểm
- distance = 0.5km → 7.79 điểm
- distance = 1.0km → 6.07 điểm
- distance = 2.0km → 3.68 điểm
```

---

## COMPONENT 3: TAG MATCH SCORE

```mermaid
flowchart TD
    Start([Component 3]) --> CreateSets[acc_tags = SET acc.tags<br/>required = SET required_tags]
    CreateSets --> Intersect[matching = acc_tags ∩ required]
    Intersect --> InitTag[tag_score = 0.0]
    InitTag --> LoopStart{FOR EACH<br/>tag in matching}
    
    LoopStart -->|Has tag| GetWeight[weight = tag_weights.get tag, 1]
    GetWeight --> AddTag[tag_score += weight]
    AddTag --> LoopStart
    
    LoopStart -->|Done| Cap{tag_score<br/>> 15?}
    Cap -->|Yes| SetCap[tag_score = 15.0]
    Cap -->|No| AddToScore
    SetCap --> AddToScore[score += tag_score]
    AddToScore --> End([Continue])
    
    style Start fill:#FFE4B5
    style Intersect fill:#FFA07A
    style LoopStart fill:#FFD700
    style Cap fill:#FFA07A
    style AddToScore fill:#87CEEB
    style End fill:#90EE90
```

**Weighted Tags:**
```
Critical (3 điểm):  hotel, beach, resort, beachfront
Important (2 điểm): pool, spa, restaurant, bar
Nice-to-have (1):   wifi, parking, gym
```

**Ví dụ:**
```
acc_tags = {'hotel', 'beach', 'pool', 'wifi'}
required_tags = {'hotel', 'beach', 'wifi'}

matching = {'hotel', 'beach', 'wifi'}

tag_score = 3 (hotel) + 3 (beach) + 1 (wifi) = 7 điểm
```

---

## COMPONENT 4: TYPE MATCH BONUS

```mermaid
flowchart TD
    Start([Component 4]) --> GetTypes[acc_type = acc.type<br/>search_type = search_request.type]
    GetTypes --> Compare{acc_type ==<br/>search_type?}
    Compare -->|Yes| AddBonus[score += 5.0]
    Compare -->|No| Skip[No bonus]
    AddBonus --> End([Continue])
    Skip --> End
    
    style Start fill:#FFE4B5
    style Compare fill:#FFA07A
    style AddBonus fill:#87CEEB
    style Skip fill:#D3D3D3
    style End fill:#90EE90
```

**Ví dụ:**
```
Case 1: acc.type = 'hotel', search_type = 'hotel'
        → Match! → +5.0 điểm

Case 2: acc.type = 'resort', search_type = 'hotel'
        → No match → +0.0 điểm
```

---

## COMPONENT 5: NAME QUALITY BONUS

```mermaid
flowchart TD
    Start([Component 5]) --> GetName[name = acc.name]
    GetName --> CheckUnnamed{name ==<br/>'Unnamed'?}
    
    CheckUnnamed -->|Yes| NoBonus[bonus = 0]
    CheckUnnamed -->|No| GetLength[length = LEN name]
    
    GetLength --> Check20{length<br/>> 20?}
    Check20 -->|Yes| Bonus3[bonus = 3.0]
    Check20 -->|No| Check10{length<br/>> 10?}
    
    Check10 -->|Yes| Bonus2[bonus = 2.0]
    Check10 -->|No| Bonus1[bonus = 1.0]
    
    NoBonus --> AddBonus[score += bonus]
    Bonus3 --> AddBonus
    Bonus2 --> AddBonus
    Bonus1 --> AddBonus
    
    AddBonus --> End([Continue])
    
    style Start fill:#FFE4B5
    style CheckUnnamed fill:#FFA07A
    style Check20 fill:#FFA07A
    style Check10 fill:#FFA07A
    style Bonus3 fill:#87CEEB
    style Bonus2 fill:#87CEEB
    style Bonus1 fill:#87CEEB
    style End fill:#90EE90
```

**Scale:**
```
Unnamed               → 0 điểm
Name ≤ 10 chars       → 1 điểm
Name 11-20 chars      → 2 điểm
Name > 20 chars       → 3 điểm
```

**Ví dụ:**
```
'Unnamed'                           → 0
'Hotel A'                           → 1 (7 chars)
'Grand Hotel'                       → 2 (12 chars)
'Imperial Beach Resort & Spa'       → 3 (28 chars)
```

---

## COMPONENT 6: SORTING (Timsort)

```mermaid
flowchart LR
    Start([All Scored]) --> Sort[sorted_accs = SORT<br/>accommodations<br/>KEY: score<br/>ORDER: DESC]
    Sort --> Result[Highest score first]
    Result --> End([Continue])
    
    style Start fill:#FFE4B5
    style Sort fill:#DDA0DD
    style Result fill:#98FB98
    style End fill:#90EE90
```

**Algorithm:** Timsort
- Time: O(n log n)
- Stable: Yes
- Adaptive: Yes (O(n) for sorted data)

---

## COMPONENT 7: TOP-5 SELECTION & RANKING

```mermaid
flowchart TD
    Start([Sorted List]) --> Slice[top_results = sorted_accs[0:5]]
    Slice --> InitLoop[i = 0]
    InitLoop --> LoopCheck{i < 5 AND<br/>i < LEN top_results?}
    
    LoopCheck -->|Yes| Assign[top_results[i].rank = i + 1]
    Assign --> Increment[i += 1]
    Increment --> LoopCheck
    
    LoopCheck -->|No| Return[RETURN top_results]
    Return --> End([END])
    
    style Start fill:#FFE4B5
    style Slice fill:#98FB98
    style LoopCheck fill:#FFD700
    style Assign fill:#87CEEB
    style Return fill:#90EE90
    style End fill:#90EE90
```

**Ví dụ:**
```
sorted_accs = [
    {name: 'A', score: 30},
    {name: 'B', score: 25},
    {name: 'C', score: 20},
    ...
]

top_results = [
    {name: 'A', score: 30, rank: 1},
    {name: 'B', score: 25, rank: 2},
    {name: 'C', score: 20, rank: 3},
    {name: 'D', score: 18, rank: 4},
    {name: 'E', score: 15, rank: 5}
]
```

---

## TỔNG HỢP TẤT CẢ COMPONENTS

```mermaid
flowchart TD
    Start([Input: 1 accommodation]) --> C1[Component 1<br/>Base: +5.0]
    C1 --> C2[Component 2<br/>Proximity: +0-10]
    C2 --> C3[Component 3<br/>Tags: +0-15]
    C3 --> C4[Component 4<br/>Type: +0 or +5]
    C4 --> C5[Component 5<br/>Name: +0 to +3]
    C5 --> Final[Final Score<br/>Min: 5.0<br/>Max: 38.0]
    Final --> End([Output])
    
    style Start fill:#FFE4B5
    style C1 fill:#87CEEB
    style C2 fill:#87CEEB
    style C3 fill:#87CEEB
    style C4 fill:#87CEEB
    style C5 fill:#87CEEB
    style Final fill:#FFD700
    style End fill:#90EE90
```

**Score Range:**
```
Minimum: 5.0  (base only, unnamed, far, no matches)
Maximum: 38.0 (base + 10 proximity + 15 tags + 5 type + 3 name)

Typical: 15-30 điểm
```