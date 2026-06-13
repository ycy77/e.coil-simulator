---
entity_id: "reaction.ecocyc.DETHIOBIOTIN-SYN-RXN"
entity_type: "reaction"
name: "DETHIOBIOTIN-SYN-RXN"
source_database: "EcoCyc"
source_id: "DETHIOBIOTIN-SYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "DTB SYNTHETASE"
---

# DETHIOBIOTIN-SYN-RXN

`reaction.ecocyc.DETHIOBIOTIN-SYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DETHIOBIOTIN-SYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The third step in the biosynthesis of biotin. EcoCyc reaction equation: CARBON-DIOXIDE + DIAMINONONANOATE + ATP -> PROTON + DETHIOBIOTIN + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. The third step in the biosynthesis of biotin.

## Biological Role

Catalyzed by dethiobiotin synthetase BidA (complex.ecocyc.CPLX0-8613), dethiobiotin synthetase (complex.ecocyc.DETHIOBIOTIN-SYN-CPLX). Substrates: ATP (molecule.C00002), CO2 (molecule.C00011), 7,8-Diaminononanoate (molecule.C01037). Products: ADP (molecule.C00008), H+ (molecule.C00080), Dethiobiotin (molecule.C01909), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY0-1507` biotin biosynthesis from 8-amino-7-oxononanoate I (EcoCyc)

## Annotation

The third step in the biosynthesis of biotin.

## Pathways

- `ecocyc.PWY0-1507` biotin biosynthesis from 8-amino-7-oxononanoate I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8613|complex.ecocyc.CPLX0-8613]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.DETHIOBIOTIN-SYN-CPLX|complex.ecocyc.DETHIOBIOTIN-SYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01909|molecule.C01909]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01037|molecule.C01037]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DETHIOBIOTIN-SYN-RXN`

## Notes

CARBON-DIOXIDE + DIAMINONONANOATE + ATP -> PROTON + DETHIOBIOTIN + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
