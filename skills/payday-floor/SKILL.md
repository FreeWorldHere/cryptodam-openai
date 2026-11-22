---
name: payday-floor
description: "Model how much EURC a set of expected USDC receipts could yield at the rates and fees a user supplies."
---

# Payday Floor

Use `cryptodam_model_payday_floor` for a user-supplied scenario. Ask for the USDC cap, inclusive UTC expiry date, receipt amounts and arrival dates, expected EURC per USDC at spot, and spot fee in basis points. An unknown arrival date can be omitted. For a floor comparison, obtain the floor rate in the same direction, the upfront premium and the flat exercise fee in EURC. Confirm a zero fee with the user. Avoid personal names, addresses and invoices.

Identify assumptions and report the on-time amount, covered amount, spot-only net, exercise net, lapse net and improvement or loss against spot. A favorable market, late receipts or paying the premium can change the result. The output is in tokens; it does not establish a cash-out rate, executable quote or reserve. Use `cryptodam_my_payday_floor` only to show the connected member's saved plan count and link, after explicit workspace consent.

한국어로 요청하면 입력한 조건으로 계산한 USDC·EURC 결과, 만기일과 수수료를 설명하세요. 실제 견적을 발행하거나 송금을 요청하지 마세요.
