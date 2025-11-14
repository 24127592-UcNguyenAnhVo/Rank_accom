# TÀI LIỆU THAM KHẢO HỌC THUẬT

**Author:** 24127592-UcNguyenAnhVo  
**Date:** 2025-11-14

---

## 1. THUẬT TOÁN CƠ SỞ: WEIGHTED SUM MODEL

### Tài liệu chính:

**Triantaphyllou, E. (2000).** *Multi-Criteria Decision Making Methods: A Comparative Study.*  
Kluwer Academic Publishers, Boston.

**Relevant Chapters:**
- Chapter 2: The Weighted Sum Model (WSM)
- Chapter 3: Comparison of MCDM Methods

**ISBN:** 978-0-7923-6607-2

**Key Formula:**
```
A* = argmax Σ(wi × fi(a))
      a∈A   i=1

Where:
- A* = optimal solution
- wi = weight of criterion i
- fi(a) = value of criterion i for alternative a
```

**Ứng dụng vào bài toán:**
```python
Score(acc) = w1×Base + w2×Proximity + w3×Tags + w4×Type + w5×Name

With weights:
- w1 = 1 (Base = 5.0)
- w2 = 1 (Proximity max = 10.0)
- w3 = weighted (Tags max = 15.0)
- w4 = 1 (Type = 5.0)
- w5 = dynamic (Name = 0-3)
```

**Citation:**
```bibtex
@book{triantaphyllou2000multi,
  title={Multi-criteria decision making methods: a comparative study},
  author={Triantaphyllou, Evangelos},
  year={2000},
  publisher={Springer Science \& Business Media}
}
```

---

## 2. PROXIMITY SCORE: EXPONENTIAL DECAY

### Tài liệu chính:

**Küpper, A. (2005).** *Location-Based Services: Fundamentals and Operation.*  
John Wiley & Sons, Chichester, UK.

**Relevant Chapters:**
- Chapter 5: Proximity-based Search Algorithms
- Section 5.3: Distance Decay Functions

**ISBN:** 978-0-470-09231-6

**Key Concepts:**
- Distance decay function: `f(d) = K × e^(-λd)`
- λ (lambda) = decay rate parameter
- Trong code: λ = 0.5 (decay rate = 1/2)

**Công thức trong code:**
```python
proximity_score = 10.0 * math.exp(-distance / 2.0)
#                  ↑              ↑
#                  K              λ = 0.5
```

**Citation:**
```bibtex
@book{kupper2005location,
  title={Location-based services: fundamentals and operation},
  author={K{\"u}pper, Axel},
  year={2005},
  publisher={John Wiley \& Sons}
}
```

---

## 3. TOBLER'S FIRST LAW OF GEOGRAPHY

**Tobler, W.R. (1970).** "A Computer Movie Simulating Urban Growth in the Detroit Region."  
*Economic Geography*, 46 (supplement), 234–240.

**Famous Quote:**
> "Everything is related to everything else, but near things are more related than distant things."

**Ứng dụng:**
- Justification cho việc ưu tiên nơi ở GẦN hơn
- Proximity score decay theo khoảng cách

**DOI:** 10.2307/143141

**Citation:**
```bibtex
@article{tobler1970computer,
  title={A computer movie simulating urban growth in the Detroit region},
  author={Tobler, Waldo R},
  journal={Economic geography},
  volume={46},
  number={sup1},
  pages={234--240},
  year={1970},
  publisher={Taylor \& Francis}
}
```

---

## 4. TAG MATCHING: INFORMATION RETRIEVAL

### Tài liệu chính:

**Manning, C.D., Raghavan, P., & Schütze, H. (2008).**  
*Introduction to Information Retrieval.*  
Cambridge University Press.

**Relevant Chapters:**
- Chapter 6: Scoring, Term Weighting, and the Vector Space Model
- Section 6.2: Term Frequency and Weighting
- Section 6.3: TF-IDF Weighting

**ISBN:** 978-0-521-86571-5

**Online:** https://nlp.stanford.edu/IR-book/

**Key Concepts:**
- Term weighting based on importance
- Set intersection for matching
- Relevance scoring

**Áp dụng:**
```python
# Weighted tag matching (similar to TF-IDF)
tag_weights = {
    'hotel': 3,   # High importance
    'wifi': 1     # Low importance
}

# Set intersection
matching_tags = acc_tags & required_tags
```

**Citation:**
```bibtex
@book{manning2008introduction,
  title={Introduction to information retrieval},
  author={Manning, Christopher D and Raghavan, Prabhakar and Sch{\"u}tze, Hinrich},
  year={2008},
  publisher={Cambridge university press}
}
```

---

## 5. JACCARD SIMILARITY INDEX

**Jaccard, P. (1901).** "Étude comparative de la distribution florale dans une portion des Alpes et des Jura."  
*Bulletin de la Société Vaudoise des Sciences Naturelles*, 37, 547–579.

**Formula:**
```
J(A, B) = |A ∩ B| / |A ∪ B|
```

**Simplified version in code:**
```python
# We use intersection without union normalization
matching_count = len(acc_tags & required_tags)
```

