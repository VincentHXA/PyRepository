# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
# 高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100
# 万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

# 程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。

from collections import OrderedDict

standard = OrderedDict(sorted({0: 0.1, 100000: 0.075, 200000: 0.05, 400000: 0.03, 600000: 0.015, 1000000: 0.01}.items(),
							  key=lambda t: t[0], reverse=True))
	
def get_reward(benefit):
	reward = 0
	remain = benefit
	for split_money, ratio in standard.items():
		if(benefit > split_money):
			reward += (remain - split_money) * ratio
			remain = remain - split_money

	return reward

if __name__ == '__main__':
	print(get_reward(200000))
