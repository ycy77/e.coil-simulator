---
entity_id: "reaction.ecocyc.RXN0-5422"
entity_type: "reaction"
name: "tRNA-queuosine glutamyltransferase"
source_database: "EcoCyc"
source_id: "RXN0-5422"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# tRNA-queuosine glutamyltransferase

`reaction.ecocyc.RXN0-5422`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5422`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Queuosine34-in-tRNA-Asp + ATP + GLT -> tRNAs-with-glutamylated-queuosine + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Queuosine34-in-tRNA-Asp + ATP + GLT -> tRNAs-with-glutamylated-queuosine + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by gluQ (protein.P27305). Substrates: ATP (molecule.C00002), L-Glutamate (molecule.C00025), queuosine34 in tRNAAsp (molecule.ecocyc.Queuosine34-in-tRNA-Asp). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), glutamyl-queuosine34 in tRNAAsp (molecule.ecocyc.tRNAs-with-glutamylated-queuosine).

## Annotation

Queuosine34-in-tRNA-Asp + ATP + GLT -> tRNAs-with-glutamylated-queuosine + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P27305|protein.P27305]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.tRNAs-with-glutamylated-queuosine|molecule.ecocyc.tRNAs-with-glutamylated-queuosine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Queuosine34-in-tRNA-Asp|molecule.ecocyc.Queuosine34-in-tRNA-Asp]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5422`

## Notes

Queuosine34-in-tRNA-Asp + ATP + GLT -> tRNAs-with-glutamylated-queuosine + AMP + PPI + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
