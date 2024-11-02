import os

class LinearCongruentialGenerator:
    def __init__(self, seed, a=1664525, c=1013904223, m=2**32):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m
        self.state = seed
    
    def random(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def gen_float(self):
        return self.random() / self.m
    
class MiddleSquareGenerator:
    def __init__(self, seed, num_digits=10):
        self.seed = seed
        self.num_digits = num_digits
        
    def random(self):
        value = self.seed
        num_digits = self.num_digits
        value_str = str(value).zfill(num_digits * 2)
        next_value = int(value_str[(num_digits // 2):(num_digits // 2 + num_digits)])
        value = next_value
        self.seed = value
        return value
    
    def gen_float(self):
        return self.random() / (2**self.num_digits - 1)
    
class XORShiftGenerator:
    def __init__(self, seed):
        self.state = seed

    def random(self):
        x = self.state
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17) & 0xFFFFFFFF
        x ^= (x << 5) & 0xFFFFFFFF
        self.state = x
        return x

    def gen_float(self):
        return self.next() / 2**32
    
class Xorshift128Generator:
    def __init__(self, seed):
        self.state = [seed, seed]

    def random(self):
        s0 = self.state[0]
        s1 = self.state[1]
        result = (s0 + s1) & 0xFFFFFFFFFFFFFFFF
        s1 ^= s0
        self.state[0] = (s0 << 55 | s0 >> 9) & 0xFFFFFFFFFFFFFFFF
        self.state[1] = (s1 << 36 | s1 >> 28) & 0xF
        return result

    def gen_float(self):
        return self.random() / 2**64
    
class Xorshift1024Generator:
    def __init__(self, seed):
        self.state = [seed] * 16

    def random(self):
        s0 = self.state[0]
        s1 = self.state[1]
        s2 = self.state[2]
        s3 = self.state[3]
        s4 = self.state[4]
        s5 = self.state[5]
        s6 = self.state[6]
        s7 = self.state[7]
        s8 = self.state[8]
        s9 = self.state[9]
        s10 = self.state[10]
        s11 = self.state[11]
        s12 = self.state[12]
        s13 = self.state[13]
        s14 = self.state[14]
        s15 = self.state[15]
        result = (s0 + s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11 + s12 + s13 + s14 + s15) & 0xFFF
        s15 ^= s14
        s14 ^= s13
        s13 ^= s12            
        s12 ^= s11
        s11 ^= s10
        s10 ^= s9
        s9 ^= s8
        s8 ^= s7
        s7 ^= s6
        s6 ^= s5
        s5 ^= s4
        s4 ^= s3
        s3 ^= s2
        s2 ^= s1
        s1 ^= s0
        s0 = (s0 << 11 | s0 >> 53) & 0xF
        self.state[0] = s0
        self.state[1] = s1
        self.state[2] = s2
        self.state[3] = s3
        self.state[4] = s4
        self.state[5] = s5
        self.state[6] = s6
        self.state[7] = s7
        self.state[8] = s8
        self.state[9] = s9
        self.state[10] = s10
        self.state[11] = s11
        self.state[12] = s12
        self.state[13] = s13
        self.state[14] = s14
        self.state[15] = s15
        return result

    def gen_float(self):
        return self.random() / 2**12
    
class Xorshift256Generator:
    def __init__(self, seed):
        self.state = [seed] * 4

    def random(self):
        s0 = self.state[0]
        s1 = self.state[1]
        s2 = self.state[2]
        s3 = self.state[3]
        result = (s0 + s3) & 0xFFFFFFFFFFFFFFFF
        t = (s1 << 17) & 0xFFFFFFFFFFFFFFFF
        s2 ^= s0
        s3 ^= s1
        s1 ^= s2
        s0 ^= s3
        s2 ^= t
        s3 = (s3 << 45 | s3 >> 19) & 0xF
        self.state[0] = s0
        self.state[1] = s1
        self.state[2] = s2
        self.state[3] = s3
        return result

    def gen_float(self):
        return self.random() / 2**64
    
class Xorshift512Generator:
    def __init__(self, seed):
        self.state = [seed] * 8

    def random(self):
        s0 = self.state[0]
        s1 = self.state[1]
        s2 = self.state[2]
        s3 = self.state[3]
        s4 = self.state[4]
        s5 = self.state[5]
        s6 = self.state[6]
        s7 = self.state[7]
        result = (s0 + s1 + s2 + s3 + s4 + s5 + s6 + s7) & 0xFFFFFFFFFFFFFFFF
        t = (s1 << 17) & 0xFFFFFFFFFFFFFFFF
        s6 ^= s0
        s7 ^= s1
        s4 ^= s2
        s5 ^= s3
        s0 ^= s4
        s1 ^= s5
        s2 ^= s6
        s3 ^= s7
        s6 ^= t
        s7 = (s7 << 36 | s7 >> 28) & 0xFFFFFFFFFFFFFFFF
        self.state[0] = s0
        self.state[1] = s1
        self.state[2] = s2
        self.state[3] = s3
        self.state[4] = s4
        self.state[5] = s5
        self.state[6] = s6
        self.state[7] = s7
        return result

    def gen_float(self):
        return self.random() / 2**128
    
class MerseneTwisterGenerator:
    def __init__(self, seed):
        self.state = [seed] * 624
        self.index = 0

    def random(self):
        if self.index == 0:
            self.twist()
        y = self.state[self.index]
        y ^= (y >> 11) & 0xFFFFFFFFFFFFFFFF
        y ^= (y << 7) & 0xFFFFFFFFFFFFFFFF
        y ^= (y << 15) & 0xFFFFFFFFFFFFFFFF
        y ^= (y >> 18) & 0xFFFFFFFFFFFFFFFF
        self.index = (self.index + 1) % 624
        return y

    def twist(self):
        for i in range(624):
            y = (self.state[i] & 0x80) + (self.state[(i + 1) % 624] & 0x7FFFFFFFFFFFFFFF)
            self.state[i] = self.state[(i + 397) % 624] ^ (y >> 1)
            if y % 2 != 0:
                self.state[i] ^= 0x9908B0DF1647A9AB

    def gen_float(self):
        return self.random() / 2**64
    
class PCGGenerator:
    def __init__(self, seed):
        self.state = [seed, seed]

    def random(self):
        s0 = self.state[0]
        s1 = self.state[1]
        result = (s0 * 6364136223846793005 + s1) & 0xFFFFFFFFFFFFFFFF
        s1 = (s1 << 18 | s1 >> 46) & 0xFFFFFFFFFFFFFFFF
        self.state[0] = s0
        self.state[1] = s1
        return result

    def gen_float(self):
        return self.random() / 2**64
    
class LCGGenerator:
    def __init__(self, seed):
        self.state = seed

    def random(self):
        self.state = (self.state * 1103515245 + 12345) & 0xFFFFFFFF
        return self.state

    def gen_float(self):
        return self.random() / 2**32
    
class LCG64Generator:
    def __init__(self, seed):
        self.state = seed

    def random(self):
        self.state = (self.state * 6364136223846793005 + 1442695040888963407) & 0xFFFFFFFFFFFFFFFF
        return self.state

    def gen_float(self):
        return self.random() / 2**64
    
class LCG128Generator:
    def __init__(self, seed):
        self.state = [seed, seed]

    def random(self):
        s0 = self.state[0]
        s1 = self.state[1]
        result = (s0 * 6364136223846793005 + s1) & 0xFFFFFFFFFFFFFFFF
        s1 = (s1 << 18 | s1 >> 46) & 0xFFFFFFFFFFFFFFFF
        self.state[0] = s0
        self.state[1] = s1
        return result

    def gen_float(self):
        return self.random() / 2**128
    
class LCG256Generator:
    def __init__(self, seed):
        self.state = [seed] * 4

    def random(self):
        s0 = self.state[0]
        s1 = self.state[1]
        s2 = self.state[2]
        s3 = self.state[3]
        result = (s0 * 6364136223846793005 + s1 + s2 + s3) & 0xFFFFFFFFFFFFFFFF
        t = (s1 << 18 | s1 >> 46) & 0xFFFFFFFFFFFFFFFF
        s2 ^= s0
        s3 ^= s1
        s0 ^= s2
        s1 ^= s3
        s2 ^= t
        s3 = (s3 << 39 | s3 >> 25) & 0xF
        self.state[0] = s0
        self.state[1] = s1
        self.state[2] = s2
        self.state[3] = s3
        return result

    def gen_float(self):
        return self.random() / 2**128
    
class LCG512Generator:
    def __init__(self, seed):
        self.state = [seed] * 8

    def random(self):
        s0 = self.state[0]
        s1 = self.state[1]
        s2 = self.state[2]
        s3 = self.state[3]
        s4 = self.state[4]
        s5 = self.state[5]
        s6 = self.state[6]
        s7 = self.state[7]
        result = (s0 * 6364136223846793005 + s1 + s2 + s3 + s4 + s5 + s6 + s7) & 0xFFFFFFFFFFFFFFFF
        t = (s1 << 18 | s1 >> 46) & 0xFFFFFFFFFFFFFFFF
        s6 ^= s0
        s7 ^= s1
        s4 ^= s2
        s5 ^= s3
        s0 ^= s4
        s1 ^= s5
        s2 ^= s6
        s3 ^= s7
        s6 ^= t
        s7 = (s7 << 36 | s7 >> 28) & 0xF
        self.state[0] = s0
        self.state[1] = s1
        self.state[2] = s2
        self.state[3] = s3
        self.state[4] = s4
        self.state[5] = s5
        self.state[6] = s6
        self.state[7] = s7
        return result

    def gen_float(self):
        return self.random() / 2**256
    
class LCG1024Generator:
    def __init__(self, seed):
        self.state = [seed] * 16

    def random(self):
        s0 = self.state[0]
        s1 = self.state[1]
        s2 = self.state[2]
        s3 = self.state[3]
        s4 = self.state[4]
        s5 = self.state[5]
        s6 = self.state[6]
        s7 = self.state[7]
        s8 = self.state[8]
        s9 = self.state[9]
        s10 = self.state[10]
        s11 = self.state[11]
        s12 = self.state[12]
        s13 = self.state[13]
        s14 = self.state[14]
        s15 = self.state[15]        
        result = (s0 * 6364136223846793005 + s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11 + s12 + s13 + s14 + s15) & 0xFFFFFFFFFFFFFFFF
        t = (s1 << 18 | s1 >> 46) & 0xFFFFFFFFFFFFFFFF
        s15 ^= s14
        s14 ^= s13
        s13 ^= s12
        s12 ^= s11
        s11 ^= s10
        s10 ^= s9
        s9 ^= s8
        s8 ^= s7
        s7 ^= s6
        s6 ^= s5
        s5 ^= s4
        s4 ^= s3
        s3 ^= s2
        s2 ^= s1
        s1 ^= s0
        s0 = (s0 << 11 | s0 >> 53) & 0xF
        self.state[0] = s0
        self.state[1] = s1
        self.state[2] = s2
        self.state[3] = s3
        self.state[4] = s4
        self.state[5] = s5
        self.state[6] = s6
        self.state[7] = s7
        self.state[8] = s8
        self.state[9] = s9
        self.state[10] = s10
        self.state[11] = s11
        self.state[12] = s12
        self.state[13] = s13
        self.state[14] = s14
        self.state[15] = s15
        return result

    def gen_float(self):
        return self.random() / 2**512
    
class TrueRandomGenerator:
    def __init__(self):
        pass

    def random(self):
        return int.from_bytes(os.urandom(4), byteorder='big')
    
    def gen_float(self):
        return self.random() / 2**32
    
class RandomGenerator:
    def __init__(self, seed, method='LCG'):
        self.method = method
        self.generator = None
        if method == 'LCG':
            self.generator = LCGGenerator(seed)
        elif method == 'LCG64':
            self.generator = LCG64Generator(seed)
        elif method == 'LCG128':
            self.generator = LCG128Generator(seed)
        elif method == 'LCG256':
            self.generator = LCG256Generator(seed)
        elif method == 'LCG512':
            self.generator = LCG512Generator(seed)
        elif method == 'LCG1024':
            self.generator = LCG1024Generator(seed)
        elif method == 'Xorshift256':
            self.generator = Xorshift256Generator(seed)
        elif method == 'Xorshift512':
            self.generator = Xorshift512Generator(seed)            
        elif method == 'MersenneTwister':
            self.generator = MerseneTwisterGenerator(seed)
        elif method == 'PCG':
            self.generator = PCGGenerator(seed)
        elif method == 'TrueRandom':
            self.generator = TrueRandomGenerator()
        elif method == 'XORShift':
            self.generator = XORShiftGenerator(seed)
        elif method == 'Xorshift1024':
            self.generator = Xorshift1024Generator(seed)
        elif method == 'Xorshift128':
            self.generator = Xorshift128Generator(seed)
        else:
            raise ValueError('Invalid random method')

    def random(self):
        return self.generator.random()

    def gen_float(self):
        return self.generator.gen_float()
    
    def random_ranged(self, a, b):
        return a + (b - a) * self.random()
    
    def gen_float_ranged(self, a, b):
        return a + (b - a) * self.gen_float()