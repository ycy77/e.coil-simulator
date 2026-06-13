---
entity_id: "reaction.ecocyc.RXN0-1862"
entity_type: "reaction"
name: "RXN0-1862"
source_database: "EcoCyc"
source_id: "RXN0-1862"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1862

`reaction.ecocyc.RXN0-1862`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1862`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-4-AMINO-4-DEOXY-L-ARABINOSE + FORMYL-THF-GLU-N -> UDP-L-ARA4-FORMYL-N + THF-GLU-N + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: UDP-4-AMINO-4-DEOXY-L-ARABINOSE + FORMYL-THF-GLU-N -> UDP-L-ARA4-FORMYL-N + THF-GLU-N + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by UDP-4-amino-4-deoxy-L-arabinose formyltransferase/UDP-glucuronate dehydrogenase (complex.ecocyc.CPLX0-7718). Substrates: UDP-L-Ara4N (molecule.C16153), an N10-formyltetrahydrofolate (molecule.ecocyc.FORMYL-THF-GLU-N). Products: H+ (molecule.C00080), THF-polyglutamate (molecule.C03541), UDP-L-Ara4FN (molecule.C16154).

## Enriched Pathways

- `ecocyc.PWY0-1338` polymyxin resistance (EcoCyc)

## Annotation

UDP-4-AMINO-4-DEOXY-L-ARABINOSE + FORMYL-THF-GLU-N -> UDP-L-ARA4-FORMYL-N + THF-GLU-N + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1338` polymyxin resistance (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7718|complex.ecocyc.CPLX0-7718]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03541|molecule.C03541]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C16154|molecule.C16154]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C16153|molecule.C16153]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.FORMYL-THF-GLU-N|molecule.ecocyc.FORMYL-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1862`

## Notes

UDP-4-AMINO-4-DEOXY-L-ARABINOSE + FORMYL-THF-GLU-N -> UDP-L-ARA4-FORMYL-N + THF-GLU-N + PROTON; direction=LEFT-TO-RIGHT
