import pandas as pd
import matplotlib.pyplot as plt

# 设置中文，防止乱码（只使用Windows自带黑体）
plt.rcParams["font.family"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号

# 构造原始生产数据
data = {
    "日期": ["10-01", "10-02", "10-03", "10-04", "10-05"],
    "总产量": [1200, 1350, 1180, 1420, 1300],
    "不良品": [32, 41, 25, 48, 36]
}
df = pd.DataFrame(data)
# 计算良品、良品率
df["良品"] = df["总产量"] - df["不良品"]
df["良品率"] = df["良品"] / df["总产量"]

# 打印数据表格，保留4位小数
print(df.round(4))

# ========== 绘制良品率柱状图 ==========
fig1, ax1 = plt.subplots(figsize=(8, 6), dpi=100)
bars = ax1.bar(df["日期"], df["良品率"], color="#2b7bba", width=0.6)

# 在柱子上方标注良品率百分比
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.003,
             f"{height:.2%}", ha="center", fontsize=10)

ax1.set_title("每日良品率（%）", fontsize=14, pad=12)
ax1.set_xlabel("日期", fontsize=11)
ax1.set_ylabel("良品率", fontsize=11)
ax1.set_ylim(0.9, 1.01)  # Y轴范围聚焦，对比更明显
ax1.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("良品率图表.png", dpi=300, bbox_inches="tight")
plt.close()

# ========== 绘制产量趋势折线图 ==========
fig2, ax2 = plt.subplots(figsize=(8, 6), dpi=100)
ax2.plot(df["日期"], df["总产量"], marker="o", linewidth=2, color="#c82423", markersize=7)

# 折线图数据标注
for x, y in zip(df["日期"], df["总产量"]):
    ax2.text(x, y + 15, str(y), ha="center", fontsize=10)

ax2.set_title("每日总产量趋势图", fontsize=14, pad=12)
ax2.set_xlabel("日期", fontsize=11)
ax2.set_ylabel("总产量", fontsize=11)
ax2.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("产量趋势图.png", dpi=300, bbox_inches="tight")
plt.close()

# ========== 新增：良品&不良品分组柱状对比图 ==========
fig3, ax3 = plt.subplots(figsize=(9, 6), dpi=100)
x = range(len(df["日期"]))
width = 0.35

bar_good = ax3.bar([i - width/2 for i in x], df["良品"], width, label="良品", color="#2b7bba")
bar_bad = ax3.bar([i + width/2 for i in x], df["不良品"], width, label="不良品", color="#ed553b")

# 柱子添加数值标签
for bar in bar_good:
    h = bar.get_height()
    ax3.text(bar.get_x()+bar.get_width()/2, h+10, str(h), ha="center", fontsize=9)
for bar in bar_bad:
    h = bar.get_height()
    ax3.text(bar.get_x()+bar.get_width()/2, h+10, str(h), ha="center", fontsize=9)

ax3.set_title("每日良品与不良品数量对比", fontsize=14, pad=12)
ax3.set_xlabel("日期", fontsize=11)
ax3.set_ylabel("产品数量", fontsize=11)
ax3.set_xticks(x)
ax3.set_xticklabels(df["日期"])
ax3.legend()
ax3.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("良品不良品对比图.png", dpi=300, bbox_inches="tight")
plt.close()

print("✅ 全部图表生成完成！\n已生成：良品率图表.png、产量趋势图.png、良品不良品对比图.png")
