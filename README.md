# ComfyUI-FlipperZveroboy

![image](image.jpg)

<<<<<<< HEAD
## Русская секция

=======
>>>>>>> origin/master
Кастомная нода для ComfyUI, которая случайно меняет местами значения `width` и `height`.

### Что делает нода

Нода принимает два целых числа:

- `width`
- `height`

При каждом запуске графа с заданной вероятностью значения могут быть поменяны местами.

По умолчанию вероятность равна `0.5`, то есть шанс 50/50.

Например:

- вход: `width = 768`, `height = 1024`
- вариант 1: выход останется `768 x 1024`
- вариант 2: выход станет `1024 x 768`

Таким образом, вертикальное разрешение с шансом 50% может стать горизонтальным.

### Параметры

| Параметр | Тип | Описание |
|---|---|---|
| `width` | INT | Входная ширина |
| `height` | INT | Входная высота |
| `swap_probability` | FLOAT | Вероятность обмена местами, от 0.0 до 1.0 |

При `swap_probability = 0.5` шанс обмена равен 50%.

### Установка

Установите репозиторий в папку `custom_nodes` вашего ComfyUI:

    cd ComfyUI/custom_nodes
    git clone https://github.com/thezveroboy/ComfyUI-FlipperZveroboy.git

Или просто скопируйте папку проекта в:

    ComfyUI/custom_nodes/ComfyUI-FlipperZveroboy

После этого перезапустите ComfyUI.

### Использование

Добавьте ноду через поиск:

    Flipper Zveroboy

Или найдите её в категории:

    Zveroboy/Utils

Выходы ноды `width` и `height` можно подключить, например, к:

- `Empty Latent Image`
- `Empty Image`
- любой другой ноде, которая принимает размеры изображения

### Почему добавлен `IS_CHANGED`

ComfyUI кэширует результаты нод, если входные данные не изменились.

Чтобы случайная перестановка `width` и `height` происходила при каждом запуске, в ноде реализован метод `IS_CHANGED`, который принудительно инвалидирует кэш ноды.
<<<<<<< HEAD

## English section

Custom ComfyUI node that randomly swaps `width` and `height` values.

### What the node does

The node takes two integers:

- `width`
- `height`

On each graph run, with a given probability, the values may be swapped.

By default, the probability is `0.5`, i.e. a 50/50 chance.

Example:

- input: `width = 768`, `height = 1024`
- variant 1: output stays `768 x 1024`
- variant 2: output becomes `1024 x 768`

Thus, a vertical resolution with a 50% chance may become horizontal.

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `width` | INT | Input width |
| `height` | INT | Input height |
| `swap_probability` | FLOAT | Probability of swapping, from 0.0 to 1.0 |

At `swap_probability = 0.5`, the swap chance is 50%.

### Installation

Install the repository in your ComfyUI `custom_nodes` folder:

    cd ComfyUI/custom_nodes
    git clone https://github.com/thezveroboy/ComfyUI-FlipperZveroboy.git

Or simply copy the project folder to:

    ComfyUI/custom_nodes/ComfyUI-FlipperZveroboy

Then restart ComfyUI.

### Usage

Add the node via search:

    Flipper Zveroboy

Or find it in the category:

    Zveroboy/Utils

The node outputs `width` and `height` can be connected, for example, to:

- `Empty Latent Image`
- `Empty Image`
- any other node that accepts image dimensions

### Why `IS_CHANGED` is added

ComfyUI caches node results if the input data has not changed.

To make the random swap of `width` and `height` happen on every run, the node implements the `IS_CHANGED` method, which forces the node cache to be invalidated.
=======
>>>>>>> origin/master
