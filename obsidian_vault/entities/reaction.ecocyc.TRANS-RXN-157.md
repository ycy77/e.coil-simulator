---
entity_id: "reaction.ecocyc.TRANS-RXN-157"
entity_type: "reaction"
name: "transport of β-D-glucose by PTS"
source_database: "EcoCyc"
source_id: "TRANS-RXN-157"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# transport of β-D-glucose by PTS

`reaction.ecocyc.TRANS-RXN-157`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-157`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Hpr-pi-phospho-L-histidines + Glucopyranose -> D-glucopyranose-6-phosphate + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Hpr-pi-phospho-L-histidines + Glucopyranose -> D-glucopyranose-6-phosphate + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by β-glucoside specific PTS enzyme II / BglG kinase / BglG phosphatase (complex.ecocyc.CPLX-154), glucose-specific PTS enzyme II (complex.ecocyc.CPLX-157), mannose-specific PTS enzyme II (complex.ecocyc.CPLX-165). Substrates: D-Glucose (molecule.C00031), an [HPr protein]-Nπ-phospho-L-histidine (molecule.ecocyc.Hpr-pi-phospho-L-histidines). Products: D-Glucose 6-phosphate (molecule.C00092), an [HPr]-L-histidine (molecule.ecocyc.Hpr-Histidine).

## Enriched Pathways

- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)

## Annotation

Hpr-pi-phospho-L-histidines + Glucopyranose -> D-glucopyranose-6-phosphate + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX-154|complex.ecocyc.CPLX-154]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX-157|complex.ecocyc.CPLX-157]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX-165|complex.ecocyc.CPLX-165]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00092|molecule.C00092]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Hpr-Histidine|molecule.ecocyc.Hpr-Histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hpr-pi-phospho-L-histidines|molecule.ecocyc.Hpr-pi-phospho-L-histidines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-157`

## Notes

Hpr-pi-phospho-L-histidines + Glucopyranose -> D-glucopyranose-6-phosphate + Hpr-Histidine; direction=PHYSIOL-LEFT-TO-RIGHT
