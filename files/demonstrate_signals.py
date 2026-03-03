import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons, Button


def main() -> None:
	x = np.linspace(0, 10, 1200)

	defaults = {
		"constant": 1.0,
		"noise_std": 0.0,
		"gain_const": 1.0,
		"gain_slope": 0.2,
		"gain_mode": "Constant gain",
	}

	rng = np.random.default_rng(7)

	fig, ax = plt.subplots(figsize=(11, 6))
	plt.subplots_adjust(left=0.1, right=0.78, bottom=0.33)

	baseline = np.full_like(x, defaults["constant"])
	signal_line, = ax.plot(x, baseline, lw=2, label="Signal")
	baseline_line, = ax.plot(x, baseline, "--", lw=1.2, alpha=0.7, label="Constant baseline")

	ax.set_title("Interactive Constant Signal with Noise and Gain")
	ax.set_xlabel("x")
	ax.set_ylabel("y")
	ax.grid(alpha=0.35)
	ax.legend(loc="upper left")

	ax_constant = plt.axes([0.1, 0.24, 0.58, 0.03])
	ax_noise = plt.axes([0.1, 0.19, 0.58, 0.03])
	ax_gain_const = plt.axes([0.1, 0.14, 0.58, 0.03])
	ax_gain_slope = plt.axes([0.1, 0.09, 0.58, 0.03])
	ax_mode = plt.axes([0.81, 0.55, 0.17, 0.18])
	ax_clear = plt.axes([0.81, 0.42, 0.17, 0.07])

	slider_constant = Slider(ax_constant, "Constant", -5.0, 5.0, valinit=defaults["constant"])
	slider_noise = Slider(ax_noise, "Noise std", 0.0, 2.0, valinit=defaults["noise_std"])
	slider_gain_const = Slider(ax_gain_const, "Gain", 0.0, 3.0, valinit=defaults["gain_const"])
	slider_gain_slope = Slider(ax_gain_slope, "Gain slope", -1.0, 1.0, valinit=defaults["gain_slope"])

	mode_selector = RadioButtons(ax_mode, ("Constant gain", "Gain = 1 + slope·x"), active=0)
	clear_button = Button(ax_clear, "Clear / Reset")

	def recompute() -> None:
		constant_value = slider_constant.val
		noise_std = slider_noise.val
		gain_const = slider_gain_const.val
		gain_slope = slider_gain_slope.val
		gain_mode = mode_selector.value_selected

		base = np.full_like(x, constant_value)

		if gain_mode == "Constant gain":
			gain = np.full_like(x, gain_const)
			ax.set_title("Mode: Constant gain")
		else:
			x_norm = x
			gain = 1.0 + gain_slope * x_norm
			ax.set_title("Mode: Gain as function of x (1 + slope·x)")

		noisy_signal = base * gain + rng.normal(0.0, noise_std, size=x.size)

		signal_line.set_ydata(noisy_signal)
		baseline_line.set_ydata(base)

		y_min = min(np.min(noisy_signal), np.min(base))
		y_max = max(np.max(noisy_signal), np.max(base))
		pad = max(0.5, 0.1 * (y_max - y_min if y_max != y_min else 1.0))
		ax.set_ylim(y_min - pad, y_max + pad)

		fig.canvas.draw_idle()

	def on_slider_change(_value: float) -> None:
		recompute()

	def on_mode_change(_label: str) -> None:
		recompute()

	def on_clear(_event) -> None:
		slider_constant.reset()
		slider_noise.reset()
		slider_gain_const.reset()
		slider_gain_slope.reset()

		desired_mode = defaults["gain_mode"]
		current_mode = mode_selector.value_selected
		if current_mode != desired_mode:
			target_index = list(mode_selector.labels).index(
				next(label for label in mode_selector.labels if label.get_text() == desired_mode)
			)
			mode_selector.set_active(target_index)
		else:
			recompute()

	slider_constant.on_changed(on_slider_change)
	slider_noise.on_changed(on_slider_change)
	slider_gain_const.on_changed(on_slider_change)
	slider_gain_slope.on_changed(on_slider_change)
	mode_selector.on_clicked(on_mode_change)
	clear_button.on_clicked(on_clear)

	recompute()
	plt.show()


if __name__ == "__main__":
	main()
