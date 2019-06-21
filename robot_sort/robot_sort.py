class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        #attributes 
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        # SortingRobot concept:
        # Starts from the beginning with it's lights on while sorting items (..insert compare and swap..), when it's done it will switch the lights off.
        # Missing things
        #   (i)
        #   [4,   5,    2,  1]
        self.set_light_on() #First, set the lights on
        while self.light_is_on() is True: #initiate the while loop
            self.set_light_off() #SET FINAL ACTION
            #print(self.light_is_on())
            
            while self.can_move_right(): #starts at the beginning move to the right 
                self.swap_item() #swaps item and move to the right
                self.move_right()
                    
                if self.compare_item() == 1: #Moves item to the correct place
                    self.swap_item()
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                    self.set_light_on()
                    
                if self.compare_item() == -1: #Item has less value so item doesn't need to be sorted
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                
                if self.compare_item() == 0: #if both items have the same value so item doesn't need to be sorted
                    self.move_left()
                    self.swap_item()
                    self.move_right()
            # after the robot reaches the end of the array the main while loop will continue from here 
                    
            if self.light_is_on() and self.can_move_right() is False: #break
                while self.can_move_left() == True:
                    self.move_left() #will be activated
        print('Robot works')
                
          # turn your sortingrobot list to the sorted list        
                    
 # Main command for Sorting Robot
        #self._item = None       # The item the robot is holding
        #self._position = 0      # The list position the robot is at
        #self._light = "OFF"     # The state of the robot's light
        #self._time = 0          # A time counter (stretch)
    
    # Library of Robots movement/command
        #self.can_move_left   :   move left if at the start of the list
        #self.can_move_right  :   move right if at the end of the list
        
        #self.move_left       :   returns true if robot move left. Otherwise, it stays in place and returns False (increments 1)
        #self.move_right      :   returns true if robot move right. Otherwise, it stays in place and returns False (increments 1)
        
        #self.swap_item       :   swaps current held item with the list in front
        #self.compare_item    :   compares current held item with the list item item in front of the robot
        
        #self.set_light_on    :   turn on robot's light. Otherwise, false. | Stretch: triggers lights when looking for items from left or right when finding item on the list
        #self.set_light_off   :   non-movement

if __name__ == "__main__":

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)