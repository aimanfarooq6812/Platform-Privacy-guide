"""
Trapdoor — find the setting.
A plain-language index of the account and privacy controls that platforms bury.

Run locally:   streamlit run app.py
"""

import html

import streamlit as st

from data import GENERAL_NOTES, LAST_REVIEWED, PLATFORMS

st.set_page_config(
    page_title="Trapdoor — find the setting",
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
  --shell:      #FFF7FB;
  --petal:      #FDEBF4;
  --blush:      #FBDCEC;
  --rose:       #F7C2DD;
  --pink:       #E0568F;
  --pink-deep:  #C23A72;
  --pink-soft:  #F294BE;

  --ink:        #3F2231;
  --ink-soft:   #6B4257;
  --ink-mute:   #93697F;

  --line:       rgba(224, 86, 143, 0.18);
  --line-lit:   rgba(224, 86, 143, 0.38);
  --card:       rgba(255, 255, 255, 0.72);
  --card-lit:   #FFFFFF;

  --accent: linear-gradient(120deg,
    #F7C2DD 0%, #F294BE 28%, #E0568F 58%, #F294BE 82%, #FBDCEC 100%);
}

/* ---------- page shell ---------- */

.stApp {
  background:
    radial-gradient(120% 68% at 10% -10%, rgba(247, 194, 221, 0.55), transparent 62%),
    radial-gradient(95% 58% at 94% 106%, rgba(242, 148, 190, 0.34), transparent 62%),
    linear-gradient(180deg, #FFF7FB 0%, #FDEBF4 100%);
  background-attachment: fixed, fixed, fixed;
  color: var(--ink);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

[data-testid="stHeader"] {
  background: linear-gradient(180deg, rgba(255, 247, 251, 0.95) 42%, rgba(255, 247, 251, 0));
  backdrop-filter: blur(7px);
}
[data-testid="stToolbarActions"],
[data-testid="stAppDeployButton"] { display: none !important; }
#MainMenu, footer { visibility: hidden; }

.block-container {
  max-width: 820px;
  padding-top: 3.5rem;
  padding-bottom: 5rem;
}

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
  color: var(--pink-deep) !important;
  background: rgba(255, 255, 255, 0.86) !important;
  border: 1px solid var(--line-lit) !important;
  backdrop-filter: blur(10px);
  transition: border-color .18s ease, background .18s ease;
}
[data-testid="stExpandSidebarButton"]:hover,
[data-testid="stSidebarCollapsedControl"] button:hover {
  border-color: var(--pink) !important;
  background: #FFFFFF !important;
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

[data-testid="stSidebarCollapseButton"] button { color: var(--ink-soft) !important; }

/* ---------- sidebar index ---------- */

[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #FFFFFF 0%, #FEF3F8 100%);
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
  background: rgba(224, 86, 143, 0.1);
  border-left-color: var(--pink);
  color: var(--pink-deep) !important;
}
a.idx-link.lead {
  color: var(--pink-deep) !important;
  font-weight: 600;
  background: rgba(224, 86, 143, 0.08);
  border-left-color: var(--pink-soft);
}

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
  color: var(--pink);
  margin-bottom: 0.9rem;
}
.hero h1 {
  font-size: clamp(2.1rem, 6vw, 3.1rem);
  line-height: 1.06;
  font-weight: 700;
  letter-spacing: -0.035em;
  margin: 0 0 1rem;
  color: var(--ink);
}
.hero h1 em { font-style: normal; color: var(--pink); }
.hero p.lede {
  font-size: 1.03rem;
  line-height: 1.65;
  color: var(--ink-soft);
  margin: 0 0 1.5rem;
  max-width: 60ch;
}
.rule { height: 3px; border: 0; background: var(--accent); border-radius: 3px; margin: 0 0 1.7rem; }

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
  color: var(--pink);
  display: block;
  margin-bottom: 0.4rem;
}
.how-card .t { font-size: 0.92rem; font-weight: 600; margin-bottom: 0.25rem; color: var(--ink); }
.how-card .d { font-size: 0.83rem; line-height: 1.5; color: var(--ink-mute); }

.hint {
  font-size: 0.86rem;
  color: var(--ink-soft);
  background: rgba(251, 220, 236, 0.66);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 0.7rem 0.95rem;
  margin-bottom: 2.6rem;
}
.hint b { color: var(--pink-deep); font-weight: 600; }

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
summary:focus-visible { outline: 2px solid var(--pink); outline-offset: 3px; border-radius: 12px; }

.platform {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 16px;
  margin-bottom: 0.6rem;
  overflow: hidden;
  transition: border-color .18s ease, box-shadow .18s ease;
}
.platform:hover { border-color: var(--line-lit); }
.platform[open] {
  background: var(--card-lit);
  border-color: var(--line-lit);
  box-shadow: 0 2px 14px rgba(224, 86, 143, 0.08);
}

.p-sum {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 1.05rem 1.15rem;
}
.p-name { font-size: 1.08rem; font-weight: 600; letter-spacing: -0.015em; flex: 1; color: var(--ink); }
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
.platform[open] > .p-sum .chev { transform: rotate(-135deg); margin-top: 3px; border-color: var(--pink); }

.p-body { padding: 0 1.15rem 0.55rem; }

.grp-title {
  font-size: 0.63rem;
  font-weight: 600;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--pink);
  padding: 1rem 0 0.5rem;
}

