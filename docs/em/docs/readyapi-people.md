# ReadyAPI 👫👫

ReadyAPI ✔️ 🎆 👪 👈 🙋 👫👫 ⚪️➡️ 🌐 🖥.

## 👼 - 🐛

🙋 ❗ 👶

👉 👤:

{% if people %}
<div class="user-list user-list-center">
{% for user in people.maintainers %}

<div class="user"><a href="{{ user.url }}" target="_blank"><div class="avatar-wrapper"><img src="{{ user.avatarUrl }}"/></div><div class="title">@{{ user.login }}</div></a> <div class="count">❔: {{ user.answers }}</div><div class="count">🚲 📨: {{ user.prs }}</div></div>
{% endfor %}

</div>
{% endif %}

👤 👼 &amp; 🐛 **ReadyAPI**. 👆 💪 ✍ 🌅 🔃 👈 [ℹ ReadyAPI - 🤚 ℹ - 🔗 ⏮️ 📕](help-readyapi.md#connect-with-the-author){.internal-link target=_blank}.

...✋️ 📥 👤 💚 🎦 👆 👪.

---

**ReadyAPI** 📨 📚 🐕‍🦺 ⚪️➡️ 👪. &amp; 👤 💚 🎦 👫 💰.

👫 👫👫 👈:

* [ℹ 🎏 ⏮️ ❔ 📂](help-readyapi.md#help-others-with-questions-in-github){.internal-link target=_blank}.
* [✍ 🚲 📨](help-readyapi.md#create-a-pull-request){.internal-link target=_blank}.
* 📄 🚲 📨, [✴️ ⚠ ✍](contributing.md#translations){.internal-link target=_blank}.

👏 👫. 👶 👶

## 🌅 🦁 👩‍💻 🏁 🗓️

👫 👩‍💻 👈 ✔️ [🤝 🎏 🏆 ⏮️ ❔ 📂](help-readyapi.md#help-others-with-questions-in-github){.internal-link target=_blank} ⏮️ 🏁 🗓️. 👶

{% if people %}
<div class="user-list user-list-center">
{% for user in people.last_month_active %}

<div class="user"><a href="{{ user.url }}" target="_blank"><div class="avatar-wrapper"><img src="{{ user.avatarUrl }}"/></div><div class="title">@{{ user.login }}</div></a> <div class="count">❔ 📨: {{ user.count }}</div></div>
{% endfor %}

</div>
{% endif %}

## 🕴

📥 **ReadyAPI 🕴**. 👶

👫 👩‍💻 👈 ✔️ [ℹ 🎏 🏆 ⏮️ ❔ 📂](help-readyapi.md#help-others-with-questions-in-github){.internal-link target=_blank} 🔘 *🌐 🕰*.

👫 ✔️ 🎦 🕴 🤝 📚 🎏. 👶

{% if people %}
<div class="user-list user-list-center">
{% for user in people.experts %}

<div class="user"><a href="{{ user.url }}" target="_blank"><div class="avatar-wrapper"><img src="{{ user.avatarUrl }}"/></div><div class="title">@{{ user.login }}</div></a> <div class="count">❔ 📨: {{ user.count }}</div></div>
{% endfor %}

</div>
{% endif %}

## 🔝 👨‍🔬

📥 **🔝 👨‍🔬**. 👶

👉 👩‍💻 ✔️ [✍ 🏆 🚲 📨](help-readyapi.md#create-a-pull-request){.internal-link target=_blank} 👈 ✔️ *🔗*.

👫 ✔️ 📉 ℹ 📟, 🧾, ✍, ♒️. 👶

{% if people %}
<div class="user-list user-list-center">
{% for user in people.top_contributors %}

<div class="user"><a href="{{ user.url }}" target="_blank"><div class="avatar-wrapper"><img src="{{ user.avatarUrl }}"/></div><div class="title">@{{ user.login }}</div></a> <div class="count">🚲 📨: {{ user.count }}</div></div>
{% endfor %}

</div>
{% endif %}

📤 📚 🎏 👨‍🔬 (🌅 🌘 💯), 👆 💪 👀 👫 🌐 <a href="https://github.com/khulnasoft/readyapi/graphs/contributors" class="external-link" target="_blank">ReadyAPI 📂 👨‍🔬 📃</a>. 👶

## 🔝 👨‍🔬

👫 👩‍💻 **🔝 👨‍🔬**. 👶 👶

### 📄 ✍

👤 🕴 💬 👩‍❤‍👨 🇪🇸 (&amp; 🚫 📶 👍 👶). , 👨‍🔬 🕐 👈 ✔️ [**🏋️ ✔ ✍**](contributing.md#translations){.internal-link target=_blank} 🧾. 🍵 👫, 📤 🚫🔜 🧾 📚 🎏 🇪🇸.

---

**🔝 👨‍🔬** 👶 👶 ✔️ 📄 🏆 🚲 📨 ⚪️➡️ 🎏, 🚚 🔆 📟, 🧾, &amp; ✴️, **✍**.

{% if people %}
<div class="user-list user-list-center">
{% for user in people.top_reviewers %}

<div class="user"><a href="{{ user.url }}" target="_blank"><div class="avatar-wrapper"><img src="{{ user.avatarUrl }}"/></div><div class="title">@{{ user.login }}</div></a> <div class="count">📄: {{ user.count }}</div></div>
{% endfor %}

</div>
{% endif %}

## 💰

👫 **💰**. 👶

👫 🔗 👇 👷 ⏮️ **ReadyAPI** (&amp; 🎏), ✴️ 🔘 <a href="https://github.com/sponsors/khulnasoft" class="external-link" target="_blank">📂 💰</a>.

{% if sponsors %}

{% if sponsors.gold %}

### 🌟 💰

{% for sponsor in sponsors.gold -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}" style="border-radius:15px"></a>
{% endfor %}
{% endif %}

{% if sponsors.silver %}

### 🥇1st 💰

{% for sponsor in sponsors.silver -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}" style="border-radius:15px"></a>
{% endfor %}
{% endif %}

{% if sponsors.bronze %}

### 🥈2nd 💰

{% for sponsor in sponsors.bronze -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}" style="border-radius:15px"></a>
{% endfor %}
{% endif %}

{% endif %}

### 🎯 💰

{% if github_sponsors %}
{% for group in github_sponsors.sponsors %}

<div class="user-list user-list-center">

{% for user in group %}
{% if user.login not in sponsors_badge.logins %}

<div class="user"><a href="{{ user.url }}" target="_blank"><div class="avatar-wrapper"><img src="{{ user.avatarUrl }}"/></div><div class="title">@{{ user.login }}</div></a></div>

{% endif %}
{% endfor %}

</div>

{% endfor %}
{% endif %}

## 🔃 📊 - 📡 ℹ

👑 🎯 👉 📃 🎦 🎯 👪 ℹ 🎏.

✴️ ✅ 🎯 👈 🛎 🌘 ⭐, &amp; 📚 💼 🌅 😩, 💖 🤝 🎏 ⏮️ ❔ &amp; ⚖ 🚲 📨 ⏮️ ✍.

💽 ⚖ 🔠 🗓️, 👆 💪 ✍ <a href="https://github.com/khulnasoft/readyapi/blob/master/.github/actions/people/app/main.py" class="external-link" target="_blank">ℹ 📟 📥</a>.

📥 👤 🎦 💰 ⚪️➡️ 💰.

👤 🏦 ▶️️ ℹ 📊, 📄, ⚡, ♒️ (💼 🤷).
