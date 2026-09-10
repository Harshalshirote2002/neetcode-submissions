class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # Target character frequencies
        t_char_counts = {}
        for char in t:
            t_char_counts[char] = t_char_counts.get(char, 0) + 1

        s_char_counts = {}
        required_unique = len(t_char_counts)
        matched_unique = 0

        start = 0
        min_len = float("inf")
        best_range = (0, 0)

        # Expand the window using 'end'
        for end in range(len(s)):
            char_in = s[end]
            s_char_counts[char_in] = s_char_counts.get(char_in, 0) + 1

            # Check if this character now meets the required frequency in t
            if (
                char_in in t_char_counts
                and s_char_counts[char_in] == t_char_counts[char_in]
            ):
                matched_unique += 1

            # When all required characters are satisfied, shrink from 'start'
            while matched_unique == required_unique:
                current_len = end - start + 1
                if current_len < min_len:
                    min_len = current_len
                    best_range = (start, end + 1)

                char_out = s[start]
                s_char_counts[char_out] -= 1
                if (
                    char_out in t_char_counts
                    and s_char_counts[char_out] < t_char_counts[char_out]
                ):
                    matched_unique -= 1

                start += 1

        return s[best_range[0] : best_range[1]] if min_len != float("inf") else ""