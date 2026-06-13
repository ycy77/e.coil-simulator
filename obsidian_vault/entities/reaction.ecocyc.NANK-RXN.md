---
entity_id: "reaction.ecocyc.NANK-RXN"
entity_type: "reaction"
name: "NANK-RXN"
source_database: "EcoCyc"
source_id: "NANK-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# NANK-RXN

`reaction.ecocyc.NANK-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NANK-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N-acetyl-D-mannosamine + ATP -> PROTON + N-ACETYL-D-MANNOSAMINE-6P + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: N-acetyl-D-mannosamine + ATP -> PROTON + N-ACETYL-D-MANNOSAMINE-6P + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by N-acetylmannosamine kinase (complex.ecocyc.CPLX0-8588). Substrates: ATP (molecule.C00002), N-Acetyl-D-mannosamine (molecule.C00645). Products: ADP (molecule.C00008), H+ (molecule.C00080), N-Acetyl-D-mannosamine 6-phosphate (molecule.C04257).

## Enriched Pathways

- `ecocyc.PWY0-1324` N-acetylneuraminate and N-acetylmannosamine degradation I (EcoCyc)

## Annotation

N-acetyl-D-mannosamine + ATP -> PROTON + N-ACETYL-D-MANNOSAMINE-6P + ADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1324` N-acetylneuraminate and N-acetylmannosamine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8588|complex.ecocyc.CPLX0-8588]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04257|molecule.C04257]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00645|molecule.C00645]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:NANK-RXN`

## Notes

N-acetyl-D-mannosamine + ATP -> PROTON + N-ACETYL-D-MANNOSAMINE-6P + ADP; direction=LEFT-TO-RIGHT
