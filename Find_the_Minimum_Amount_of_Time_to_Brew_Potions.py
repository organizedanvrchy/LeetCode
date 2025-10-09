class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        """
        Simulates wizards brewing potions on an assembly line with no waiting allowed between wizards.
        Each wizard i takes skill[i] * mana[j] time on potion j.
        Potions must go through all wizards sequentially, with exact timing synchronization.
        """

        num_wizards = len(skill)
        num_potions = len(mana)

        # Prefix sum of skill levels: total skill up to each wizard
        # Example: skill = [1,5,2,4] → wizard_prefix = [0,1,6,8,12]
        wizard_prefix = [0] * (num_wizards + 1)
        for i in range(1, num_wizards + 1):
            wizard_prefix[i] = wizard_prefix[i - 1] + skill[i - 1]

        # Time when the current potion starts brewing on Wizard 0
        potion_start_time = 0

        # Go through each potion (except the first, which starts at time 0)
        for potion_index in range(1, num_potions):
            previous_mana = mana[potion_index - 1]
            current_mana = mana[potion_index]

            # Find the minimum delay needed so no wizard overlaps between the two potions
            delay_needed = float('-inf')

            # For each wizard, check when the previous potion finishes
            # and when the next potion would arrive there.
            for i in range(1, num_wizards + 1):
                # previous_potion_finish = previous_mana * total_skill_up_to_wizard_i
                # current_potion_arrival = current_mana * total_skill_up_to_previous_wizard
                required_delay = (previous_mana * wizard_prefix[i]) - (current_mana * wizard_prefix[i - 1])
                delay_needed = max(delay_needed, required_delay)

            # Move the start time forward by that much
            potion_start_time += max(0, delay_needed)

        # Once all potions have started, total time = last start + time for last potion to finish
        total_brewing_time = potion_start_time + mana[-1] * wizard_prefix[num_wizards]
        return total_brewing_time
