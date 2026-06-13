---
entity_id: "reaction.ecocyc.RXN0-7115"
entity_type: "reaction"
name: "RXN0-7115"
source_database: "EcoCyc"
source_id: "RXN0-7115"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7115

`reaction.ecocyc.RXN0-7115`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7115`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N6-L-threonylcarbamoyladenine37-tRNAs + ATP -> Cyclic-N6-threonylcarbamoyl-A37-tRNAs + ADP + Pi; direction=LEFT-TO-RIGHT EcoCyc reaction equation: N6-L-threonylcarbamoyladenine37-tRNAs + ATP -> Cyclic-N6-threonylcarbamoyl-A37-tRNAs + ADP + Pi; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tRNA threonylcarbamoyladenosine dehydratase (complex.ecocyc.CPLX0-8176). Substrates: ATP (molecule.C00002), an N6-L-threonylcarbamoyladenine37 in tRNA (molecule.ecocyc.N6-L-threonylcarbamoyladenine37-tRNAs). Products: ADP (molecule.C00008), a cyclic N6-L-threonylcarbamoyladenosine 37 in tRNA (molecule.ecocyc.Cyclic-N6-threonylcarbamoyl-A37-tRNAs), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY0-1587` N6-L-threonylcarbamoyladenosine37-modified tRNA biosynthesis (EcoCyc)

## Annotation

N6-L-threonylcarbamoyladenine37-tRNAs + ATP -> Cyclic-N6-threonylcarbamoyl-A37-tRNAs + ADP + Pi; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1587` N6-L-threonylcarbamoyladenosine37-modified tRNA biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8176|complex.ecocyc.CPLX0-8176]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Cyclic-N6-threonylcarbamoyl-A37-tRNAs|molecule.ecocyc.Cyclic-N6-threonylcarbamoyl-A37-tRNAs]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.N6-L-threonylcarbamoyladenine37-tRNAs|molecule.ecocyc.N6-L-threonylcarbamoyladenine37-tRNAs]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7115`

## Notes

N6-L-threonylcarbamoyladenine37-tRNAs + ATP -> Cyclic-N6-threonylcarbamoyl-A37-tRNAs + ADP + Pi; direction=LEFT-TO-RIGHT
