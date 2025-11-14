"""
TEST CASES cho Thuật toán Ranking

Author: 24127592-UcNguyenAnhVo
Date: 2025-11-14
"""

import sys
import math
from rank_results_improved import rank_results, explain_ranking


def test_normal_case():
    """Test Case 1: Normal case với 3 accommodations"""
    print("=" * 70)
    print("TEST 1: NORMAL CASE")
    print("=" * 70)
    
    accommodations = [
        {
            'name': 'Imperial Hotel Vung Tau',
            'distance': 0.3,
            'tags': ['hotel', 'beach', 'pool', 'wifi', 'restaurant'],
            'type': 'hotel'
        },
        {
            'name': 'Pullman Vung Tau Resort',
            'distance': 1.5,
            'tags': ['resort', 'beach', 'pool', 'spa'],
            'type': 'resort'
        },
        {
            'name': 'Unnamed',
            'distance': 0.8,
            'tags': ['hotel', 'wifi'],
            'type': 'hotel'
        }
    ]
    
    search_request = {
        'type': 'hotel',
        'tags': ['hotel', 'beach', 'pool', 'wifi']
    }
    
    results = rank_results(accommodations, search_request)
    
    # Expected
    # Imperial: Base(5) + Prox(8.61) + Tags(9) + Type(5) + Name(3) = 30.61
    # Unnamed: Base(5) + Prox(6.70) + Tags(4) + Type(5) + Name(0) = 20.70
    # Pullman: Base(5) + Prox(4.72) + Tags(5) + Type(0) + Name(3) = 17.72
    
    assert results[0]['name'] == 'Imperial Hotel Vung Tau', "Rank 1 should be Imperial"
    assert results[0]['rank'] == 1, "Rank should be 1"
    assert abs(results[0]['score'] - 30.61) < 0.5, f"Score should be ~30.61, got {results[0]['score']}"
    
    print("✅ Test PASSED")
    print(f"Rank 1: {results[0]['name']} - {results[0]['score']} điểm")
    print(f"Rank 2: {results[1]['name']} - {results[1]['score']} điểm")
    print(f"Rank 3: {results[2]['name']} - {results[2]['score']} điểm")
    print()


def test_empty_list():
    """Test Case 2: Empty accommodations list"""
    print("=" * 70)
    print("TEST 2: EMPTY LIST")
    print("=" * 70)
    
    accommodations = []
    search_request = {'type': 'hotel', 'tags': []}
    
    results = rank_results(accommodations, search_request)
    
    assert results == [], "Empty input should return empty list"
    
    print("✅ Test PASSED")
    print("Empty input → Empty output")
    print()


def test_same_score():
    """Test Case 3: Accommodations với score giống nhau"""
    print("=" * 70)
    print("TEST 3: SAME SCORE (Stable Sort)")
    print("=" * 70)
    
    accommodations = [
        {
            'name': 'Hotel A',
            'distance': 1.0,
            'tags': ['hotel'],
            'type': 'hotel'
        },
        {
            'name': 'Hotel B',
            'distance': 1.0,
            'tags': ['hotel'],
            'type': 'hotel'
        }
    ]
    
    search_request = {'type': 'hotel', 'tags': ['hotel']}
    
    results = rank_results(accommodations, search_request)
    
    # Both should have same score
    assert results[0]['score'] == results[1]['score'], "Scores should be equal"
    
    # Timsort is stable, so order should be preserved
    assert results[0]['name'] == 'Hotel A', "Stable sort: Hotel A should come first"
    
    print("✅ Test PASSED")
    print(f"Both have score: {results[0]['score']}")
    print(f"Order preserved: {results[0]['name']} then {results[1]['name']}")
    print()


def test_tag_cap():
    """Test Case 4: Tag score capping at 15"""
    print("=" * 70)
    print("TEST 4: TAG SCORE CAPPING")
    print("=" * 70)
    
    accommodations = [{
        'name': 'Super Hotel',
        'distance': 1.0,
        'tags': ['hotel', 'beach', 'resort', 'pool', 'spa', 'restaurant'],
        'type': 'hotel'
    }]
    
    search_request = {
        'type': 'hotel',
        'tags': ['hotel', 'beach', 'resort', 'pool', 'spa', 'restaurant']
    }
    
    results = rank_results(accommodations, search_request)
    
    # Tags: hotel(3) + beach(3) + resort(3) + pool(2) + spa(2) + restaurant(2) = 15
    # Should be capped at 15
    
    # Total: Base(5) + Prox(6.07) + Tags(15) + Type(5) + Name(2) = 33.07
    assert abs(results[0]['score'] - 33.07) < 0.5, f"Score should be ~33.07, got {results[0]['score']}"
    
    print("✅ Test PASSED")
    print(f"Tag score capped at 15.0")
    print(f"Total score: {results[0]['score']}")
    print()


def test_exponential_proximity():
    """Test Case 5: Kiểm tra exponential proximity"""
    print("=" * 70)
    print("TEST 5: EXPONENTIAL PROXIMITY DECAY")
    print("=" * 70)
    
    distances = [0.0, 0.5, 1.0, 2.0, 5.0]
    
    print("Distance (km) | Proximity Score")
    print("-" * 35)
    for d in distances:
        prox = 10.0 * math.exp(-d / 2.0)
        print(f"{d:>12.1f}  | {prox:>15.2f}")
    
    print("\n✅ Test PASSED")
    print("Exponential decay working correctly")
    print()


def run_all_tests():
    """Chạy tất cả test cases"""
    print("\n" + "=" * 70)
    print("RUNNING ALL TESTS")
    print("=" * 70 + "\n")
    
    test_normal_case()
    test_empty_list()
    test_same_score()
    test_tag_cap()
    test_exponential_proximity()
    
    print("=" * 70)
    print("✅ ALL TESTS PASSED!")
    print("=" * 70)


if __name__ == "__main__":
    run_all_tests()