# 2026-10-22 AiPaper publish outcome

- article_count: 12 (all [10/22]; RSS 34 items = 10/20 ×10 · 10/21 ×12 · 10/22 ×12, keep_days=3; no double prefix; 10/19 dirs removed)
- edition commits: 5b5336a (edition) + 0c9f183 (drop 10/19 article pages — `git add` glob missed deletions; next time use `git add -A` on repo root but exclude notes/)
- no .pages-bump commit (WebSub)
- hub ping: `./ping_hub.sh 10/22` → live RSS had [10/22] + rel=hub on try 4 → HTTP 204 (first try). Hub topic-details: last successful fetch + last ping 2026-10-21 22:05 UTC (= 10/22 07:05 KST), no fetch error
- public RSS OK: plain newspaper.rss (cache-busted) lists 12 [10/22] titles + rel=hub
- article URL spot-check: town-ai-business, kronos-kline-foundation-model → 200; old 10/19 dir (tradingagents-070-chatgpt-plan) → 404 as expected
- Inoreader: NOT touched (no ?v= resub, per WebSub setup)
- notes/reader-signal.md: still untracked on purpose (public repo)

## AI 비즈니스: Town (new case)
- $108M Series B (Forerunner + Menlo co-lead) 10/19, unicorn valuation; ≥$160M total; launched publicly ~June; "millions ARR within weeks"
- Pricing: Free $0 (30 chats/mo), Starter $15, Pro $49, Power $99, Power Plus $199, Team $59/seat, Team Plus $149/seat (annual rate); overage $0.030–0.044/credit

## Design (3)
- Figma MCP 20 partners + Field's "asymmetric context sharing" critique
- Pure UI in the Agentic Era (state grid review)
- Brand longevity (Design Week) — fresh angle

## Reader-signal shaped: IBKR Autonomous Trading (MT5/agent-trading safety), ai-memory (obsidian/memory freshness), Figma MCP (Design)

## Used AI 비즈니스 list add: Town (2026-10-22)
Full used list: Axios Direct, TNL Daily, Ground News Vantage, Creatify Boreal, Beta Briefing, CORBrief Studio, Lovable, Gamma, Perplexity, Notion, Canva, ElevenLabs, Runway, HeyGen, Synthesia, Midjourney, Suno, Replit, Cursor, Higgsfield, Vercel v0, Framer, Fin/Intercom, Granola, Clueso, Descript, Modal, Ramp, Kling AI, Anthropic, Tolan, Otter.ai, Town
