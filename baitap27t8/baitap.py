from itertools import permutations

def liet_ke_hoan_vi_quay_lui(danh_sach_phan_tu):
    """
    Liệt kê tất cả các hoán vị bằng thuật toán quay lui (tự cài đặt)
    """
    ket_qua = []

    def backtrack(current_permutation, remaining_elements):
        if not remaining_elements:  # Nếu không còn phần tử nào -> lưu hoán vị
            ket_qua.append("".join(map(str, current_permutation)))
            return

        for i in range(len(remaining_elements)):
            chon = remaining_elements[i]
            current_permutation.append(chon)
            new_remaining = remaining_elements[:i] + remaining_elements[i+1:]
            backtrack(current_permutation, new_remaining)
            current_permutation.pop()  # Quay lui

    backtrack([], list(danh_sach_phan_tu))
    return ket_qua


def liet_ke_hoan_vi_itertools(danh_sach_phan_tu):
    """
    Liệt kê tất cả các hoán vị bằng itertools.permutations
    """
    return ["".join(map(str, p)) for p in permutations(danh_sach_phan_tu)]


# ================== CHẠY THỬ ==================
phan_tu_1 = ['A', 'B', 'C']
print("=== Quay lui với ['A','B','C'] ===")
print(liet_ke_hoan_vi_quay_lui(phan_tu_1))

print("\n=== itertools với ['A','B','C'] ===")
print(liet_ke_hoan_vi_itertools(phan_tu_1))

phan_tu_2 = [1, 2]
print("\n=== Quay lui với [1,2] ===")
print(liet_ke_hoan_vi_quay_lui(phan_tu_2))

print("\n=== itertools với [1,2] ===")
print(liet_ke_hoan_vi_itertools(phan_tu_2))
