---
entity_id: "molecule.C11143"
entity_type: "small_molecule"
name: "Dimethyl sulfoxide"
source_database: "KEGG"
source_id: "C11143"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Dimethyl sulfoxide"
  - "DMSO"
---

# Dimethyl sulfoxide

`molecule.C11143`

## Static

- Type: `small_molecule`
- Source: `KEGG:C11143`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Dimethyl sulfoxide; DMSO DMSO "Dimethyl sulfoxide" (DMSO) is naturally present in significant amounts (1200 nM) in ocean surface waters, probably originating from marine phytoplankton . In addition, DMSO is widely used in various industries since it dissolves many organic and inorganic substances. In Japan alone a total of 5000 tons of DMSO is produced per year for use in various industries. Much of the DMSO accumulates in wastewater, where it has toxic effects on many organisms .

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)

## Annotation

KEGG compound: Dimethyl sulfoxide; DMSO

## Pathways

- `eco00920` Sulfur metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.DIMESULFREDUCT-RXN|reaction.ecocyc.DIMESULFREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-273|reaction.ecocyc.TRANS-RXN0-273]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5262|reaction.ecocyc.RXN0-5262]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-273|reaction.ecocyc.TRANS-RXN0-273]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C11143`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
