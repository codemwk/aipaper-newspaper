#!/usr/bin/env bash
# Ping the WebSub hub after a publish so Inoreader gets today's items by push.
# Usage: ./ping_hub.sh [M/D]   e.g. ./ping_hub.sh 10/22
#   If a [M/D] tag is given, first waits (up to ~5 min) until the live plain RSS
#   contains a "[M/D]" title and rel="hub"; then pings the hub for RSS + Atom.
# Exit 0 = hub accepted (HTTP 204); non-zero otherwise.
set -euo pipefail
HUB="https://pubsubhubbub.appspot.com/"
RSS="https://codemwk.github.io/aipaper-newspaper/feeds/newspaper.rss"
ATOM="https://codemwk.github.io/aipaper-newspaper/feeds/newspaper.xml"
TAG="${1:-}"

if [[ -n "$TAG" ]]; then
  for i in $(seq 1 30); do
    body=$(curl -fsS -H 'Cache-Control: no-cache' "$RSS?nocache=$(date +%s)" || true)
    if grep -q "<title>\[$TAG\]" <<<"$body" && grep -q 'rel="hub"' <<<"$body"; then
      echo "live RSS has [$TAG] + rel=hub (try $i)"; break
    fi
    [[ $i -eq 30 ]] && { echo "live RSS not updated with [$TAG] after ~5 min; not pinging" >&2; exit 2; }
    sleep 10
  done
fi

code=$(curl -s -o /dev/null -w '%{http_code}' -X POST "$HUB" \
  -d hub.mode=publish --data-urlencode "hub.url=$RSS" --data-urlencode "hub.url=$ATOM")
echo "hub ping HTTP $code"
echo "check: ${HUB}topic-details?hub.url=$RSS"
[[ "$code" == "204" ]]
