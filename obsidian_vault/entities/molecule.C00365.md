---
entity_id: "molecule.C00365"
entity_type: "small_molecule"
name: "dUMP"
source_database: "KEGG"
source_id: "C00365"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dUMP"
  - "Deoxyuridylic acid"
  - "Deoxyuridine monophosphate"
  - "Deoxyuridine 5'-phosphate"
  - "2'-Deoxyuridine 5'-phosphate"
---

# dUMP

`molecule.C00365`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00365`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dUMP; Deoxyuridylic acid; Deoxyuridine monophosphate; Deoxyuridine 5'-phosphate; 2'-Deoxyuridine 5'-phosphate

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

KEGG compound: dUMP; Deoxyuridylic acid; Deoxyuridine monophosphate; Deoxyuridine 5'-phosphate; 2'-Deoxyuridine 5'-phosphate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.DURIDKI-RXN|reaction.ecocyc.DURIDKI-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DUTP-PYROP-RXN|reaction.ecocyc.DUTP-PYROP-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14143|reaction.ecocyc.RXN-14143]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.THYMIDYLATESYN-RXN|reaction.ecocyc.THYMIDYLATESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DTMPKI-RXN|reaction.ecocyc.DTMPKI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00365`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
