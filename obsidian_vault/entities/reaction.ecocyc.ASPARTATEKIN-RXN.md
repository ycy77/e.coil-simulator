---
entity_id: "reaction.ecocyc.ASPARTATEKIN-RXN"
entity_type: "reaction"
name: "ASPARTATEKIN-RXN"
source_database: "EcoCyc"
source_id: "ASPARTATEKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ASPARTATEKIN-RXN

`reaction.ecocyc.ASPARTATEKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ASPARTATEKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-ASPARTATE + ATP -> L-BETA-ASPARTYL-P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-ASPARTATE + ATP -> L-BETA-ASPARTYL-P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fused aspartate kinase/homoserine dehydrogenase 1 (complex.ecocyc.ASPKINIHOMOSERDEHYDROGI-CPLX), fused aspartate kinase/homoserine dehydrogenase 2 (complex.ecocyc.ASPKINIIHOMOSERDEHYDROGII-CPLX), aspartate kinase III (complex.ecocyc.ASPKINIII-CPLX). Substrates: ATP (molecule.C00002), L-Aspartate (molecule.C00049). Products: ADP (molecule.C00008), 4-Phospho-L-aspartate (molecule.C03082).

## Enriched Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)
- `ecocyc.HOMOSERSYN-PWY` L-homoserine biosynthesis (EcoCyc)

## Annotation

L-ASPARTATE + ATP -> L-BETA-ASPARTYL-P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)
- `ecocyc.HOMOSERSYN-PWY` L-homoserine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `activates` <-- [[molecule.C00263|molecule.C00263]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.ASPKINIHOMOSERDEHYDROGI-CPLX|complex.ecocyc.ASPKINIHOMOSERDEHYDROGI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ASPKINIIHOMOSERDEHYDROGII-CPLX|complex.ecocyc.ASPKINIIHOMOSERDEHYDROGII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ASPKINIII-CPLX|complex.ecocyc.ASPKINIII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03082|molecule.C03082]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.S-2-AMINOETHYL-L-CYSTEINE|molecule.ecocyc.S-2-AMINOETHYL-L-CYSTEINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ASPARTATEKIN-RXN`

## Notes

L-ASPARTATE + ATP -> L-BETA-ASPARTYL-P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
