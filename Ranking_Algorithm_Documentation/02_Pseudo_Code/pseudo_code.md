# PSEUDO CODE - Thuật toán Ranking

**Author:** 24127592-UcNguyenAnhVo  
**Date:** 2025-11-14

---

## PSEUDO CODE CHI TIẾT

```
ALGORITHM RankAccommodations(accommodations, search_request)
│
├─ INPUT:
│   ├─ accommodations[] : Array of accommodation objects
│   │   └─ Each object contains: {name, distance, tags[], type}
│   └─ search_request{} : Dictionary
│       └─ Contains: {type, tags[], lat, lon, radius}
│
└─ OUTPUT:
    └─ ranked_list[] : Top 5 accommodations sorted by score

BEGIN
    ┌─────────────────────────────────────────────────────────────────┐
    │ PHASE 1: INPUT VALIDATION                                       │
    └─────────────────────────────────────────────────────────────────┘
    
    IF accommodations is EMPTY THEN
        RETURN []
    END IF
    
    ┌─────────────────────────────────────────────────────────────────┐
    │ PHASE 2: EXTRACT & PREPARE DATA                                 │
    └─────────────────────────────────────────────────────────────────┘
    
    required_tags ← search_request.tags
    search_type ← search_request.type
    
    // Define tag weights (Evidence-based)
    tag_weights ← {
        'hotel': 3, 'resort': 3, 'beach': 3,      // Critical
        'pool': 2, 'spa': 2, 'restaurant': 2,     // Important
        'wifi': 1, 'parking': 1, 'gym': 1         // Nice-to-have
    }
    
    ┌─────────────────────────────────────────────────────────────────┐
    │ PHASE 3: SCORING LOOP                                           │
    └─────────────────────────────────────────────────────────────────┘
    
    FOR EACH acc IN accommodations DO
        score ← 0.0
        
        ┌─────────────────────────────────────────────────────────┐
        │ Component 1: Base Score                                 │
        └─────────────────────────────────────────────────────────┘
        score ← score + 5.0
        
        ┌─────────────────────────────────────────────────────────┐
        │ Component 2: Proximity Score (Exponential Decay)        │
        │ Formula: 10 × e^(-d/2)                                  │
        └─────────────────────────────────────────────────────────┘
        distance ← acc.distance  // in km
        proximity_score ← 10.0 × exp(-distance / 2.0)
        score ← score + proximity_score
        
        ┌─────────────────────────────────────────────────────────┐
        │ Component 3: Weighted Tag Match Score                   │
        │ Formula: Σ weight[tag] for tag ∈ intersection           │
        └─────────────────────────────────────────────────────────┘
        acc_tags ← SET(acc.tags)
        required_tags_set ← SET(required_tags)
        
        // Set intersection operation
        matching_tags ← acc_tags ∩ required_tags_set
        
        tag_score ← 0.0
        FOR EACH tag IN matching_tags DO
            weight ← tag_weights[tag] IF tag EXISTS IN tag_weights
                                     ELSE 1.0  // default weight
            tag_score ← tag_score + weight
        END FOR
        
        // Cap at 15 to prevent outliers
        tag_score ← MIN(tag_score, 15.0)
        score ← score + tag_score
        
        ┌─────────────────────────────────────────────────────────┐
        │ Component 4: Type Match Bonus                           │
        └─────────────────────────────────────────────────────────┘
        IF acc.type == search_type THEN
            score ← score + 5.0
        END IF
        
        ┌─────────────────────────────────────────────────────────┐
        │ Component 5: Name Quality Bonus                         │
        │ Scale: 0 (unnamed), 1 (≤10), 2 (≤20), 3 (>20 chars)    │
        └─────────────────────────────────────────────────────────┘
        IF acc.name ≠ "Unnamed" THEN
            name_length ← LENGTH(acc.name)
            
            IF name_length > 20 THEN
                score ← score + 3.0
            ELSE IF name_length > 10 THEN
                score ← score + 2.0
            ELSE
                score ← score + 1.0
            END IF
        END IF
        
        // Assign final score (rounded to 2 decimals)
        acc.score ← ROUND(score, 2)
    END FOR
    
    ┌─────────────────────────────────────────────────────────────────┐
    │ PHASE 4: SORTING                                                │
    │ Algorithm: Timsort (Python's built-in)                         │
    │ Complexity: O(n log n)                                          │
    └─────────────────────────────────────────────────────────────────┘
    
    sorted_accs ← SORT(accommodations, 
                       KEY = acc.score, 
                       ORDER = DESCENDING)
    
    ┌─────────────────────────────────────────────────────────────────┐
    │ PHASE 5: TOP-K SELECTION (K = 5)                                │
    └─────────────────────────────────────────────────────────────────┘
    
    top_results ← sorted_accs[0:5]  // First 5 elements
    
    ┌─────────────────────────────────────────────────────────────────┐
    │ PHASE 6: RANK ASSIGNMENT                                        │
    └─────────────────────────────────────────────────────────────────┘
    
    FOR i ← 0 TO LENGTH(top_results) - 1 DO
        top_results[i].rank ← i + 1
    END FOR
    
    ┌─────────────────────────────────────────────────────────────────┐
    │ PHASE 7: RETURN RESULT                                          │
    └─────────────────────────────────────────────────────────────────┘
    
    RETURN top_results

END ALGORITHM
```

---

## VÍ DỤ MINH HỌA

### Input:
```
accommodations = [
    {name: 'Hotel A', distance: 0.3, tags: ['hotel', 'beach'], type: 'hotel'},
    {name: 'Resort B', distance: 1.5, tags: ['resort', 'pool'], type: 'resort'}
]

search_request = {type: 'hotel', tags: ['hotel', 'beach', 'pool']}
```

### Execution:

**Accommodation 1: Hotel A**
```
score = 0
score = score + 5.0                        = 5.0    (Base)
score = score + 10 × e^(-0.3/2)            = 13.61  (Proximity: 8.61)
tags matching: {hotel, beach}
score = score + 3 + 3                      = 19.61  (Tags: 6.0)
type match: hotel == hotel
score = score + 5.0                        = 24.61  (Type: 5.0)
name length = 7
score = score + 1.0                        = 25.61  (Name: 1.0)

Final: Hotel A score = 25.61
```

**Accommodation 2: Resort B**
```
score = 0
score = score + 5.0                        = 5.0    (Base)
score = score + 10 × e^(-1.5/2)            = 9.72   (Proximity: 4.72)
tags matching: {pool}
score = score + 2                          = 11.72  (Tags: 2.0)
type match: resort ≠ hotel
score = score + 0                          = 11.72  (Type: 0.0)
name length = 8
score = score + 1.0                        = 12.72  (Name: 1.0)

Final: Resort B score = 12.72
```

### Output:
```
[
    {name: 'Hotel A', score: 25.61, rank: 1},
    {name: 'Resort B', score: 12.72, rank: 2}
]
```