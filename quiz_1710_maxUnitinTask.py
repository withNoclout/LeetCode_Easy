class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxType.sort( key=lambda x: x[1], reverse=True)
        total_units = 0 
        boxes_used = 0 

        for num_boxes, units_per_box in boxTypes:
            boxes_to_take = min( num_boxes , truckSize - boxes_used ) 
            total_unit += boxes_to_take * units_per_box 
            boxes_used  += boxes_to_take
            if boxes_used >= truckSize : 
                break 

        return total_units
