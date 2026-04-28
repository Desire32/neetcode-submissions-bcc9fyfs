from typing import Dict, List, Tuple

class Solution:
    def build_vocab(self, text: str) -> Tuple[Dict[str, int], Dict[int, str]]:
        
        stoi = {char: index for index, char in enumerate(text)}
        itos = {index: char for index, char in enumerate(text)}

        stoi = dict(sorted(stoi.items()))
        itos = dict(sorted(itos.items()))

        return (stoi, itos)

    def encode(self, text: str, stoi: Dict[str, int]) -> List[int]:
        return [stoi[char] for char in text]

    def decode(self, ids: List[int], itos: Dict[int, str]) -> str:
        return ''.join(itos[num] for num in ids)
