---
entity_id: "protein.P0A9Z1"
entity_type: "protein"
name: "glnB"
source_database: "UniProt"
source_id: "P0A9Z1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glnB b2553 JW2537"
---

# glnB

`protein.P0A9Z1`

## Static

- Type: `protein`
- Source: `UniProt:P0A9Z1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: P-II indirectly controls the transcription of the glutamine synthetase gene (glnA). P-II prevents NR-II-catalyzed conversion of NR-I to NR-I-phosphate, the transcriptional activator of GlnA. When P-II is uridylylated to P-II-UMP, these events are reversed. When the ratio of Gln to 2-ketoglutarate decreases, P-II is uridylylated to P-II-UMP, which causes the deadenylation of glutamine synthetase by GlnE, so activating the enzyme.

## Biological Role

Component of uridylyl-[protein PII-1] (complex.ecocyc.CPLX0-8568), nitrogen regulatory protein PII-1 (complex.ecocyc.PIIPROTEIN-CPLX).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: P-II indirectly controls the transcription of the glutamine synthetase gene (glnA). P-II prevents NR-II-catalyzed conversion of NR-I to NR-I-phosphate, the transcriptional activator of GlnA. When P-II is uridylylated to P-II-UMP, these events are reversed. When the ratio of Gln to 2-ketoglutarate decreases, P-II is uridylylated to P-II-UMP, which causes the deadenylation of glutamine synthetase by GlnE, so activating the enzyme.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (4)

- `activates` --> [[reaction.ecocyc.GLUCOSAMINE-6-P-DEAMIN-RXN|reaction.ecocyc.GLUCOSAMINE-6-P-DEAMIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.GSADENYLATION-RXN|reaction.ecocyc.GSADENYLATION-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_component_of` --> [[complex.ecocyc.CPLX0-8568|complex.ecocyc.CPLX0-8568]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.PIIPROTEIN-CPLX|complex.ecocyc.PIIPROTEIN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b2553|gene.b2553]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9Z1`
- `KEGG:ecj:JW2537;eco:b2553;ecoc:C3026_14135;`
- `GeneID:86860673;93774582;947016;`
- `GO:GO:0005524; GO:0005829; GO:0006808; GO:0008047; GO:0030234; GO:0036094; GO:0042304; GO:0042802`

## Notes

Nitrogen regulatory protein P-II 1
