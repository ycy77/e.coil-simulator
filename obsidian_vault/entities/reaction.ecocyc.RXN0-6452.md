---
entity_id: "reaction.ecocyc.RXN0-6452"
entity_type: "reaction"
name: "RXN0-6452"
source_database: "EcoCyc"
source_id: "RXN0-6452"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6452

`reaction.ecocyc.RXN0-6452`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6452`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + CPD0-2339 + WATER -> MALONATE-S-ALD + AMMONIUM; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + CPD0-2339 + WATER -> MALONATE-S-ALD + AMMONIUM; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 3-aminoacrylate deaminase (complex.ecocyc.CPLX0-8589). Substrates: H2O (molecule.C00001), H+ (molecule.C00080), Aminoacrylate (molecule.C20253). Products: 3-Oxopropanoate (molecule.C00222), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY0-1471` uracil degradation III (EcoCyc)

## Annotation

PROTON + CPD0-2339 + WATER -> MALONATE-S-ALD + AMMONIUM; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1471` uracil degradation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8589|complex.ecocyc.CPLX0-8589]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00222|molecule.C00222]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C20253|molecule.C20253]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6452`

## Notes

PROTON + CPD0-2339 + WATER -> MALONATE-S-ALD + AMMONIUM; direction=LEFT-TO-RIGHT
