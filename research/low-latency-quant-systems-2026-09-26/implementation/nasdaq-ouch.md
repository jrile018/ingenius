# Nasdaq OUCH 5.0 order-entry protocol

## Evidence

Nasdaq's October 2025 OUCH 5.0 specification defines its low-level native order-entry protocol. It describes fixed-length logical messages, binary big-endian data, implied-decimal prices, account/port identity, day-unique increasing user references, fault-redundant hosts, benign retransmission of inbound requests, and sequential processing on one connection. Inbound actions include enter, replace, cancel/partial cancel, modify, mass cancel, and session controls; outbound events include accepted, replaced, canceled, executed, broken trade, rejected, cancel pending/reject, priority update, modified, and restated.

## Skill use

A gateway benchmark needs a protocol-version-pinned parser and an explicit order-state machine. Test field widths, byte order, price scaling, message lengths, optional appendages, monotonically increasing identifiers, duplicates/retransmission, mirrored-session recovery, partial fills, replace chains, and every reject/cancel outcome used by the application. Replacements and partial cancels have liability and priority semantics that cannot be simplified into a generic update without tests.

## Limits

This is venue- and revision-specific. Recheck the current Nasdaq specification, certification environment, lower-level transport, and account rules before implementation. Public access does not establish an open redistribution license; link and paraphrase rather than embedding the document.

## Source

- [Nasdaq OUCH 5.0 Order Entry Specification, updated October 2025](https://www.nasdaqtrader.com/content/technicalsupport/specifications/TradingProducts/OUCH5.0.pdf)
