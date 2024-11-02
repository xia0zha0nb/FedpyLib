from .. import randombuilder as rd

random_generator = rd.RandomGenerator(seed=12345, method='LCG')

for i in range(10):
    print(random_generator.random())

for i in range(10):
    print(random_generator.gen_float())

for i in range(10):
    print(random_generator.random_ranged(0, 100))

for i in range(10):
    print(random_generator.gen_float_ranged(0, 100))