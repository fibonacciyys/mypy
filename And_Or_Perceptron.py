from functools import reduce

class Perceptron(object):
    #input_num stand for the number of weights, 
    #activator stand for the activate function
    def __init__(self, input_num, activator):
        self.activator = activator
        self.weights = [0.0 for i in range(input_num)]
        self.bias = 0.0
        
    def __str__(self):
        return "weight\t: %s\nbias\t: %f" % (self.weights, self.bias)
    
    def predict(self, input_vec):
        wx = list(map(lambda x, w : x * w, input_vec, self.weights))
        res = reduce(lambda x, y : x + y, wx)
        res += self.bias
        return self.activator(res)
    
    #input, correct result of input, train time for each sample, learning rate
    def train(self, input_vecs, labels, train_time, rate):
        numb = len(labels)
        for j in range(train_time) :
            for i in range(numb):
                self._train_one_vec(input_vecs[i], labels[i], rate)
    
    def _train_one_vec(self, input_vec, label, rate):
        p_res = self.predict(input_vec) #get predict of input
        d = rate * (label - p_res)      #for calculate the delta vector
        delta = list(map(lambda x: d * x, input_vec))   #delta of each weight
        self.weights = list(map(lambda w, dw: w + dw, self.weights, delta))
        self.bias += d

#activate function
def af(num):
    return 1 if num > 0 else 0

def test_and_perceptron():
    train_set_input = [[1, 1], [0, 0], [0, 1], [1, 0]]
    train_set_res = [1, 0, 0, 0]
    test_set_input = [[0, 0], [0, 1], [0, 1], [0, 0], [1, 1], [1, 0]]
    
    and_p = Perceptron(len(train_set_input[0]), af)
    
    #train
    and_p.train(train_set_input, train_set_res, 10, 0.1)
    print(and_p)
    
    #check
    for x in test_set_input:
        res = and_p.predict(x)
        print("test %s -> %d" % (x, res))
    return and_p

def test_or_perceptron():
    train_set_input = [[1, 1], [0, 0], [0, 1], [1, 0]]
    train_set_res = [1, 0, 1, 1]
    test_set_input = [[0, 0], [0, 1], [0, 1], [0, 0], [1, 1], [1, 0]]
    
    or_p = Perceptron(len(train_set_input[0]), af)
    
    #train
    or_p.train(train_set_input, train_set_res, 10, 0.1)
    print(or_p)
    
    #check
    for x in test_set_input:
        res = or_p.predict(x)
        print("test %s -> %d" % (x, res))
        
    return or_p

def main():
    print('and')
    test_and_perceptron()
    print('or')
    test_or_perceptron()

if __name__ == "__main__":
    main()