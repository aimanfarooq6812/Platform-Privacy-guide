"""
Find the setting.
A plain-language index of the account and privacy controls that platforms bury.

Run locally:   streamlit run app.py
"""

import html

import streamlit as st

from data import GENERAL_NOTES, PLATFORMS

st.set_page_config(
    page_title="Find the setting",
    page_icon="🔑",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --------------------------------------------------------------------------- #
# Styling
# --------------------------------------------------------------------------- #

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  --lavender: #C894EE;
  --plum:     #821563;
  --indigo:   #1F0240;
  --violet:   #793A98;
  --royal:    #28064C;
  --bright:   #9F58E1;
  --orchid:   #CF61C8;
  --rose:     #BD3F89;
  --deep:     #350967;

  --ink:      #F4ECFC;
  --ink-soft: #CDB6E4;
  --ink-mute: #9E86BA;

  --line:     rgba(200, 148, 238, 0.16);
  --line-lit: rgba(200, 148, 238, 0.38);
  --card:     rgba(31, 2, 64, 0.44);
  --card-lit: rgba(53, 9, 103, 0.55);

  --accent: linear-gradient(135deg,
    #C894EE 0%, #821563 10%, #1F0240 20%, #793A98 30%, #28064C 40%,
    #821563 50%, #9F58E1 60%, #CF61C8 70%, #BD3F89 80%, #350967 100%);
}

/* ---------- page shell ---------- */

.stApp {
  background:
    radial-gradient(120% 70% at 12% -8%, rgba(200, 148, 238, 0.16), transparent 62%),
    radial-gradient(90% 55% at 92% 108%, rgba(207, 97, 200, 0.14), transparent 60%),
    linear-gradient(180deg, rgba(9, 2, 22, 0.80) 0%, rgba(9, 2, 22, 0.88) 100%),
    linear-gradient(135deg,
      #C894EE 0%, #821563 10%, #1F0240 20%, #793A98 30%, #28064C 40%,
      #821563 50%, #9F58E1 60%, #CF61C8 70%, #BD3F89 80%, #350967 100%);
  background-attachment: fixed, fixed, fixed, fixed;
  color: var(--ink);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

[data-testid="stHeader"] {
  background: linear-gradient(180deg, rgba(9, 2, 22, 0.94) 42%, rgba(9, 2, 22, 0));
  backdrop-filter: blur(7px);
}
/* hide Deploy + the burger menu, but NOT the sidebar button that sits in the toolbar */
[data-testid="stToolbarActions"],
[data-testid="stAppDeployButton"] { display: none !important; }
#MainMenu, footer { visibility: hidden; }

.block-container {
  max-width: 820px;
  padding-top: 3.5rem;
  padding-bottom: 5rem;
}

/* kill the default gap between stacked markdown blocks */
[data-testid="stMarkdownContainer"] > *:first-child { margin-top: 0; }

/* ---------- hamburger (sidebar open button) ---------- */

[data-testid="stExpandSidebarButton"],
[data-testid="stSidebarCollapsedControl"] button {
  display: flex !important;
  align-items: center;
  justify-content: center;
  width: 44px !important;
  height: 44px !important;
  border-radius: 13px !important;
  color: #E7D6F8 !important;
  background: rgba(31, 2, 64, 0.78) !important;
  border: 1px solid var(--line-lit) !important;
  backdrop-filter: blur(10px);
  transition: border-color .18s ease, background .18s ease;
}
[data-testid="stExpandSidebarButton"]:hover,
[data-testid="stSidebarCollapsedControl"] button:hover {
  border-color: var(--orchid) !important;
  background: rgba(53, 9, 103, 0.9) !important;
}
[data-testid="stExpandSidebarButton"] > *,
[data-testid="stSidebarCollapsedControl"] button > * { display: none !important; }
[data-testid="stExpandSidebarButton"]::before,
[data-testid="stSidebarCollapsedControl"] button::before {
  content: "";
  display: block;
  width: 18px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  box-shadow: 0 -6px 0 currentColor, 0 6px 0 currentColor;
}

/* collapse arrow inside the open sidebar */
[data-testid="stSidebarCollapseButton"] button { color: var(--ink-soft) !important; }

/* ---------- sidebar index ---------- */

[data-testid="stSidebar"] {
  background: linear-gradient(180deg, rgba(20, 3, 45, 0.97), rgba(12, 2, 30, 0.97));
  border-right: 1px solid var(--line);
}
[data-testid="stSidebar"] [data-testid="stSidebarContent"] { padding-top: 1rem; }

.idx-title {
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--ink-mute);
  padding: 0 0.35rem 0.75rem;
}
.idx-group {
  font-size: 0.62rem;
  font-weight: 600;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--ink-mute);
  padding: 1.15rem 0.35rem 0.45rem;
  border-top: 1px solid var(--line);
  margin-top: 0.6rem;
}
.idx-group:first-of-type { border-top: none; margin-top: 0; }
a.idx-link {
  display: block;
  padding: 0.46rem 0.55rem;
  margin-bottom: 1px;
  border-radius: 9px;
  border-left: 2px solid transparent;
  color: var(--ink-soft) !important;
  font-size: 0.9rem;
  font-weight: 450;
  text-decoration: none !important;
  transition: background .15s ease, color .15s ease, border-color .15s ease;
}
a.idx-link:hover {
  background: rgba(159, 88, 225, 0.16);
  border-left-color: var(--orchid);
  color: var(--ink) !important;
}
a.idx-link.lead {
  color: var(--ink) !important;
  font-weight: 550;
  background: rgba(159, 88, 225, 0.1);
  border-left-color: var(--lavender);
}
.idx-em { margin-right: 0.5rem; }

/* ---------- hero ---------- */

.anchor {
  display: block;
  position: relative;
  top: -5.5rem;
  visibility: hidden;
}

.hero { padding-bottom: 0.5rem; }
.eyebrow {
  font-size: 0.66rem;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--orchid);
  margin-bottom: 0.9rem;
}
.hero h1 {
  font-size: clamp(2.1rem, 6vw, 3.1rem);
  line-height: 1.06;
  font-weight: 700;
  letter-spacing: -0.035em;
  margin: 0 0 1rem;
  background: linear-gradient(120deg, #F4ECFC 10%, #C894EE 45%, #CF61C8 80%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}
.hero p.lede {
  font-size: 1.03rem;
  line-height: 1.65;
  color: var(--ink-soft);
  margin: 0 0 1.5rem;
  max-width: 60ch;
}
.rule { height: 2px; border: 0; background: var(--accent); border-radius: 2px; margin: 0 0 1.7rem; }

.how-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 0.7rem; margin-bottom: 1.4rem; }
.how-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 0.95rem 1.05rem;
}
.how-card .n {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  color: var(--orchid);
  display: block;
  margin-bottom: 0.4rem;
}
.how-card .t { font-size: 0.92rem; font-weight: 600; margin-bottom: 0.25rem; }
.how-card .d { font-size: 0.83rem; line-height: 1.5; color: var(--ink-mute); }

