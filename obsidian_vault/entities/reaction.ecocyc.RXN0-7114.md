---
entity_id: "reaction.ecocyc.RXN0-7114"
entity_type: "reaction"
name: "RXN0-7114"
source_database: "EcoCyc"
source_id: "RXN0-7114"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7114

`reaction.ecocyc.RXN0-7114`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7114`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + N6-L-threonylcarbamoyladenine37-tRNAs -> N6-met-threonylcarbamoyl-A37-tRNAs + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + N6-L-threonylcarbamoyladenine37-tRNAs -> N6-met-threonylcarbamoyl-A37-tRNAs + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by trmO (protein.P28634). Substrates: S-Adenosyl-L-methionine (molecule.C00019), an N6-L-threonylcarbamoyladenine37 in tRNA (molecule.ecocyc.N6-L-threonylcarbamoyladenine37-tRNAs). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), an N6-methyl-threonylcarbamoyladenosine 37 in tRNA (molecule.ecocyc.N6-met-threonylcarbamoyl-A37-tRNAs).

## Annotation

S-ADENOSYLMETHIONINE + N6-L-threonylcarbamoyladenine37-tRNAs -> N6-met-threonylcarbamoyl-A37-tRNAs + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P28634|protein.P28634]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.N6-met-threonylcarbamoyl-A37-tRNAs|molecule.ecocyc.N6-met-threonylcarbamoyl-A37-tRNAs]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.N6-L-threonylcarbamoyladenine37-tRNAs|molecule.ecocyc.N6-L-threonylcarbamoyladenine37-tRNAs]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7114`

## Notes

S-ADENOSYLMETHIONINE + N6-L-threonylcarbamoyladenine37-tRNAs -> N6-met-threonylcarbamoyl-A37-tRNAs + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
