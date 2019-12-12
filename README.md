# fileorganize
指定フォルダのファイルを日付フォルダに整理する

## 動作要件
言語:python3 開発環境:python3.8 

## Option引数

-p relative_path 検索するパス： ユーザーディレクトリからのパスになります。 
default:Pictures
ex:Pictures 
ユーザーディレクトリ/Pictures　のパスを探索します。

-o relative_path 出力するパス： 
default:Pictures
ex:Pictures
ユーザーディレクトリ/Pictures/年/月/日のフォルダ整理をします

タスクスケジューラーとかで自動整理するとかがいいと思います。
macではautomatorのapplescriptで 

```
on run
	tell application "Terminal"
		do script "python 置いてるパス/fileAutoOrganize.py"
		run
	end tell
end run
```

みたいな感じで作成し、カレンダーに登録するみたいな運用