.hint {
  font-size: 0.86rem;
  color: var(--ink-mute);
  background: rgba(159, 88, 225, 0.09);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 0.7rem 0.95rem;
  margin-bottom: 2.6rem;
}
.hint b { color: var(--ink-soft); font-weight: 600; }

/* ---------- section headings ---------- */

.sec-head {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  margin: 2.4rem 0 1.1rem;
}
.sec-head span {
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--ink-mute);
  white-space: nowrap;
}
.sec-head:after { content: ""; flex: 1; height: 1px; background: var(--line); }

/* ---------- platform dropdown ---------- */

details { border: 0; }
summary { cursor: pointer; list-style: none; }
summary::-webkit-details-marker { display: none; }
summary:focus-visible { outline: 2px solid var(--orchid); outline-offset: 3px; border-radius: 12px; }

.platform {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 16px;
  margin-bottom: 0.6rem;
  overflow: hidden;
  transition: border-color .18s ease;
}
.platform:hover { border-color: var(--line-lit); }
.platform[open] { background: var(--card-lit); border-color: var(--line-lit); }

.p-sum {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 1.05rem 1.15rem;
}
.p-emoji { font-size: 1.15rem; line-height: 1; }
.p-name { font-size: 1.08rem; font-weight: 600; letter-spacing: -0.015em; flex: 1; }
.p-count {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.7rem;
  color: var(--ink-mute);
  white-space: nowrap;
}
.chev {
  width: 8px; height: 8px; flex: none;
  border-right: 2px solid var(--ink-mute);
  border-bottom: 2px solid var(--ink-mute);
  transform: rotate(45deg);
  margin: -4px 4px 0 2px;
  transition: transform .2s ease, border-color .2s ease;
}
.platform[open] > .p-sum .chev { transform: rotate(-135deg); margin-top: 3px; border-color: var(--lavender); }

.p-body { padding: 0 1.15rem 0.55rem; }

.grp-title {
  font-size: 0.63rem;
  font-weight: 600;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--ink-mute);
  padding: 1rem 0 0.5rem;
}

/* ---------- setting dropdown ---------- */

