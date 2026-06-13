---
entity_id: "molecule.C02291"
entity_type: "small_molecule"
name: "L-Cystathionine"
source_database: "KEGG"
source_id: "C02291"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Cystathionine"
---

# L-Cystathionine

`molecule.C02291`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02291`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Cystathionine

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)

## Annotation

KEGG compound: L-Cystathionine

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.ecocyc.O-SUCCHOMOSERLYASE-RXN|reaction.ecocyc.O-SUCCHOMOSERLYASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-512|reaction.ecocyc.TRANS-RXN0-512]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.CYSTATHIONINE-BETA-LYASE-RXN|reaction.ecocyc.CYSTATHIONINE-BETA-LYASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15131|reaction.ecocyc.RXN-15131]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-512|reaction.ecocyc.TRANS-RXN0-512]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.TRANS-RXN0-593|reaction.ecocyc.TRANS-RXN0-593]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02291`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
