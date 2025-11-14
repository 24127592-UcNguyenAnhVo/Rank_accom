# 📚 Ranking Algorithm Documentation

**Đồ án:** Tư duy Tính toán  
**Sinh viên:** 24127592-UcNguyenAnhVo  
**Ngày:** 2025-11-14  
**Chủ đề:** Thuật toán xếp hạng nơi ở (Accommodation Ranking Algorithm)

---

## 📂 Cấu trúc thư mục

```
Ranking_Algorithm_Documentation/
├── README.md                          # File này
├── 01_Code_Implementation/            # Yêu cầu 1: Code implementation
│   ├── rank_results_improved.py       # Code cải tiến đầy đủ
│   ├── test_ranking.py                # Test cases
│   └── requirements.txt               # Dependencies
├── 02_Pseudo_Code/                    # Yêu cầu 2: Pseudo code
│   ├── pseudo_code.md                 # Pseudo code chi tiết
│   └── complexity_analysis.md         # Phân tích độ phức tạp
├── 03_Flowchart/                      # Yêu cầu 3: Flowchart
│   ├── flowchart_main.md              # Flowchart tổng thể (Mermaid)
│   ├── flowchart_components.md        # Flowchart từng component
│   └── flowchart_comparison.md        # So sánh code vs flowchart
└── 04_References/                     # Yêu cầu 4: Dẫn chứng
    ├── academic_references.md         # Tài liệu học thuật
    ├── evidence_based.md              # Bằng chứng từng component
    └── industry_examples.md           # Ví dụ thực tế
```

---

## 🎯 4 YÊU CẦU CỦA NHÓM TRƯỞNG

### ✅ 1. Code Implementation
**Mô tả:** Implement thuật toán ranking đúng chức năng, có type hints, comments đầy đủ

**Files:**
- `01_Code_Implementation/rank_results_improved.py`
- `01_Code_Implementation/test_ranking.py`

**Improvements:**
- Base score: 10 → 5
- Proximity: Linear → Exponential decay
- Tags: Equal weights → Weighted (1-3)
- Type bonus: 3 → 5
- Name bonus: Fixed 1 → Dynamic 1-3

---

### ✅ 2. Pseudo Code
**Mô tả:** Pseudo code rõ ràng với cấu trúc BEGIN...END, có phân tích complexity

**Files:**
- `02_Pseudo_Code/pseudo_code.md`
- `02_Pseudo_Code/complexity_analysis.md`

**Highlights:**
- 7 phases rõ ràng
- Ký hiệu toán học chuẩn (∩, Σ, →)
- Time: O(n log n)
- Space: O(n)

---

### ✅ 3. Flowchart
**Mô tả:** Flowchart chi tiết, khớp 100% với code

**Files:**
- `03_Flowchart/flowchart_main.md`
- `03_Flowchart/flowchart_components.md`
- `03_Flowchart/flowchart_comparison.md`

**Features:**
- Mermaid syntax
- Color coding
- Decision nodes, Process boxes, Loop indicators

---

### ✅ 4. Dẫn chứng & Nguồn gốc
**Mô tả:** Tài liệu tham khảo academic papers, industry examples

**Files:**
- `04_References/academic_references.md`
- `04_References/evidence_based.md`
- `04_References/industry_examples.md`

**Key References:**
- Weighted Sum Model: Triantaphyllou (2000)
- Proximity Decay: Küpper (2005)
- Tag Matching: Manning et al. (2008)
- Timsort: Python Documentation

---

## 🚀 Cách sử dụng

### 1. Xem Code
```bash
cd 01_Code_Implementation
python rank_results_improved.py
```

### 2. Chạy Tests
```bash
cd 01_Code_Implementation
python test_ranking.py
```

### 3. Xem Flowchart
Mở file `03_Flowchart/flowchart_main.md` trên GitHub để render Mermaid diagram

---

## 📊 Kết quả

**Cải tiến so với code cũ:**
- ✅ Score separation tăng 57%
- ✅ Proximity phân biệt rõ hơn 
- ✅ Tag weighting realistic hơn
- ✅ Documentation đầy đủ

**Test coverage:**
- ✅ Normal cases
- ✅ Edge cases (empty, unnamed, same score)
- ✅ Ablation study

---

## 👨‍💻 Tác giả

**24127592-UcNguyenAnhVo**  
Đồ án Tư duy Tính toán - Năm 2  
Ngày: 2025-11-14

---

## 📝 License

Educational Project - For learning purposes only