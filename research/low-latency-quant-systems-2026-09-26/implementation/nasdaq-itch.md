# Nasdaq TotalView-ITCH 5.0 market-data protocol

## Evidence

Nasdaq's TotalView-ITCH 5.0 specification defines a sequenced stream of system, directory, trading-status, add-order, execution, cancel, delete, replace, trade, cross, imbalance, and broken-trade messages. Common headers include stock-locate codes, tracking numbers, and nanoseconds-since-midnight timestamps. Order-reference numbers connect add and subsequent modify events; partial executions are cumulative; replace events retire the old reference and establish a new one; broken trades have different implications for statistics and displayed-book state.

## Skill use

A feed-handler oracle should parse exact lengths and types, maintain day/session state, apply adds/executions/cancels/deletes/replaces in sequence, retain inherited fields across replacement, prevent negative displayed quantity, and separate book state from time-and-sales/statistics. Test multiple partial executions, execution-at-different-price, order death at zero quantity, non-displayable trades, crosses, halts, end-of-day messages, and broken trades. Record the protocol revision with captured data and benchmark fixtures.

## Limits

ITCH describes observable Nasdaq feed semantics, not all hidden venue state or every market. The public document's revision history is long and the live specification can change. Public access does not establish an open redistribution license; link and paraphrase.

## Source

- [Nasdaq TotalView-ITCH 5.0 Specification](https://www.nasdaqtrader.com/content/technicalsupport/specifications/dataproducts/NQTVITCHSpecification.pdf)
