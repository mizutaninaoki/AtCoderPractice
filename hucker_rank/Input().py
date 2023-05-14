x, k = map(int, input().split())
# execで文字列をpythonで実行
exec('result =' + input())
print('True') if result == k else print('False')
