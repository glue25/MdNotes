## 应用概述

原始文件夹中文件格式为

`word 分隔符 翻译 分隔符 标识符`

Md文件夹中是md格式的单词



为便于表示，设置代号如下：

|      |                    |
| ---- | ------------------ |
| Rc   | 无序原始数据       |
| Rws  | 字母排序原始数据   |
| Rn   | 标识符排序原始数据 |
| MDc  | 无序Markdown       |
| MDws | 字母排序Markdown   |
| MDn  | 标识符排序Markdown |



转换时使用一个独立脚本，通过命令行使用。

预计参数包括

- （输入）输出类型
- 输入输出文件名（可以设置默认参数）
- 输入输出文件夹（当然也可以把路径写进文件名参数，这样设置是为了看着舒服）

此外，有无表头是一个值得考虑的问题.

还有一个功能就是合成，可以设置合成的大文件中依然分段，或者不分段整体处理

平时是不会使用Raw模式的，所以合成后直接输出就好？





## 转换关系

| 原类型 | 直接转换类型 | 间接转换类型 |
| ------ | ------------ | ------------ |
| Rc     | Rws,Rn,MDc   | MDws,MDn     |
| Rws    | Rn,MDws      | MDn          |
| Rn     | MDn,Rws      | MDws         |
| MDc    | Rc,MDws,MDn  | Rws,Rn       |
| MDws   | Rws,MDn      | Rn           |
| MDn    | Rn,MDws      | Rws          |


