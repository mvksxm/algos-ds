# Time Complexity: O(log n) + O(1) = O(log n)
# Space Complexity: O(m*n); where m is the amount of keys and n is the amount of timestamps per key.

class TimeMap:

    def __init__(self):
        self._backend_map = {}

    def _search_value(self, key, timestamp) -> str:

        stamped_values = self._backend_map.get(key, None)

        if stamped_values is None:
            return ""


        l_pointer = 0
        r_pointer = len(stamped_values) - 1
        m_pointer = 0


        while l_pointer <= r_pointer:

            m_pointer = l_pointer + ((r_pointer - l_pointer) // 2)
            m_record = stamped_values[m_pointer]
            record_timestamp = m_record[0]

            if record_timestamp == timestamp:
                return m_record[1]

            if record_timestamp > timestamp:
                r_pointer = m_pointer - 1
            else:
                l_pointer = m_pointer + 1

        res_pointer = -1
        if m_pointer > r_pointer:
            res_pointer = r_pointer

        if l_pointer > m_pointer:
            res_pointer = m_pointer

        return stamped_values[res_pointer][1] if res_pointer != -1 else ""


    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self._backend_map:
            self._backend_map[key].append((timestamp, value))
            return

        self._backend_map[key] = [(timestamp, value)]


    def get(self, key: str, timestamp: int) -> str:
        return self._search_value(key,  timestamp)


if  __name__ == "__main__":
    tm = TimeMap()