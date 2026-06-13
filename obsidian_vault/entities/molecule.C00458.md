---
entity_id: "molecule.C00458"
entity_type: "small_molecule"
name: "dCTP"
source_database: "KEGG"
source_id: "C00458"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dCTP"
  - "Deoxycytidine 5'-triphosphate"
  - "Deoxycytidine triphosphate"
  - "2'-Deoxycytidine 5'-triphosphate"
---

# dCTP

`molecule.C00458`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00458`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dCTP; Deoxycytidine 5'-triphosphate; Deoxycytidine triphosphate; 2'-Deoxycytidine 5'-triphosphate

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: dCTP; Deoxycytidine 5'-triphosphate; Deoxycytidine triphosphate; 2'-Deoxycytidine 5'-triphosphate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (9)

- `activates` --> [[reaction.ecocyc.THYKI-RXN|reaction.ecocyc.THYKI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.DCDPKIN-RXN|reaction.ecocyc.DCDPKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-723|reaction.ecocyc.RXN0-723]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00377|reaction.R00377]] `KEGG` `database` - C00458 + C00039 <=> C00013 + C00039
- `is_substrate_of` --> [[reaction.ecocyc.DCTP-DEAM-RXN|reaction.ecocyc.DCTP-DEAM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DCTP-PYROPHOSPHATASE-RXN|reaction.ecocyc.DCTP-PYROPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DTMPKI-RXN|reaction.ecocyc.DTMPKI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-3741|reaction.ecocyc.RXN0-3741]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5515|reaction.ecocyc.RXN0-5515]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00458`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
