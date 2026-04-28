from typing import Dict, List, Tuple

class Solution:
    def build_vocab(text: str) -> Tuple[Dict[str, int], Dict[int, str]]:
        n = len(text)
        
        stoi = {v: k for k,v in enumerate(text)}
        itos = {k: v for k,v in enumerate(text)}
        
        stoi, itos = sorted(stoi.items()), sorted(itos.items())
        
        return (stoi, itos)

    def encode(self, text: str, stoi: Dict[str, int]) -> List[int]:
        return [stoi[char] for char in text]

    def decode(self, ids: List[int], itos: Dict[int, str]) -> str:
        return ''.join(itos[num] for num in ids)
