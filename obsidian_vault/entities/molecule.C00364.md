---
entity_id: "molecule.C00364"
entity_type: "small_molecule"
name: "dTMP"
source_database: "KEGG"
source_id: "C00364"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dTMP"
  - "Thymidine 5'-phosphate"
  - "Deoxythymidine 5'-phosphate"
  - "Thymidylic acid"
  - "5'-Thymidylic acid"
  - "Thymidine monophosphate"
  - "Deoxythymidylic acid"
  - "Thymidylate"
---

# dTMP

`molecule.C00364`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00364`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dTMP; Thymidine 5'-phosphate; Deoxythymidine 5'-phosphate; Thymidylic acid; 5'-Thymidylic acid; Thymidine monophosphate; Deoxythymidylic acid; Thymidylate

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

KEGG compound: dTMP; Thymidine 5'-phosphate; Deoxythymidine 5'-phosphate; Thymidylic acid; 5'-Thymidylic acid; Thymidine monophosphate; Deoxythymidylic acid; Thymidylate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.RXN0-5107|reaction.ecocyc.RXN0-5107]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.THYKI-RXN|reaction.ecocyc.THYKI-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.THYMIDYLATESYN-RXN|reaction.ecocyc.THYMIDYLATESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DTMPKI-RXN|reaction.ecocyc.DTMPKI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.THYMIDYLATE-5-PHOSPHATASE-RXN|reaction.ecocyc.THYMIDYLATE-5-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00364`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
