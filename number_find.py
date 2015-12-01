""" Find the duplicate number game """
import random
import datetime

class NumberFind(object):
    """ game object """
    def __init__(self):
        self.grid_sizes = range(3, 8)

    def _get_grid_size(self):
        return raw_input('Choose a grid size: {0} '.format(self.grid_sizes))

    def _setup_grid(self):
        user_input = self._get_grid_size()
        invalid_grid = True
        while invalid_grid:
            try:
                if int(user_input) in self.grid_sizes:
                    self.grid_size = int(user_input)
                    invalid_grid = False
                else:
                    print 'Invalid: grid size not allowed'
                    user_input = self._get_grid_size()
            except ValueError:
                print 'Invalid: grid size must be a number'
                user_input = self._get_grid_size()
        self.numbers = random.sample(range(1000), self.grid_size**2)
        answer_locations = random.sample(range(self.grid_size**2), 2)
        self.answer = self.numbers[answer_locations[0]]
        self.numbers[answer_locations[1]] = self.answer

    def play(self):
        """ play game """
        self._setup_grid()

        counter = 0
        line = []
        for num in self.numbers:
            line.append(num)
            counter += 1
            if counter == self.grid_size:
                print ' '.join('{:4}'.format(x) for x in line)
                counter = 0
                line = []
        start_time = datetime.datetime.now()
        user_answer = raw_input('What is the answer? ')
        end_time = datetime.datetime.now()
        diff_time = end_time - start_time
        try:
            if int(user_answer) == self.answer:
                print '\nYOU WIN!'
                print "Time: {} seconds\n".format(diff_time.total_seconds())
            else:
                print 'You lost...'
        except:
            print 'You lost...'

if __name__ == '__main__':
    game = NumberFind()
    game.play()
