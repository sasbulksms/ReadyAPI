# 💪 - 💗 🔢

🔜 👈 👥 ✔️ 👀 ❔ ⚙️ `Path` &amp; `Query`, ➡️ 👀 🌅 🏧 ⚙️ 📨 💪 📄.

## 🌀 `Path`, `Query` &amp; 💪 🔢

🥇, ↗️, 👆 💪 🌀 `Path`, `Query` &amp; 📨 💪 🔢 📄 ➡ &amp; **ReadyAPI** 🔜 💭 ⚫️❔.

&amp; 👆 💪 📣 💪 🔢 📦, ⚒ 🔢 `None`:

=== "🐍 3️⃣.6️⃣ &amp; 🔛"

    ```Python hl_lines="19-21"
    {!> ../../../docs_src/body_multiple_params/tutorial001.py!}
    ```

=== "🐍 3️⃣.1️⃣0️⃣ &amp; 🔛"

    ```Python hl_lines="17-19"
    {!> ../../../docs_src/body_multiple_params/tutorial001_py310.py!}
    ```

!!! note
    👀 👈, 👉 💼, `item` 👈 🔜 ✊ ⚪️➡️ 💪 📦. ⚫️ ✔️ `None` 🔢 💲.

## 💗 💪 🔢

⏮️ 🖼, *➡ 🛠️* 🔜 ⌛ 🎻 💪 ⏮️ 🔢 `Item`, 💖:

```JSON
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
```

✋️ 👆 💪 📣 💗 💪 🔢, ✅ `item` &amp; `user`:

=== "🐍 3️⃣.6️⃣ &amp; 🔛"

    ```Python hl_lines="22"
    {!> ../../../docs_src/body_multiple_params/tutorial002.py!}
    ```

=== "🐍 3️⃣.1️⃣0️⃣ &amp; 🔛"

    ```Python hl_lines="20"
    {!> ../../../docs_src/body_multiple_params/tutorial002_py310.py!}
    ```

👉 💼, **ReadyAPI** 🔜 👀 👈 📤 🌅 🌘 1️⃣ 💪 🔢 🔢 (2️⃣ 🔢 👈 Pydantic 🏷).

, ⚫️ 🔜 ⤴️ ⚙️ 🔢 📛 🔑 (🏑 📛) 💪, &amp; ⌛ 💪 💖:

```JSON
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
```

!!! note
    👀 👈 ✋️ `item` 📣 🎏 🌌 ⏭, ⚫️ 🔜 ⌛ 🔘 💪 ⏮️ 🔑 `item`.


**ReadyAPI** 🔜 🏧 🛠️ ⚪️➡️ 📨, 👈 🔢 `item` 📨 ⚫️ 🎯 🎚 &amp; 🎏 `user`.

⚫️ 🔜 🎭 🔬 ⚗ 💽, &amp; 🔜 📄 ⚫️ 💖 👈 🗄 🔗 &amp; 🏧 🩺.

## ⭐ 💲 💪

🎏 🌌 📤 `Query` &amp; `Path` 🔬 ➕ 💽 🔢 &amp; ➡ 🔢, **ReadyAPI** 🚚 🌓 `Body`.

🖼, ↔ ⏮️ 🏷, 👆 💪 💭 👈 👆 💚 ✔️ ➕1️⃣ 🔑 `importance` 🎏 💪, 🥈 `item` &amp; `user`.

🚥 👆 📣 ⚫️, ↩️ ⚫️ ⭐ 💲, **ReadyAPI** 🔜 🤔 👈 ⚫️ 🔢 🔢.

✋️ 👆 💪 💡 **ReadyAPI** 😥 ⚫️ ➕1️⃣ 💪 🔑 ⚙️ `Body`:

=== "🐍 3️⃣.6️⃣ &amp; 🔛"

    ```Python hl_lines="22"
    {!> ../../../docs_src/body_multiple_params/tutorial003.py!}
    ```

=== "🐍 3️⃣.1️⃣0️⃣ &amp; 🔛"

    ```Python hl_lines="20"
    {!> ../../../docs_src/body_multiple_params/tutorial003_py310.py!}
    ```

👉 💼, **ReadyAPI** 🔜 ⌛ 💪 💖:

```JSON
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
```

🔄, ⚫️ 🔜 🗜 📊 🆎, ✔, 📄, ♒️.

## 💗 💪 = &amp; 🔢

↗️, 👆 💪 📣 🌖 🔢 🔢 🕐❔ 👆 💪, 🌖 🙆 💪 🔢.

, 🔢, ⭐ 💲 🔬 🔢 🔢, 👆 🚫 ✔️ 🎯 🚮 `Query`, 👆 💪:

```Python
q: Union[str, None] = None
```

⚖️ 🐍 3️⃣.1️⃣0️⃣ &amp; 🔛:

```Python
q: str | None = None
```

🖼:

=== "🐍 3️⃣.6️⃣ &amp; 🔛"

    ```Python hl_lines="27"
    {!> ../../../docs_src/body_multiple_params/tutorial004.py!}
    ```

=== "🐍 3️⃣.1️⃣0️⃣ &amp; 🔛"

    ```Python hl_lines="26"
    {!> ../../../docs_src/body_multiple_params/tutorial004_py310.py!}
    ```

!!! info
    `Body` ✔️ 🌐 🎏 ➕ 🔬 &amp; 🗃 🔢 `Query`,`Path` &amp; 🎏 👆 🔜 👀 ⏪.

## ⏯ 👁 💪 🔢

➡️ 💬 👆 🕴 ✔️ 👁 `item` 💪 🔢 ⚪️➡️ Pydantic 🏷 `Item`.

🔢, **ReadyAPI** 🔜 ⤴️ ⌛ 🚮 💪 🔗.

✋️ 🚥 👆 💚 ⚫️ ⌛ 🎻 ⏮️ 🔑 `item` &amp; 🔘 ⚫️ 🏷 🎚, ⚫️ 🔨 🕐❔ 👆 📣 ➕ 💪 🔢, 👆 💪 ⚙️ 🎁 `Body` 🔢 `embed`:

```Python
item: Item = Body(embed=True)
```

:

=== "🐍 3️⃣.6️⃣ &amp; 🔛"

    ```Python hl_lines="17"
    {!> ../../../docs_src/body_multiple_params/tutorial005.py!}
    ```

=== "🐍 3️⃣.1️⃣0️⃣ &amp; 🔛"

    ```Python hl_lines="15"
    {!> ../../../docs_src/body_multiple_params/tutorial005_py310.py!}
    ```

👉 💼 **ReadyAPI** 🔜 ⌛ 💪 💖:

```JSON hl_lines="2"
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}
```

↩️:

```JSON
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
```

## 🌃

👆 💪 🚮 💗 💪 🔢 👆 *➡ 🛠️ 🔢*, ✋️ 📨 💪 🕴 ✔️ 👁 💪.

✋️ **ReadyAPI** 🔜 🍵 ⚫️, 🤝 👆 ☑ 📊 👆 🔢, &amp; ✔ &amp; 📄 ☑ 🔗 *➡ 🛠️*.

👆 💪 📣 ⭐ 💲 📨 🍕 💪.

&amp; 👆 💪 💡 **ReadyAPI** ⏯ 💪 🔑 🕐❔ 📤 🕴 👁 🔢 📣.
