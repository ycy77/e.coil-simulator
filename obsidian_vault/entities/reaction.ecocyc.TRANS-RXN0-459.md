---
entity_id: "reaction.ecocyc.TRANS-RXN0-459"
entity_type: "reaction"
name: "TRANS-RXN0-459"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-459"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-459

`reaction.ecocyc.TRANS-RXN0-459`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-459`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Methanol is produced as the end product of MCP (methyl accepting chemotaxis protein) demethylation . [3H]methanol is detected in the cell free medium from E. coli cells incubated with methyl-3H methionine to label the methyl group of their MCPs and then treated to specifically demethylate these proteins . EcoCyc reaction equation: METOH -> METOH; direction=LEFT-TO-RIGHT. Methanol is produced as the end product of MCP (methyl accepting chemotaxis protein) demethylation . [3H]methanol is detected in the cell free medium from E. coli cells incubated with methyl-3H methionine to label the methyl group of their MCPs and then treated to specifically demethylate these proteins .

## Biological Role

Substrates: Methanol (molecule.C00132). Products: Methanol (molecule.C00132).

## Annotation

Methanol is produced as the end product of MCP (methyl accepting chemotaxis protein) demethylation . [3H]methanol is detected in the cell free medium from E. coli cells incubated with methyl-3H methionine to label the methyl group of their MCPs and then treated to specifically demethylate these proteins .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00132|molecule.C00132]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00132|molecule.C00132]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-459`

## Notes

METOH -> METOH; direction=LEFT-TO-RIGHT
