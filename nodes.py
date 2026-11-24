import random
import time


class FlipperZveroboy:
    """
    Randomly swaps width and height with configurable probability.

    Useful for random portrait/landscape orientation:
    if you pass vertical resolution, it may become horizontal.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": (
                    "INT",
                    {
                        "default": 1024,
                        "min": 8,
                        "max": 16384,
                        "step": 8,
                        "display": "number",
                    },
                ),
                "height": (
                    "INT",
                    {
                        "default": 1024,
                        "min": 8,
                        "max": 16384,
                        "step": 8,
                        "display": "number",
                    },
                ),
                "swap_probability": (
                    "FLOAT",
                    {
                        "default": 0.5,
                        "min": 0.0,
                        "max": 1.0,
                        "step": 0.01,
                        "display": "slider",
                    },
                ),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")

    FUNCTION = "process"
    CATEGORY = "Zveroboy/Utils"
    OUTPUT_NODE = False

    def process(self, width, height, swap_probability):
        if random.random() < swap_probability:
            return (height, width)

        return (width, height)

    @classmethod
    def IS_CHANGED(cls, width, height, swap_probability):
        """
        Force ComfyUI to re-evaluate this node every run.

        Without IS_CHANGED, ComfyUI may cache the result when inputs
        are the same, and the random swap would not happen again.
        """
        return time.time_ns()


NODE_CLASS_MAPPINGS = {
    "FlipperZveroboy": FlipperZveroboy,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FlipperZveroboy": "Flipper Zveroboy (Random W/H Swap)",
}