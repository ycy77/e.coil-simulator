---
entity_id: "reaction.ecocyc.NARQ-RXN"
entity_type: "reaction"
name: "NARQ-RXN"
source_database: "EcoCyc"
source_id: "NARQ-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# NARQ-RXN

`reaction.ecocyc.NARQ-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NARQ-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this reaction the nitrate/nitrite sensor kinase-phosphotransferase NarQ autophosphorylates. Nitrate/nitrite sensor kinase-phosphotransferase NarQ is one of two sensor proteins regulating anaerobic respiratory gene expression in E. coli. The second sensor protein is the narX gene product. Both proteins act independently of each other. The sensors communicate nitrate and nitrite availability to the response regulators, the gene products of narL and narP. In the presence of both nitrate and nitrite, sensor NarQ acts as a positive regulator of both NarL and NarP activity. EcoCyc reaction equation: ATP + NARQ-CPLX -> ADP + PHOSPHO-NARQ; direction=LEFT-TO-RIGHT. In this reaction the nitrate/nitrite sensor kinase-phosphotransferase NarQ autophosphorylates. Nitrate/nitrite sensor kinase-phosphotransferase NarQ is one of two sensor proteins regulating anaerobic respiratory gene expression in E. coli. The second sensor protein is the narX gene product. Both proteins act independently of each other. The sensors communicate nitrate and nitrite availability to the response regulators, the gene products of narL and narP. In the presence of both nitrate and nitrite, sensor NarQ acts as a positive regulator of both NarL and NarP activity.

## Biological Role

Substrates: ATP (molecule.C00002). Products: ADP (molecule.C00008).

## Enriched Pathways

- `ecocyc.PWY0-1514` NarQ Two-Component Signal Transduction System, nitrate dependent (EcoCyc)

## Annotation

In this reaction the nitrate/nitrite sensor kinase-phosphotransferase NarQ autophosphorylates. Nitrate/nitrite sensor kinase-phosphotransferase NarQ is one of two sensor proteins regulating anaerobic respiratory gene expression in E. coli. The second sensor protein is the narX gene product. Both proteins act independently of each other. The sensors communicate nitrate and nitrite availability to the response regulators, the gene products of narL and narP. In the presence of both nitrate and nitrite, sensor NarQ acts as a positive regulator of both NarL and NarP activity.

## Pathways

- `ecocyc.PWY0-1514` NarQ Two-Component Signal Transduction System, nitrate dependent (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:NARQ-RXN`

## Notes

ATP + NARQ-CPLX -> ADP + PHOSPHO-NARQ; direction=LEFT-TO-RIGHT
