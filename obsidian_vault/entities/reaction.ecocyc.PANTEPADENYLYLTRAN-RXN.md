---
entity_id: "reaction.ecocyc.PANTEPADENYLYLTRAN-RXN"
entity_type: "reaction"
name: "PANTEPADENYLYLTRAN-RXN"
source_database: "EcoCyc"
source_id: "PANTEPADENYLYLTRAN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PANTEPADENYLYLTRAN-RXN

`reaction.ecocyc.PANTEPADENYLYLTRAN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PANTEPADENYLYLTRAN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fourth reaction in coenzyme A (CoA) biosynthesis. EcoCyc reaction equation: PROTON + PANTETHEINE-P + ATP -> DEPHOSPHO-COA + PPI; direction=LEFT-TO-RIGHT. This is the fourth reaction in coenzyme A (CoA) biosynthesis.

## Biological Role

Catalyzed by pantetheine-phosphate adenylyltransferase (complex.ecocyc.COADTRI-CPLX). Substrates: ATP (molecule.C00002), H+ (molecule.C00080), Pantetheine 4'-phosphate (molecule.C01134). Products: Diphosphate (molecule.C00013), Dephospho-CoA (molecule.C00882).

## Enriched Pathways

- `ecocyc.COA-PWY` coenzyme A biosynthesis I (bacteria) (EcoCyc)

## Annotation

This is the fourth reaction in coenzyme A (CoA) biosynthesis.

## Pathways

- `ecocyc.COA-PWY` coenzyme A biosynthesis I (bacteria) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.COADTRI-CPLX|complex.ecocyc.COADTRI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00882|molecule.C00882]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01134|molecule.C01134]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PANTEPADENYLYLTRAN-RXN`

## Notes

PROTON + PANTETHEINE-P + ATP -> DEPHOSPHO-COA + PPI; direction=LEFT-TO-RIGHT
