---
entity_id: "reaction.ecocyc.PSERTRANSAM-RXN"
entity_type: "reaction"
name: "PSERTRANSAM-RXN"
source_database: "EcoCyc"
source_id: "PSERTRANSAM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PSERTRANSAM-RXN

`reaction.ecocyc.PSERTRANSAM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PSERTRANSAM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The second step in serine biosynthesis. EcoCyc reaction equation: 3-P-SERINE + 2-KETOGLUTARATE -> 3-P-HYDROXYPYRUVATE + GLT; direction=REVERSIBLE. The second step in serine biosynthesis.

## Biological Role

Catalyzed by phosphoserine/phosphohydroxythreonine aminotransferase (complex.ecocyc.PSERTRANSAM-CPLX). Substrates: 2-Oxoglutarate (molecule.C00026), O-Phospho-L-serine (molecule.C01005). Products: L-Glutamate (molecule.C00025), 3-Phosphonooxypyruvate (molecule.C03232).

## Enriched Pathways

- `ecocyc.SERSYN-PWY-1` L-serine biosynthesis (EcoCyc)

## Annotation

The second step in serine biosynthesis.

## Pathways

- `ecocyc.SERSYN-PWY-1` L-serine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.PSERTRANSAM-CPLX|complex.ecocyc.PSERTRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03232|molecule.C03232]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01005|molecule.C01005]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PSERTRANSAM-RXN`

## Notes

3-P-SERINE + 2-KETOGLUTARATE -> 3-P-HYDROXYPYRUVATE + GLT; direction=REVERSIBLE
