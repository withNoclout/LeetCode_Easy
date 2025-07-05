class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        """
        :type initialEnergy: int
        :type initialExperience: int
        :type energy: List[int]
        :type experience: List[int]
        :rtype: int
        """
        hours = 0
        
        # Calculate minimum energy needed
        total_energy_needed = sum(energy)
        if initialEnergy <= total_energy_needed:
            hours += total_energy_needed - initialEnergy + 1
        
        # Calculate minimum experience needed
        current_exp = initialExperience
        for exp in experience:
            if current_exp <= exp:
                # Need to train to have strictly more experience
                hours += exp - current_exp + 1
                current_exp = exp + 1
            current_exp += exp
        
        return hours
