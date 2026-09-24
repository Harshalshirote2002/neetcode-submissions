class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars_mapping = []

        for pos, sp in zip(position, speed):
            cars_mapping.append((pos, sp))

        cars_mapping = sorted(cars_mapping, key=lambda x: x[0])

        stack = []

        for pos, sp in cars_mapping:
            time = (target - pos)/sp
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)

        return len(stack) 