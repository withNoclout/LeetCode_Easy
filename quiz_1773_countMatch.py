class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        key_to_count = {
            'type' : 0 , 
            'color' : 1, 
            'name' : 2 
        }

        idx = key_to_count[ruleKey]

        return sum(1 for item in items if item[idx] == ruleValue)
