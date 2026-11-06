"""Cliente mínimo del MCP de Pixelab (HTTP) para lanzar lotes sin una llamada manual por imagen.

Lee el token de la variable de entorno PIXELLAB_API_TOKEN (nunca lo escribe en disco ni lo imprime).
Uso desde otros scripts:  from pixelab_mcp import Client; c = Client(); c.call("get_balance", {})
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request

URL = "https://api.pixellab.ai/mcp"


def _token_from_windows_user_env():
    """Si el proceso no heredó la variable, la lee de las variables de usuario de Windows (sin mostrarla)."""
    import subprocess
    try:
        out = subprocess.run(
            ["powershell", "-NoProfile", "-Command",
             '[Environment]::GetEnvironmentVariable("PIXELLAB_API_TOKEN","User")'],
            capture_output=True, text=True, timeout=20)
        return out.stdout.strip() or None
    except Exception:
        return None


class Client:
    def __init__(self, token=None, timeout=120):
        self.token = token or os.environ.get("PIXELLAB_API_TOKEN") or _token_from_windows_user_env()
        if not self.token:
            raise SystemExit("Falta la variable de entorno PIXELLAB_API_TOKEN")
        self.timeout = timeout
        self.session = None
        self._id = 0
        self._initialize()

    def _post(self, payload, expect_response=True):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "Authorization": "Bearer " + self.token,
        }
        if self.session:
            headers["Mcp-Session-Id"] = self.session
        req = urllib.request.Request(URL, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
        try:
            resp = urllib.request.urlopen(req, timeout=self.timeout)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")[:500]
            raise RuntimeError("HTTP %s: %s" % (e.code, body))
        sid = resp.headers.get("Mcp-Session-Id")
        if sid:
            self.session = sid
        raw = resp.read().decode("utf-8", "replace")
        if not expect_response or not raw.strip():
            return None
        ctype = resp.headers.get("Content-Type", "")
        if "text/event-stream" in ctype:
            msg = None
            for line in raw.splitlines():
                if line.startswith("data:"):
                    chunk = line[5:].strip()
                    if chunk:
                        msg = json.loads(chunk)
            return msg
        return json.loads(raw)

    def _initialize(self):
        self._id += 1
        r = self._post({
            "jsonrpc": "2.0", "id": self._id, "method": "initialize",
            "params": {"protocolVersion": "2025-03-26", "capabilities": {},
                       "clientInfo": {"name": "mrmak-lote", "version": "1.0"}},
        })
        if not r or "error" in r:
            raise RuntimeError("initialize falló: %r" % (r,))
        self._post({"jsonrpc": "2.0", "method": "notifications/initialized"}, expect_response=False)

    def call(self, name, arguments):
        """Devuelve el texto de la respuesta de la herramienta (y lanza si hay error)."""
        self._id += 1
        r = self._post({"jsonrpc": "2.0", "id": self._id, "method": "tools/call",
                        "params": {"name": name, "arguments": arguments}})
        if r is None:
            raise RuntimeError("sin respuesta")
        if "error" in r:
            raise RuntimeError(json.dumps(r["error"])[:500])
        res = r.get("result", {})
        text = "\n".join(c.get("text", "") for c in res.get("content", []) if c.get("type") == "text")
        if res.get("isError"):
            raise RuntimeError(text[:500])
        return text

    def tools(self):
        self._id += 1
        r = self._post({"jsonrpc": "2.0", "id": self._id, "method": "tools/list", "params": {}})
        return [t["name"] for t in r["result"]["tools"]]


if __name__ == "__main__":
    c = Client()
    print(c.call("get_balance", {}))
