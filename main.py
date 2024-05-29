from typing import List

class Solution:
    def collision(self, asteroids: List[int]) -> List[int]:
        # Criando array
        array = []
        for asteroid in asteroids:
            # Enquanto lista for True e a ultima posição forem maior que 0 e asteroide for menor que 0.
            while array and array[-1] > 0 and asteroid < 0:
                if array[-1] == -asteroid:
                    array.pop()
                    break
                elif array[-1] < -asteroid:
                    array.pop()
                    continue
                else: break
            else: array.append(asteroid)
        return array
    

asteroid = Solution()

# Output Expected -> [5, 10], [], [10], [-2, -2, -2, -2], [-2, -2, -2, 1]
print(f'{asteroid.collision([5, 10, -5])}, {asteroid.collision([8, -8])}, {asteroid.collision([10, 2, -5])}, {asteroid.collision([-2, -2, -2, -2])}, {asteroid.collision([-2, -2, -2, 1])}')

