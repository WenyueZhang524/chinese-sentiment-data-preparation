import pandas as pd
import json
from sklearn.model_selection import train_test_split

qinggan = {"sadness":"伤心","happiness":"开心","anger":"生气","fear":"害怕","disgust":"厌恶"}
# 读取Excel文件
df = pd.read_excel('data.xlsx')

# 初始化列表来存储转换后的数据
data = []

# 遍历DataFrame，构造所需的数据格式
for _, row in df.iterrows():
    input1 = str(row['content'])
    out = str(row['label'])
    entry = {
        "instruction": "您是一位情感分析师，请根据我提供的<句子>,输出对应的情感类别:伤心,开心,害怕,生气,厌恶",
        "input": "<句子>" + input1,
        "output": qinggan[out]
    }
    data.append(entry)

# 按照9:1的比例分割数据为训练集和验证集
train_data, val_data = train_test_split(data, test_size=0.1, random_state=42)

# 保存数据到JSON文件
with open('train.json', 'w', encoding='utf-8') as f:
    json.dump(train_data, f, ensure_ascii=False,indent=4)

with open('val.json', 'w', encoding='utf-8') as f:
    json.dump(val_data, f, ensure_ascii=False,indent=4)

print("数据已分割并保存为train.json和val.json。")
