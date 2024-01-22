import matplotlib.pyplot as plt
import numpy as np
import control as ctl

def plot_step_response_with_initial_condition(omega, zeta):
    # 伝達関数の係数を定義
    numerator = [omega**2]  # 分子
    denominator = [1, 2*zeta*omega, omega**2]  # 分母

    # 伝達関数オブジェクトの作成
    system = ctl.tf(numerator, denominator)

    # 拡張された時間軸（-0.5秒から開始）
    extended_time = np.linspace(-0.1, 0.5, 100)

    # ステップ応答の計算（0秒から開始）
    response = ctl.step_response(system, extended_time[extended_time >= 0])

    # ステップ応答の前処理（初期値の追加）
    full_response = np.concatenate(([3] * len(extended_time[extended_time < 0]), response.outputs.flatten() * 3 + 3))

    # ステップ入力の作成
    step_input = np.ones_like(extended_time) * 3
    step_input[extended_time >= 0] = 6

    # ステップ応答とステップ入力のプロット
    plt.figure()
    plt.plot(extended_time, full_response, label='System Response')  # システム応答
    plt.plot(extended_time, step_input, 'r--', label='Step Input')  # ステップ入力
    plt.title(f'Step Response with Initial Condition - ω={omega}, ζ={zeta}')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Response / Input Value')
    plt.legend()
    plt.grid()
    plt.show()

# 例として固有角周波数ω=1, 減衰係数ζ=0.5の場合の応答をプロット
plot_step_response_with_initial_condition(omega=29.2, zeta=0.433)
