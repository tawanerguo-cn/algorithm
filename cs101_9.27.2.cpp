#include <iostream>
#include <cmath>
#include <vector>

bool is_prime(int m) {
    if (m == 1) {
        return false;
    }
    for (int i = 2; i <= static_cast<int>(std::sqrt(m)); ++i) {
        if (m % i == 0) {
            return false;
        }
    }
    return true;
}

bool is_square(int m) {
    int sqrt_m = static_cast<int>(std::sqrt(m));
    int sqrt_m_squared = sqrt_m * sqrt_m;
    return sqrt_m_squared == m;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> list_number(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> list_number[i];
    }

    for (int i = 0; i < n; ++i) {
        if (is_prime(static_cast<int>(std::sqrt(list_number[i]))) && is_square(list_number[i])) {
            std::cout << "YES" << std::endl;
        } else {
            std::cout << "NO" << std::endl;
        }
    }
    return 0;
}