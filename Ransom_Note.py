class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)

        can_create_note = all(m_count[char] >= r_count[char] for char in r_count)                   

        return can_create_note

# Alternatively
  # if len(magazine) < len(ransomNote):
  #     return False
  
  # for l in set(ransomNote):
  #     if magazine.count(l) < ransomNote.count(l):
  #         return False
      
  # return True
