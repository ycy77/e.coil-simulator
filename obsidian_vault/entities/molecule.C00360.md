---
entity_id: "molecule.C00360"
entity_type: "small_molecule"
name: "dAMP"
source_database: "KEGG"
source_id: "C00360"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dAMP"
  - "2'-Deoxyadenosine 5'-phosphate"
  - "2'-Deoxyadenosine 5'-monophosphate"
  - "Deoxyadenylic acid"
  - "Deoxyadenosine monophosphate"
---

# dAMP

`molecule.C00360`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00360`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dAMP; 2'-Deoxyadenosine 5'-phosphate; 2'-Deoxyadenosine 5'-monophosphate; Deoxyadenylic acid; Deoxyadenosine monophosphate

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)

## Annotation

KEGG compound: dAMP; 2'-Deoxyadenosine 5'-phosphate; 2'-Deoxyadenosine 5'-monophosphate; Deoxyadenylic acid; Deoxyadenosine monophosphate

## Pathways

- `eco00230` Purine metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.RXN-18739|reaction.ecocyc.RXN-18739]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-384|reaction.ecocyc.RXN0-384]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14161|reaction.ecocyc.RXN-14161]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ADENPRIBOSYLTRAN-RXN|reaction.ecocyc.ADENPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-384|reaction.ecocyc.RXN0-384]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00360`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
