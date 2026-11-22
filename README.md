# CryptoDam & Hailey for ChatGPT

Portable plugin package for a ChatGPT connection to CryptoDam’s Payday Floor scenarios, authorized Underwriting Evidence Feed summaries, safety references and the member’s own Hailey watchlist and alerts.

**Not published in OpenAI's public directory; no public listing link exists.** This repository distributes the package and documentation; it does not establish a successful connection, runtime validation or OpenAI approval.

## Package and connection guide

- [Download the core plugin ZIP](downloads/cryptodam-openai-plugin-0.3.0.zip) · [SHA-256 checksum](downloads/SHA256SUMS.txt)
- [Website connection guide](https://www.stuporeinvestment.com/connect/chatgpt/)
- [Public package source](https://github.com/FreeWorldHere/cryptodam-openai)

The ZIP contains `plugin.json`, `mcp.json`, the icon and six skills. It is the plugin upload candidate; this repository's source-code ZIP includes additional documentation and is not the same artifact. Directory upload remains subject to OpenAI's requirements. Version 0.3.0 adds two workflows. Their tools become available when the corresponding CryptoDam server release is deployed.

## Intended core capabilities

- Model USDC receipts in EURC using the rates and fees supplied by the user. Read a saved plan count with separate workspace consent.
- Inspect coverage, freshness and gaps for accessible evidence packet versions. Record access is checked on each call.

- Find CryptoDam security and emergency-recovery guides, with the returned source links.
- Read available curated exchange profiles, distinguishing an assessed profile from a name/website-only listing.
- Check supported public wallet-address formats and explain available risk labels. A valid format or absent risk label does not prove safety, ownership or recoverability.
- Summarize the connected member's own Hailey watchlist and non-archived alerts without changing them.

The prepared account contract returns a limited window: up to the newest 200 joined watchlist records and 100 non-archived alerts. Older records may not be included. Watchlist totals may exceed returned items; alerts do not provide a complete-history total. Empty results, inactive/muted alerts, missing prices and stale observations must be described honestly.

This initial package excludes the optional market-analysis and model-portfolio skills. Excluding a skill does not hide or disable tools on the shared server; the actual connection and its permissions determine availability. No trades, transfers, payouts or account changes are part of these workflows.

## Connecting and availability

Read [CONNECTING.md](CONNECTING.md) for the existing MCP URL, consent scopes and trusted sign-in guidance. A custom MCP connection is separate from an OpenAI public-directory listing. Availability depends on the user's ChatGPT plan, region, client, workspace administrator and supported connection settings. Neither route guarantees visibility in every account or surface.

The prepared initial listing targets South Korea and the United States. Public directory publication requires OpenAI's review and approval; a website or public GitHub repository alone cannot make the connection appear in search. A public GitHub repository is not an OpenAI submission requirement.

## Links

- [CryptoDam website](https://www.stuporeinvestment.com)
- [Support](https://www.stuporeinvestment.com/contact)
- [Privacy policy](https://www.stuporeinvestment.com/privacy)
- [Terms](https://www.stuporeinvestment.com/terms)
- [Security reporting](SECURITY.md)
- [Content and distribution rights](RIGHTS.md)

No application source, backend implementation, operational logs, credentials or user data are included in this public package repository. The private application repository is not an installation dependency.

## 한국어 안내

CryptoDam & Hailey는 보안·복구 참고 자료, 지원하는 공개 지갑 주소의 형식, 연결한 본인의 관심 목록과 알림을 읽기 전용으로 안내하기 위한 패키지입니다. 관심 목록과 알림은 반환 수에 제한이 있어 이전 기록 전체를 보장하지 않습니다.

현재 OpenAI 공개 디렉터리에 게시되지 않았으며 공개 설치 링크도 없습니다. 별도의 사용자 지정 MCP 연결은 공개 디렉터리 등록과 다르며, 계정·요금제·지역·클라이언트·관리자 설정에 따라 제공 여부가 달라집니다. 거래·송금·지급 승인·계정 변경을 수행하지 않습니다. 비밀번호, 인증 코드, 개인 키 또는 복구 구문을 채팅이나 GitHub에 올리지 마세요.
