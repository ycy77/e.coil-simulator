---
entity_id: "reaction.ecocyc.RXN-14570"
entity_type: "reaction"
name: "RXN-14570"
source_database: "EcoCyc"
source_id: "RXN-14570"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14570

`reaction.ecocyc.RXN-14570`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14570`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15435 + tRNA-adenine-37 -> N6-L-threonylcarbamoyladenine37-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-15435 + tRNA-adenine-37 -> N6-L-threonylcarbamoyladenine37-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by N6-L-threonylcarbamoyladenine synthase (complex.ecocyc.CPLX0-8182). Substrates: (L-threonylcarbamoyl)adenylate (molecule.ecocyc.CPD-15435), an adenine37 in tRNA (molecule.ecocyc.tRNA-adenine-37). Products: AMP (molecule.C00020), H+ (molecule.C00080), an N6-L-threonylcarbamoyladenine37 in tRNA (molecule.ecocyc.N6-L-threonylcarbamoyladenine37-tRNAs).

## Enriched Pathways

- `ecocyc.PWY0-1587` N6-L-threonylcarbamoyladenosine37-modified tRNA biosynthesis (EcoCyc)

## Annotation

CPD-15435 + tRNA-adenine-37 -> N6-L-threonylcarbamoyladenine37-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1587` N6-L-threonylcarbamoyladenosine37-modified tRNA biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8182|complex.ecocyc.CPLX0-8182]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.N6-L-threonylcarbamoyladenine37-tRNAs|molecule.ecocyc.N6-L-threonylcarbamoyladenine37-tRNAs]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15435|molecule.ecocyc.CPD-15435]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-adenine-37|molecule.ecocyc.tRNA-adenine-37]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14570`

## Notes

CPD-15435 + tRNA-adenine-37 -> N6-L-threonylcarbamoyladenine37-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