/* ---------- setting dropdown ---------- */

.setting {
  border: 1px solid var(--line);
  border-radius: 12px;
  margin-bottom: 0.4rem;
  background: rgba(253, 235, 244, 0.5);
  transition: border-color .16s ease, background .16s ease;
}
.setting:hover { border-color: var(--line-lit); }
.setting[open] { border-color: var(--line-lit); background: rgba(253, 235, 244, 0.85); }

.s-sum {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.72rem 0.9rem;
}
.s-name { font-size: 0.94rem; font-weight: 500; flex: 1; color: var(--ink); }
.tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.62rem;
  letter-spacing: 0.04em;
  padding: 0.2rem 0.5rem;
  border-radius: 20px;
  white-space: nowrap;
  border: 1px solid var(--line-lit);
  color: var(--ink-soft);
  background: rgba(255, 255, 255, 0.7);
}
.tag.permanent { color: #A82B5E; border-color: rgba(194, 58, 114, 0.45); background: rgba(247, 194, 221, 0.5); }
.tag.reversible { color: #8A4E9E; border-color: rgba(168, 116, 190, 0.4); background: rgba(240, 222, 248, 0.6); }
.setting .chev { width: 7px; height: 7px; margin-right: 2px; }
.setting[open] > .s-sum .chev { transform: rotate(-135deg); margin-top: 3px; border-color: var(--pink); }

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
.route-label em { font-style: normal; color: var(--pink); }
.trail { display: flex; flex-wrap: wrap; align-items: center; gap: 0.3rem 0.1rem; }
.step {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.76rem;
  line-height: 1.35;
  padding: 0.26rem 0.55rem;
  border-radius: 7px;
  background: #FFFFFF;
  border: 1px solid rgba(224, 86, 143, 0.24);
  color: var(--ink-soft);
}
.step.last { background: rgba(247, 194, 221, 0.62); border-color: rgba(224, 86, 143, 0.45); color: var(--pink-deep); font-weight: 500; }
.arrow { color: var(--pink-soft); font-size: 0.72rem; padding: 0 0.22rem; }

.note {
  font-size: 0.82rem;
  line-height: 1.55;
  color: var(--ink-mute);
  margin: 0.75rem 0 0;
  padding-left: 0.75rem;
  border-left: 2px solid var(--pink-soft);
}

/* ---------- closing notes ---------- */

.note-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 1.05rem 1.15rem;
  margin-bottom: 0.6rem;
}
.note-card h3 { font-size: 0.95rem; font-weight: 600; margin: 0 0 0.45rem; color: var(--pink-deep); }
.note-card p { font-size: 0.87rem; line-height: 1.6; color: var(--ink-soft); margin: 0; }

/* ---------- update banner + footer ---------- */

.update {
  background: linear-gradient(120deg, rgba(251, 220, 236, 0.9), rgba(253, 235, 244, 0.7));
  border: 1px solid var(--line-lit);
  border-radius: 16px;
  padding: 1.25rem 1.35rem;
  margin-top: 2.6rem;
}
.update h3 {
  font-size: 1rem;
  font-weight: 600;
  margin: 0 0 0.5rem;
  color: var(--pink-deep);
}
.update p { font-size: 0.89rem; line-height: 1.65; color: var(--ink-soft); margin: 0 0 0.6rem; }
.update p:last-child { margin-bottom: 0; }
.update .stamp {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  color: var(--pink-deep);
  background: #FFFFFF;
  border: 1px solid var(--line-lit);
  border-radius: 20px;
  padding: 0.25rem 0.7rem;
  margin-top: 0.35rem;
}

.foot {
  margin-top: 1.6rem;
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
    """Turn 'Settings -> Privacy -> Limits' into a chain of step pills."""
    label = ""
    if "|" in route:
        label, route = route.split("|", 1)

    steps = [s.strip() for s in route.split("→") if s.strip()]
    pills = []
    for i, step in enumerate(steps):
        last = " last" if i == len(steps) - 1 and len(steps) > 1 else ""
        if i:
            pills.append('<span class="arrow">&rarr;</span>')
        pills.append(f'<span class="step{last}">{esc(step)}</span>')

    head = "How to get there"
    if label:
        head = f"How to get there <em>&middot; {esc(label.strip())}</em>"

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
                f'<a class="idx-link" href="#{p["slug"]}">{esc(p["name"])}</a>'
            )

index_html.append('<div class="idx-group">Worth knowing</div>')
index_html.append('<a class="idx-link" href="#notes">Before you delete anything</a>')
index_html.append('<a class="idx-link" href="#updates">How this site stays current</a>')

with st.sidebar:
    st.markdown("".join(index_html), unsafe_allow_html=True)


# --------------------------------------------------------------------------- #
# Page
# --------------------------------------------------------------------------- #

total_settings = sum(
    len(g["items"]) for p in PLATFORMS for g in p["groups"]
)

st.markdown(
    "".join(
        [
            '<span class="anchor" id="top"></span>',
            '<div class="hero">',
            '<div class="eyebrow">Privacy &amp; account control</div>',
            "<h1>The settings apps would rather you <em>didn't find</em></h1>",
            '<p class="lede">Every platform hides its privacy controls somewhere different, and renames '
            "them every few months. This is a plain index of where they actually live — how to go quiet, "
            "how to pause an account, and how to leave for good.</p>",
            '<hr class="rule">',
            '<div class="how-grid">',
            '<div class="how-card"><span class="n">01</span><div class="t">Pick a platform</div>'
            '<div class="d">Scroll, or open the index with the menu button in the top-left corner.</div></div>',
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
            '<span class="anchor" id="updates"></span>',
            '<div class="update">',
            "<h3>This site is kept up to date</h3>",
            "<p>Platforms move these controls constantly — a menu that was two taps deep last term can "
            "be somewhere else entirely by the next one, and some apps show different menus to different "
            "people at the same time.</p>",
            "<p>Because of that, every path on this page is reviewed and refreshed every few months, "
            "with new settings added as platforms release them and old ones corrected when they move. "
            "If something here doesn't match what you see on your screen, check the platform's own help "
            "centre — and the fix will land here at the next review.</p>",
            f'<span class="stamp">Last reviewed: {esc(LAST_REVIEWED)}</span>',
            "</div>",
            f'<div class="foot">Covers {len(PLATFORMS)} platforms and {total_settings} settings across '
            "social media, messaging and AI tools. Nothing here is stored or sent anywhere — "
            "it's a reference page, not a service.</div>",
        ]
    ),
    unsafe_allow_html=True,
)
