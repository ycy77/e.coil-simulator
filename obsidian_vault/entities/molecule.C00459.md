---
entity_id: "molecule.C00459"
entity_type: "small_molecule"
name: "dTTP"
source_database: "KEGG"
source_id: "C00459"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "dTTP"
  - "Deoxythymidine triphosphate"
  - "Deoxythymidine 5'-triphosphate"
  - "TTP"
---

# dTTP

`molecule.C00459`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00459`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: dTTP; Deoxythymidine triphosphate; Deoxythymidine 5'-triphosphate; TTP

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: dTTP; Deoxythymidine triphosphate; Deoxythymidine 5'-triphosphate; TTP

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (13)

- `activates` --> [[reaction.ecocyc.RXN0-746|reaction.ecocyc.RXN0-746]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.DTDPKIN-RXN|reaction.ecocyc.DTDPKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00378|reaction.R00378]] `KEGG` `database` - C00459 + C00039 <=> C00013 + C00039
- `is_substrate_of` --> [[reaction.R02328|reaction.R02328]] `KEGG` `database` - C00459 + C00103 <=> C00013 + C00842
- `is_substrate_of` --> [[reaction.ecocyc.DTDPGLUCOSEPP-RXN|reaction.ecocyc.DTDPGLUCOSEPP-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5107|reaction.ecocyc.RXN0-5107]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DCTP-DEAM-RXN|reaction.ecocyc.DCTP-DEAM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DTMPKI-RXN|reaction.ecocyc.DTMPKI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN|reaction.ecocyc.GTP-CYCLOHYDRO-I-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN|reaction.ecocyc.H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-3741|reaction.ecocyc.RXN0-3741]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-745|reaction.ecocyc.RXN0-745]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.THYKI-RXN|reaction.ecocyc.THYKI-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00459`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
