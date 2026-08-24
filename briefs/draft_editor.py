"""Tiny local editor for Rex's draft: renders markdown readably, allows inline
editing, and saves the edited text back to the .md source."""
import html as htmllib
import re
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote

SRC = r"C:\Users\raksh\portfolio-site\briefs\substack-01-germany-no-super-regulator.md"
PORT = 8763


def render_body(md_text: str) -> str:
    """Convert our limited markdown to HTML body."""
    text = re.sub(r"^---.*?---\n", "", md_text, flags=re.S)  # drop frontmatter
    text = re.sub(r"^## (.*)$", r"<h2>\1</h2>", text, flags=re.M)
    text = re.sub(r"^# (.*)$", r"<h1>\1</h1>", text, flags=re.M)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"<em>\1</em>", text)
    lines, out = text.split("\n"), []
    for ln in lines:
        s = ln.strip()
        if s.startswith("> "):
            out.append("<blockquote><p>" + s[2:] + "</p></blockquote>")
        elif s == "---":
            out.append("<hr>")
        elif s:
            out.append("<p>" + s + "</p>")
        else:
            out.append("")
    return "\n".join(out)


PAGE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Draft Editor — F-Brief #1</title>
<style>
  body { font-family: Georgia, serif; max-width: 700px; margin: 2rem auto;
         line-height: 1.7; font-size: 19px; color: #1a1a1a; padding: 0 1.5rem; }
  h1 { font-size: 1.9rem; line-height: 1.25; }
  h2 { font-size: 1.35rem; margin-top: 2.2rem; }
  blockquote { border-left: 4px solid #ccc; margin: 1.2rem 0;
               padding: 0.3rem 1.2rem; color: #444; font-style: italic; }
  hr { border: none; border-top: 1px solid #ddd; margin: 2.2rem 0; }
  [contenteditable]:focus { outline: 2px solid #bcd4ea; outline-offset: 6px; }
  .bar { position: fixed; top: 0; left: 0; right: 0; background: #f4f1ec;
         padding: 0.5rem 1.2rem; font-family: system-ui, sans-serif; font-size: 14px;
         display: flex; gap: 12px; align-items: center; box-shadow: 0 1px 4px rgba(0,0,0,.15); }
  button { font-size: 14px; padding: 6px 14px; cursor: pointer; }
  #status { color: #555; }
  main { margin-top: 3.2rem; }
</style></head>
<body>
<div class="bar">
  <button onclick="save()">Save</button>
  <span>or press Ctrl+S</span>
  <span id="status">Editing: substack-01-germany-no-super-regulator.md</span>
</div>
<main id="doc" contenteditable="true" spellcheck="true">
__BODY__
</main>
<script>
function save() {
  fetch('/save', { method: 'POST', body: document.getElementById('doc').innerHTML })
    .then(r => r.text())
    .then(t => { const s = document.getElementById('status');
                 s.textContent = t; setTimeout(() =>
                 s.textContent = 'Saved locally. Hermes reads this file directly.', 2500); });
}
document.addEventListener('keydown', e => {
  if ((e.ctrlKey || e.metaKey) && e.key === 's') { e.preventDefault(); save(); }
});
</script>
</body></html>"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):  # silence request logging
        pass

    def _send(self, code, ctype, body):
        data = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        md = open(SRC, encoding="utf-8").read()
        page = PAGE.replace("__BODY__", render_body(md))
        self._send(200, "text/html; charset=utf-8", page)

    def do_POST(self):
        if self.path != "/save":
            self._send(404, "text/plain", "not found")
            return
        length = int(self.headers.get("Content-Length", 0))
        edited_html = self.rfile.read(length).decode("utf-8")

        # Convert the edited DOM back to our markdown dialect.
        t = edited_html
        t = re.sub(r"<h1>(.*?)</h1>", r"# \1", t, flags=re.S)
        t = re.sub(r"<h2>(.*?)</h2>", r"## \1", t, flags=re.S)
        t = re.sub(r"<blockquote>\s*<p>(.*?)</p>\s*</blockquote>",
                   lambda m: "> " + m.group(1).replace("\n", "\n> "), t, flags=re.S)
        t = re.sub(r"<hr\s*/?>", "\n---\n", t)
        t = re.sub(r"<p>(.*?)</p>", lambda m: m.group(1) + "\n\n", t, flags=re.S)
        t = re.sub(r"<br\s*/?>", "\n", t)
        t = re.sub(r"</?(div|main|span|font|style|script)[^>]*>", "", t)
        t = t.replace("<strong>", "**").replace("</strong>", "**")
        t = re.sub(r"<em>(.*?)</em>", r"*\1*", t, flags=re.S)
        t = re.sub(r"<[^>]+>", "", t)          # strip anything remaining
        t = htmllib.unescape(t)
        t = re.sub(r"\n{3,}", "\n\n", t).strip() + "\n"

        with open(SRC, "w", encoding="utf-8") as f:
            f.write(t)
        self._send(200, "text/plain", "Saved.")


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Editor running at http://127.0.0.1:{PORT} -> {SRC}")
    server.serve_forever()
