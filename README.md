
atcoder-cliでAtCoderにログイン
```sh
acc login
```

例えば、abc(AtCoder Begiiner Contest)279のディレクトリを作成する場合、作成したいディレクトリにて以下実行
```sh
acc new abc279
```

テストケースで全てACするか試す場合（テストしたいディレクトリにて実行）
```sh
oj t -c " python3 ./main.py" -d ./tests/
```

AtCoderへの提出(python3)
```sh
acc submit main.py
```

AtCoderへの提出(PyPy3)
```sh
acc submit main.py -- --guess-python-interpreter pypy
```

環境構築に際して、参考にした記事  
- https://www.currypurin.com/entry/2022/12/03/160204
- https://qiita.com/malleroid/items/ab83b5ffb8ddfd58a4d3
- https://github.com/malleroid/atcoder_docker_vscode
- http://tatamo.81.la/blog/2018/12/07/atcoder-cli-tutorial/