.setting {
  border: 1px solid var(--line);
  border-radius: 12px;
  margin-bottom: 0.4rem;
  background: rgba(9, 2, 22, 0.32);
  transition: border-color .16s ease;
}
.setting:hover { border-color: var(--line-lit); }
.setting[open] { border-color: var(--line-lit); background: rgba(9, 2, 22, 0.5); }

.s-sum {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.72rem 0.9rem;
}
.s-name { font-size: 0.94rem; font-weight: 500; flex: 1; }
.tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.62rem;
  letter-spacing: 0.04em;
  padding: 0.2rem 0.5rem;
  border-radius: 20px;
  white-space: nowrap;
  border: 1px solid var(--line-lit);
  color: var(--ink-soft);
}
.tag.permanent { color: #F4B8DC; border-color: rgba(189, 63, 137, 0.6); background: rgba(189, 63, 137, 0.14); }
.tag.reversible { color: #D9BBF5; border-color: rgba(159, 88, 225, 0.5); background: rgba(159, 88, 225, 0.12); }
.setting .chev { width: 7px; height: 7px; margin-right: 2px; }
.setting[open] > .s-sum .chev { transform: rotate(-135deg); margin-top: 3px; border-color: var(--lavender); }

.s-body { padding: 0 0.9rem 0.95rem; }
.what {
  font-size: 0.9rem;
  line-height: 1.6;
  color: var(--ink-soft);
  margin: 0 0 0.85rem;
  padding-top: 0.15rem;
}

/* ---------- the path trail ---------- */

.route { margin-bottom: 0.55rem; }
.route-label {
  font-size: 0.6rem;
  font-weight: 600;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--ink-mute);
  margin-bottom: 0.4rem;
}
.route-label em { font-style: normal; color: var(--orchid); }
.trail { display: flex; flex-wrap: wrap; align-items: center; gap: 0.3rem 0.1rem; }
.step {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.76rem;
  line-height: 1.35;
  padding: 0.26rem 0.55rem;
  border-radius: 7px;
  background: rgba(159, 88, 225, 0.14);
  border: 1px solid rgba(159, 88, 225, 0.22);
  color: #EBDCF9;
}
.step.last { background: rgba(207, 97, 200, 0.2); border-color: rgba(207, 97, 200, 0.42); color: #FBE7F6; }
.arrow { color: var(--ink-mute); font-size: 0.72rem; padding: 0 0.22rem; }

.note {
  font-size: 0.82rem;
  line-height: 1.55;
  color: var(--ink-mute);
  margin: 0.75rem 0 0;
  padding-left: 0.75rem;
  border-left: 2px solid var(--rose);
}

/* ---------- closing notes ---------- */

.note-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 1.05rem 1.15rem;
  margin-bottom: 0.6rem;
}
.note-card h3 { font-size: 0.95rem; font-weight: 600; margin: 0 0 0.45rem; color: var(--ink); }
.note-card p { font-size: 0.87rem; line-height: 1.6; color: var(--ink-mute); margin: 0; }

.foot {
  margin-top: 2.6rem;
  padding-top: 1.4rem;
  border-top: 1px solid var(--line);
  font-size: 0.8rem;
  line-height: 1.6;
  color: var(--ink-mute);
}

@media (max-width: 640px) {
  .block-container { padding-top: 4rem; padding-left: 1.1rem; padding-right: 1.1rem; }
  .p-count { display: none; }
}

@media (prefers-reduced-motion: reduce) {
  * { transition: none !important; }
}
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)


# --------------------------------------------------------------------------- #
# Rendering helpers
# --------------------------------------------------------------------------- #


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def render_trail(route: str) -> str:
    """Turn 'Settings → Privacy → Limits' into a chain of step pills."""
    label = ""
    if "|" in route:
        label, route = route.split("|", 1)

    steps = [s.strip() for s in route.split("→") if s.strip()]
    pills = []
    for i, step in enumerate(steps):
        last = " last" if i == len(steps) - 1 and len(steps) > 1 else ""
        if i:
            pills.append('<span class="arrow">→</span>')
        pills.append(f'<span class="step{last}">{esc(step)}</span>')

    head = "How to get there"
    if label:
        head = f"How to get there <em>· {esc(label.strip())}</em>"

    return (
        '<div class="route">'
        f'<div class="route-label">{head}</div>'
        f'<div class="trail">{"".join(pills)}</div>'
        "</div>"
    )


