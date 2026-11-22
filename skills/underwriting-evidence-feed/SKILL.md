---
name: underwriting-evidence-feed
description: "Review control coverage, freshness and missing evidence for the packet versions a member is authorized to read."
---

# Underwriting Evidence Feed

Use `cryptodam_underwriting_evidence_feed` after the user grants `workspace:read`. With no arguments it lists at most 100 recent versions. Identify a version by its returned packet ID, then pass that value as `packetId`. Explain the UTC reporting date, version, review status, documented controls out of all required controls, source categories and stale, undated, future or missing evidence. Compare with the prior accessible version only when returned. Link the packet in CryptoDam to inspect the underlying evidence.

A declaration documents a claim; the reviewed packet and freshness counts do not decide insurance eligibility, risk, premiums or payouts. If access is denied or a record is unavailable, direct the user to the trusted app or consent flow. Never ask for credential strings, raw artifacts, private source exports, another account ID or a recipient list.

한국어로 요청하면 접근 권한이 있는 버전의 출처 분류, 누락, 유효기간과 이전 버전 대비 변화를 설명하세요. 근거 원문 열람 및 공유 권한 관리는 CryptoDam에서 진행합니다.
