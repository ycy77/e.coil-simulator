---
entity_id: "reaction.ecocyc.NANE-RXN"
entity_type: "reaction"
name: "N-acetyl-D-mannosamine-6-phosphate epimerase"
source_database: "EcoCyc"
source_id: "NANE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# N-acetyl-D-mannosamine-6-phosphate epimerase

`reaction.ecocyc.NANE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NANE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N-ACETYL-D-MANNOSAMINE-6P -> N-ACETYL-D-GLUCOSAMINE-6-P; direction=REVERSIBLE EcoCyc reaction equation: N-ACETYL-D-MANNOSAMINE-6P -> N-ACETYL-D-GLUCOSAMINE-6-P; direction=REVERSIBLE.

## Biological Role

Catalyzed by nanE (protein.P0A761). Substrates: N-Acetyl-D-mannosamine 6-phosphate (molecule.C04257). Products: N-Acetyl-D-glucosamine 6-phosphate (molecule.C00357).

## Enriched Pathways

- `ecocyc.PWY0-1324` N-acetylneuraminate and N-acetylmannosamine degradation I (EcoCyc)

## Annotation

N-ACETYL-D-MANNOSAMINE-6P -> N-ACETYL-D-GLUCOSAMINE-6-P; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1324` N-acetylneuraminate and N-acetylmannosamine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A761|protein.P0A761]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00357|molecule.C00357]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04257|molecule.C04257]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:NANE-RXN`

## Notes

N-ACETYL-D-MANNOSAMINE-6P -> N-ACETYL-D-GLUCOSAMINE-6-P; direction=REVERSIBLE