def render_item(item: dict) -> str:
    tag = ""
    if item.get("tag"):
        cls = ""
        low = item["tag"].lower()
        if low == "permanent":
            cls = " permanent"
        elif low in ("reversible", "safety net"):
            cls = " reversible"
        tag = f'<span class="tag{cls}">{esc(item["tag"])}</span>'

    routes = "".join(render_trail(r) for r in item["how"])
    note = f'<p class="note">{esc(item["note"])}</p>' if item.get("note") else ""

    return (
        '<details class="setting">'
        '<summary class="s-sum">'
        f'<span class="s-name">{esc(item["name"])}</span>{tag}'
        '<span class="chev"></span>'
        "</summary>"
        '<div class="s-body">'
        f'<p class="what">{esc(item["what"])}</p>'
        f"{routes}{note}"
        "</div>"
        "</details>"
    )


def render_platform(platform: dict) -> str:
    count = sum(len(g["items"]) for g in platform["groups"])
    body = []
    for group in platform["groups"]:
        body.append(f'<div class="grp-title">{esc(group["title"])}</div>')
        body.extend(render_item(item) for item in group["items"])

    return (
        f'<span class="anchor" id="{platform["slug"]}"></span>'
        '<details class="platform">'
        '<summary class="p-sum">'
        f'<span class="p-emoji">{platform["emoji"]}</span>'
        f'<span class="p-name">{esc(platform["name"])}</span>'
        f'<span class="p-count">{count} settings</span>'
        '<span class="chev"></span>'
        "</summary>"
        f'<div class="p-body">{"".join(body)}</div>'
        "</details>"
    )


# --------------------------------------------------------------------------- #
# Sidebar — the index
# --------------------------------------------------------------------------- #

sections: list[str] = []
for p in PLATFORMS:
    if p["section"] not in sections:
        sections.append(p["section"])

index_html = ['<div class="idx-title">Index</div>']
index_html.append('<a class="idx-link lead" href="#top">How to use this site</a>')

for section in sections:
    index_html.append(f'<div class="idx-group">{esc(section)}</div>')
    for p in PLATFORMS:
        if p["section"] == section:
            index_html.append(
                f'<a class="idx-link" href="#{p["slug"]}">'
                f'<span class="idx-em">{p["emoji"]}</span>{esc(p["name"])}</a>'
            )

index_html.append('<div class="idx-group">Worth knowing</div>')
index_html.append('<a class="idx-link" href="#notes">Before you delete anything</a>')

with st.sidebar:
    st.markdown("".join(index_html), unsafe_allow_html=True)


# --------------------------------------------------------------------------- #
# Page
# --------------------------------------------------------------------------- #

st.markdown(
    "".join(
        [
            '<span class="anchor" id="top"></span>',
            '<div class="hero">',
            '<div class="eyebrow">Privacy &amp; account control</div>',
            "<h1>The settings apps would rather you didn't find</h1>",
            '<p class="lede">Every platform hides its privacy controls somewhere different, and renames '
            "them every few months. This is a plain index of where they actually live — how to go quiet, "
            "how to pause an account, and how to leave for good.</p>",
            '<hr class="rule">',
            '<div class="how-grid">',
            '<div class="how-card"><span class="n">01</span><div class="t">Pick a platform</div>'
            '<div class="d">Scroll, or open the index with the ☰ button in the top-left corner.</div></div>',
            '<div class="how-card"><span class="n">02</span><div class="t">Open the setting</div>'
            '<div class="d">Each one explains in a line what it does, then shows the exact route to it.</div></div>',
            '<div class="how-card"><span class="n">03</span><div class="t">Follow the trail</div>'
            '<div class="d">Tap through the steps in order. The last step is the switch itself.</div></div>',
            "</div>",
            '<div class="hint"><b>Deactivate</b> hides your account and can be undone. '
            "<b>Delete</b> starts a countdown, and logging back in during it usually cancels the whole thing. "
            "Labels on each setting tell you which one you're looking at.</div>",
            "</div>",
        ]
    ),
    unsafe_allow_html=True,
)

for section in sections:
    st.markdown(
        f'<div class="sec-head"><span>{esc(section)}</span></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        "".join(render_platform(p) for p in PLATFORMS if p["section"] == section),
        unsafe_allow_html=True,
    )

st.markdown(
    "".join(
        [
            '<span class="anchor" id="notes"></span>',
            '<div class="sec-head"><span>Before you delete anything</span></div>',
        ]
        + [
            f'<div class="note-card"><h3>{esc(title)}</h3><p>{esc(body)}</p></div>'
            for title, body in GENERAL_NOTES
        ]
        + [
            '<div class="foot">Covers 17 platforms across social media, messaging and AI tools. '
            "Nothing here is stored or sent anywhere — it's a reference page, not a service.</div>"
        ]
    ),
    unsafe_allow_html=True,
)
