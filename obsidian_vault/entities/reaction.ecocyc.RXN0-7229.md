---
entity_id: "reaction.ecocyc.RXN0-7229"
entity_type: "reaction"
name: "RXN0-7229"
source_database: "EcoCyc"
source_id: "RXN0-7229"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7229

`reaction.ecocyc.RXN0-7229`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7229`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

This reaction is part of the metabolism of glycolate. EcoCyc reaction equation: ETR-Quinones + GLYCOLLATE -> ETR-Quinols + GLYOX; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of the metabolism of glycolate.

## Biological Role

Catalyzed by glycolate dehydrogenase (complex.ecocyc.CPLX0-7458). Substrates: Glycolate (molecule.C00160). Products: Glyoxylate (molecule.C00048).

## Enriched Pathways

- `ecocyc.GLYCOLATEMET-PWY` glycolate and glyoxylate degradation I (EcoCyc)
- `ecocyc.GLYOXDEG-PWY` glycolate and glyoxylate degradation II (EcoCyc)

## Annotation

This reaction is part of the metabolism of glycolate.

## Pathways

- `ecocyc.GLYCOLATEMET-PWY` glycolate and glyoxylate degradation I (EcoCyc)
- `ecocyc.GLYOXDEG-PWY` glycolate and glyoxylate degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7458|complex.ecocyc.CPLX0-7458]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00160|molecule.C00160]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7229`

## Notes

ETR-Quinones + GLYCOLLATE -> ETR-Quinols + GLYOX; direction=PHYSIOL-LEFT-TO-RIGHT
