---
entity_id: "reaction.ecocyc.SPERMIDINESYN-RXN"
entity_type: "reaction"
name: "SPERMIDINESYN-RXN"
source_database: "EcoCyc"
source_id: "SPERMIDINESYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SPERMIDINESYN-RXN

`reaction.ecocyc.SPERMIDINESYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SPERMIDINESYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fifth and last step in the biosynthesis of spermidine from arginine. It transfers propylamine moiety from S-adenosylmethioninamine to putrescine to form spermidine. EcoCyc reaction equation: PUTRESCINE + S-ADENOSYLMETHIONINAMINE -> PROTON + SPERMIDINE + 5-METHYLTHIOADENOSINE; direction=LEFT-TO-RIGHT. This is the fifth and last step in the biosynthesis of spermidine from arginine. It transfers propylamine moiety from S-adenosylmethioninamine to putrescine to form spermidine.

## Biological Role

Catalyzed by spermidine synthase (complex.ecocyc.SPERMIDINESYN-CPLX). Substrates: Putrescine (molecule.C00134), S-Adenosylmethioninamine (molecule.C01137). Products: H+ (molecule.C00080), 5'-Methylthioadenosine (molecule.C00170), Spermidine (molecule.C00315).

## Enriched Pathways

- `ecocyc.BSUBPOLYAMSYN-PWY` spermidine biosynthesis I (EcoCyc)

## Annotation

This is the fifth and last step in the biosynthesis of spermidine from arginine. It transfers propylamine moiety from S-adenosylmethioninamine to putrescine to form spermidine.

## Pathways

- `ecocyc.BSUBPOLYAMSYN-PWY` spermidine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.SPERMIDINESYN-CPLX|complex.ecocyc.SPERMIDINESYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00170|molecule.C00170]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01137|molecule.C01137]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1375|molecule.ecocyc.CPD0-1375]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1376|molecule.ecocyc.CPD0-1376]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:SPERMIDINESYN-RXN`

## Notes

PUTRESCINE + S-ADENOSYLMETHIONINAMINE -> PROTON + SPERMIDINE + 5-METHYLTHIOADENOSINE; direction=LEFT-TO-RIGHT
