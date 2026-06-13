---
entity_id: "molecule.C01909"
entity_type: "small_molecule"
name: "Dethiobiotin"
source_database: "KEGG"
source_id: "C01909"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Dethiobiotin"
  - "Desthiobiotin"
---

# Dethiobiotin

`molecule.C01909`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01909`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Dethiobiotin; Desthiobiotin

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)

## Annotation

KEGG compound: Dethiobiotin; Desthiobiotin

## Pathways

- `eco00780` Biotin metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R03182|reaction.R03182]] `KEGG` `database` - C00002 + C01037 + C00011 <=> C00008 + C00009 + C01909
- `is_product_of` --> [[reaction.ecocyc.DETHIOBIOTIN-SYN-RXN|reaction.ecocyc.DETHIOBIOTIN-SYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN1ZN3-10|reaction.ecocyc.RXN1ZN3-10]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-25310|reaction.ecocyc.RXN-25310]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RXN0-5055|reaction.ecocyc.RXN0-5055]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01909`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
