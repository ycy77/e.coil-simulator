---
entity_id: "reaction.ecocyc.ASPAMINOTRANS-RXN"
entity_type: "reaction"
name: "ASPAMINOTRANS-RXN"
source_database: "EcoCyc"
source_id: "ASPAMINOTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ASPAMINOTRANS-RXN

`reaction.ecocyc.ASPAMINOTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ASPAMINOTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The reversible reaction interconverts amino acids and their keto-derivatives. The major biosynthetic pathway to aspartate is through transamination between oxalacetate and glutamate. EcoCyc reaction equation: L-ASPARTATE + 2-KETOGLUTARATE -> OXALACETIC_ACID + GLT; direction=REVERSIBLE. The reversible reaction interconverts amino acids and their keto-derivatives. The major biosynthetic pathway to aspartate is through transamination between oxalacetate and glutamate.

## Biological Role

Catalyzed by aspartate aminotransferase (complex.ecocyc.ASPAMINOTRANS-DIMER). Substrates: 2-Oxoglutarate (molecule.C00026), L-Aspartate (molecule.C00049). Products: L-Glutamate (molecule.C00025), Oxaloacetate (molecule.C00036).

## Enriched Pathways

- `ecocyc.ASPARTATESYN-PWY` L-aspartate biosynthesis (EcoCyc)
- `ecocyc.GLUTDEG-PWY` L-glutamate degradation II (EcoCyc)

## Annotation

The reversible reaction interconverts amino acids and their keto-derivatives. The major biosynthetic pathway to aspartate is through transamination between oxalacetate and glutamate.

## Pathways

- `ecocyc.ASPARTATESYN-PWY` L-aspartate biosynthesis (EcoCyc)
- `ecocyc.GLUTDEG-PWY` L-glutamate degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ASPAMINOTRANS-DIMER|complex.ecocyc.ASPAMINOTRANS-DIMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01384|molecule.C01384]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-12132|molecule.ecocyc.CPD-12132]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1614|molecule.ecocyc.CPD0-1614]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ASPAMINOTRANS-RXN`

## Notes

L-ASPARTATE + 2-KETOGLUTARATE -> OXALACETIC_ACID + GLT; direction=REVERSIBLE
