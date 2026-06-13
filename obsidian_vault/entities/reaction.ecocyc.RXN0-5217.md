---
entity_id: "reaction.ecocyc.RXN0-5217"
entity_type: "reaction"
name: "RXN0-5217"
source_database: "EcoCyc"
source_id: "RXN0-5217"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5217

`reaction.ecocyc.RXN0-5217`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5217`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CADAVERINE + S-ADENOSYLMETHIONINAMINE -> PROTON + CPD0-1065 + 5-METHYLTHIOADENOSINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CADAVERINE + S-ADENOSYLMETHIONINAMINE -> PROTON + CPD0-1065 + 5-METHYLTHIOADENOSINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by spermidine synthase (complex.ecocyc.SPERMIDINESYN-CPLX). Substrates: S-Adenosylmethioninamine (molecule.C01137), Cadaverine (molecule.C01672). Products: H+ (molecule.C00080), 5'-Methylthioadenosine (molecule.C00170), Aminopropylcadaverine (molecule.C16565).

## Enriched Pathways

- `ecocyc.PWY0-1303` aminopropylcadaverine biosynthesis (EcoCyc)

## Annotation

CADAVERINE + S-ADENOSYLMETHIONINAMINE -> PROTON + CPD0-1065 + 5-METHYLTHIOADENOSINE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1303` aminopropylcadaverine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.SPERMIDINESYN-CPLX|complex.ecocyc.SPERMIDINESYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00170|molecule.C00170]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C16565|molecule.C16565]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01137|molecule.C01137]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01672|molecule.C01672]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5217`

## Notes

CADAVERINE + S-ADENOSYLMETHIONINAMINE -> PROTON + CPD0-1065 + 5-METHYLTHIOADENOSINE; direction=LEFT-TO-RIGHT
