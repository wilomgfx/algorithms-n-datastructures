class HuffNode:
    key = '-'
    val = -1

    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self):
        return "{0} : {1}".format(self.key, self.val)


class Huffman:
    nodes = []
    freq_table = dict()

    # def __init__(self):
    def gen_freq_table(self, message):
        # freq_table = dict()
        for i in message:
            key = str(i)
            if key in self.freq_table:
                self.freq_table[key] += 1
            else:
                self.freq_table[key] = 1
        return sorted(self.freq_table.items(), key=lambda x: x[1])

    def sorted_freq_table(self):
        return sorted(self.freq_table.items(), key=lambda x: x[1])

    def create_nodes(self):
        for k, v in self.sorted_freq_table():
            huffNode = HuffNode(k,v)
            # print(huffNode)
            self.nodes.append(huffNode)
        return self.nodes

    # def get_smallest_nodes(self):
    #     # huffnode: HuffNode
    #     for huffnode in self.nodes:
    #         if huffnode.val >


    # def build_tree(self):
    #     tree = []


freq = Huffman().gen_freq_table("un message tres secret")
nodes = Huffman().create_nodes()
print(freq)
print(nodes)
