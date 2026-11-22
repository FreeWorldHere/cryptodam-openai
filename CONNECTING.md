# Connecting CryptoDam & Hailey

**Not published in OpenAI's public directory; no public listing link exists.** These are preparation instructions, not evidence that connection checks have passed.

## Existing connection metadata

| Field | Value |
| --- | --- |
| Display name | CryptoDam & Hailey |
| MCP URL | `https://www.stuporeinvestment.com/mcp` |
| Transport | Streamable HTTP |
| Authentication declared by the prepared package | OAuth with dynamic client registration (DCR) |
| Reference consent | `reference:read` — CryptoDam reference information |
| Workspace consent | `workspace:read` — saved Payday Floor plan count and summaries of authorized evidence packet versions |
| Account consent | `account:read` — the signed-in member's own Hailey watchlist and alerts |

The URL is the existing service. These documents do not provision a server, change its authentication, create credentials or establish OAuth compatibility with a particular ChatGPT client. No extra identity scopes, client IDs or secret overrides are supplied here.

## Where a connection can be added

If your ChatGPT account and workspace permit custom remote MCP connections, use the connection controls offered by that client and enter the URL above. The control names and availability can vary. If no appropriate control exists, consult your workspace administrator or [OpenAI's official documentation](https://developers.openai.com/plugins/); do not disable organization protections or substitute a database/service key.

When a public directory listing is approved, its actual listing link can be added here. Do not infer a public installation URL from the display name. A GitHub repository, website link or local ZIP does not register the connection for all ChatGPT users.

## Trusted sign-in and consent

1. Start the connection from the client's trusted connection controls.
2. Complete CryptoDam sign-in and any required MFA in the trusted browser flow. Review the destination and requested permissions before continuing.
3. A new workspace request shows its own scope on CryptoDam’s consent screen. Consent only to the access you want. `account:read` is for your account; it does not grant access to other members' private records.
4. Finish **Create as a plugin** where offered, locate and install the resulting plugin, then select it with **@** in your conversation. Use the equivalent controls if your client labels them differently; these controls may not be available in every account.
5. Inspect the tools the installed connection actually makes available. A missing tool, permission error or empty list is not proof that another capability works.

Never paste passwords, MFA codes, authorization codes, tokens, callback URLs containing codes, private keys, recovery phrases or API keys into a chat, issue or support request. Do not use another member's login or request broader backend privileges to resolve an error.

You can review or disconnect access through CryptoDam's Connected applications settings. Disconnecting does not remove answers or records already saved in a separate client; consult that client's controls and the [privacy policy](https://www.stuporeinvestment.com/privacy).

## Known coverage limits

The prepared core package provides guidance for references, public-address checks and your own account summaries. Watchlists and alerts may be partial rather than complete history. Returned sources, timestamps, missing data and inactive/muted alert status matter. See [README.md](README.md).

Optional market or portfolio tools may be unavailable. Do not activate providers, change permissions or enable settings simply to follow these instructions. If connection fails, send only a sanitized error description to [support](https://www.stuporeinvestment.com/contact).

## 한국어 안내

사용 중인 ChatGPT가 사용자 지정 원격 MCP 연결을 허용하는 경우에만 공식 연결 화면에 위 URL을 입력하세요. 공개 디렉터리 등록과는 별개이며 모든 사용자에게 제공되는 기능은 아닙니다. CryptoDam의 신뢰할 수 있는 로그인·동의 화면에서 필요한 권한만 승인하고, 인증 정보는 채팅이나 GitHub에 공유하지 마세요.
