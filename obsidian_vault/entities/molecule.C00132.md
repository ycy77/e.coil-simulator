---
entity_id: "molecule.C00132"
entity_type: "small_molecule"
name: "Methanol"
source_database: "KEGG"
source_id: "C00132"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Methanol"
  - "Methyl alcohol"
  - "CH3OH"
---

# Methanol

`molecule.C00132`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00132`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Methanol; Methyl alcohol; CH3OH

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 10 reaction(s).

## Enriched Pathways

- `eco00650` Butanoate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Annotation

KEGG compound: Methanol; Methyl alcohol; CH3OH

## Pathways

- `eco00650` Butanoate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Outgoing Edges (13)

- `activates` --> [[reaction.ecocyc.3-OCTAPRENYL-4-OHBENZOATE-DECARBOX-RXN|reaction.ecocyc.3-OCTAPRENYL-4-OHBENZOATE-DECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R02362|reaction.R02362]] `KEGG` `database` - C00714 + n C00001 <=> n C00132 + C00470
- `is_product_of` --> [[reaction.R02624|reaction.R02624]] `KEGG` `database` - C04142 + C00001 <=> C00614 + C00132
- `is_product_of` --> [[reaction.ecocyc.MCPMETEST-RXN|reaction.ecocyc.MCPMETEST-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MCPTAP-RXN|reaction.ecocyc.MCPTAP-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MCPTAR-RXN|reaction.ecocyc.MCPTAR-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MCPTRG-RXN|reaction.ecocyc.MCPTRG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.MCPTSR-RXN|reaction.ecocyc.MCPTSR-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-11483|reaction.ecocyc.RXN-11483]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6994|reaction.ecocyc.RXN0-6994]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-459|reaction.ecocyc.TRANS-RXN0-459]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00602|reaction.R00602]] `KEGG` `database` - C00132 + C00027 <=> C00067 + 2 C00001
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-459|reaction.ecocyc.TRANS-RXN0-459]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00132`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