**Citation:**
```bibtex
@article{jaccard1901etude,
  title={{\'E}tude comparative de la distribution florale dans une portion des Alpes et des Jura},
  author={Jaccard, Paul},
  journal={Bulletin de la Soci{\'e}t{\'e} Vaudoise des Sciences Naturelles},
  volume={37},
  pages={547--579},
  year={1901}
}
```

---

## 6. SORTING ALGORITHM: TIMSORT

### Tài liệu chính:

**Peters, T. (2002).** *Timsort Description.*  
Python-Dev mailing list.

**Official Python Documentation:**  
https://docs.python.org/3/howto/sorting.html

**Source Code:**  
https://github.com/python/cpython/blob/main/Objects/listsort.txt

**Key Features:**
- Hybrid: Merge Sort + Insertion Sort
- Stable sort (preserves order of equal elements)
- Adaptive: O(n) best case for sorted data
- O(n log n) worst case

**Citation:**
```bibtex
@misc{peters2002timsort,
  title={Timsort},
  author={Peters, Tim},
  year={2002},
  howpublished={Python-Dev mailing list},
  url={https://github.com/python/cpython/blob/main/Objects/listsort.txt}
}
```

---

## 7. PYTHON SET OPERATIONS

**Official Python Documentation:**  
https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

**Relevant Operations:**
```python
# Set intersection
A & B           # Operator syntax
A.intersection(B)  # Method syntax

# Complexity: O(min(len(A), len(B)))
```

**Citation:**
```bibtex
@manual{python3reference,
  title={The Python Language Reference},
  author={{Python Software Foundation}},
  year={2024},
  url={https://docs.python.org/3/reference/}
}
```

---

## 8. COMPLEXITY ANALYSIS

**Cormen, T.H., Leiserson, C.E., Rivest, R.L., & Stein, C. (2009).**  
*Introduction to Algorithms (3rd Edition).*  
MIT Press.

**Relevant Chapters:**
- Chapter 2: Getting Started (Sorting basics)
- Chapter 3: Growth of Functions (Big-O notation)
- Chapter 6: Heapsort

**ISBN:** 978-0-262-03384-8

**Citation:**
```bibtex
@book{cormen2009introduction,
  title={Introduction to algorithms},
  author={Cormen, Thomas H and Leiserson, Charles E and Rivest, Ronald L and Stein, Clifford},
  year={2009},
  publisher={MIT press}
}
```

---

## 9. MATHEMATICAL FUNCTIONS

**Exponential Function:**

**Euler, L. (1748).** *Introductio in analysin infinitorum.*  
Lausanne: Marcum-Michaelem Bousquet.

**Modern reference:**
```
e^x = exp(x) = Σ(x^n / n!) for n=0 to ∞

In Python: math.exp(x)
```

---

## 10. ALGORITHM DESIGN

**Kleinberg, J., & Tardos, É. (2006).**  
*Algorithm Design.*  
Pearson Education.

**Relevant Chapters:**
- Chapter 4: Greedy Algorithms
- Chapter 13: Randomized Algorithms

**ISBN:** 978-0-321-29535-4

**Citation:**
```bibtex
@book{kleinberg2006algorithm,
  title={Algorithm design},
  author={Kleinberg, Jon and Tardos, Eva},
  year={2006},
  publisher={Pearson Education India}
}
```

---

## SUMMARY TABLE

| Component | Academic Source | Year |
|-----------|----------------|------|
| Weighted Sum Model | Triantaphyllou (2000) | 2000 |
| Proximity Decay | Küpper (2005) | 2005 |
| Geography Law | Tobler (1970) | 1970 |
| Tag Weighting | Manning et al. (2008) | 2008 |
| Set Operations | Jaccard (1901) | 1901 |
| Sorting | Peters (2002) | 2002 |
| Complexity | Cormen et al. (2009) | 2009 |

---

## FULL BIBLIOGRAPHY

```bibtex
@book{triantaphyllou2000multi,
  title={Multi-criteria decision making methods: a comparative study},
  author={Triantaphyllou, Evangelos},
  year={2000},
  publisher={Springer Science \& Business Media}
}

@book{kupper2005location,
  title={Location-based services: fundamentals and operation},
  author={K{\"u}pper, Axel},
  year={2005},
  publisher={John Wiley \& Sons}
}

@article{tobler1970computer,
  title={A computer movie simulating urban growth in the Detroit region},
  author={Tobler, Waldo R},
  journal={Economic geography},
  volume={46},
  number={sup1},
  pages={234--240},
  year={1970}
}

@book{manning2008introduction,
  title={Introduction to information retrieval},
  author={Manning, Christopher D and Raghavan, Prabhakar and Sch{\"u}tze, Hinrich},
  year={2008},
  publisher={Cambridge university press}
}

@book{cormen2009introduction,
  title={Introduction to algorithms},
  author={Cormen, Thomas H and Leiserson, Charles E and Rivest, Ronald L and Stein, Clifford},
  year={2009},
  publisher={MIT press}
}
```