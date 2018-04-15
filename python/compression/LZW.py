import sys

class LZW:

    @staticmethod
    def compress(uncompressed, initial_dict=None):
        codes = []
        if initial_dict is not None:
            d = initial_dict.copy()
        else:
            d = dict()
        seq = uncompressed[0]
        for i in range(1, len(uncompressed)):
            c = uncompressed[i]
            if seq + c in d:
                seq = seq + c
            else:
                code = d.get(seq)
                # print(code)
                codes.append(code)
                d[seq + c] = len(d)
                seq = c
        code = d.get(seq)
        codes.append(code)
        # pre_compression_size = len(uncompressed.encode("utf-8"))
        # compression_size = sys.getsizeof(codes)
        return (codes, d)

    @staticmethod
    def decompress(compressed, initial_dict=None):
        decompressed = []
        if initial_dict is not None:
            d = initial_dict.copy()
        else:
            d = dict()
        s = None
        for i in compressed:
            c = i
            seq = d.get(c)
            if seq is None:
                seq = s + s[0]
            decompressed.append(seq)
            if s is not None:
                d.update({len(d): s + seq[0]})
            s = seq
        # compression_size = bytes(compressed)
        # len(bytes(decompressed)
        return ("".join(decompressed), d)


compress_out = LZW.compress("ababcbababaaaaaaa", {'a': 0, 'b': 1, 'c': 2})
print(compress_out[0])
print(compress_out[1])
# should be 0 1 3 2 4 7 0 9 10 0
assert compress_out[0] == [0, 1, 3, 2, 4, 7, 0, 9, 10, 0]
out = LZW.decompress(compress_out[0], {0: 'a', 1: 'b', 2: 'c'})
print(out)
assert "".join(out[0]) == "ababcbababaaaaaaa"
