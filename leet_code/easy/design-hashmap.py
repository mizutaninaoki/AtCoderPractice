class MyHashMap:

    def __init__(self):
        self.dictionary = {}

    def put(self, key: int, value: int) -> None:
        self.dictionary[key] = value

    def get(self, key: int) -> int:
        if key in self.dictionary:
            return self.dictionary[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        self.dictionary.pop(key, None)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# MyHashMap() は、空のマップでオブジェクトを初期化します。
# void put(int key, int value) HashMapに(key, value)のペアを挿入します。キーがすでにマップに存在する場合は、対応する値を更新します。
# int get(int key) 指定されたキーがマッピングされている値を返し、このマップにキーのマッピングがない場合は -1 を返します。
# void remove(key) マップにキーのマッピングが含まれている場合、キーとそれに対応する値を削除します。
