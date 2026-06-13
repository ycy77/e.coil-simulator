---
entity_id: "protein.P0A754"
entity_type: "protein"
name: "kefF"
source_database: "UniProt"
source_id: "P0A754"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01414}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01414}; Cytoplasmic side {ECO:0000255|HAMAP-Rule:MF_01414}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kefF yabF b0046 JW0045"
---

# kefF

`protein.P0A754`

## Static

- Type: `protein`
- Source: `UniProt:P0A754`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01414}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01414}; Cytoplasmic side {ECO:0000255|HAMAP-Rule:MF_01414}.

## Enriched Summary

FUNCTION: Regulatory subunit of a potassium efflux system that confers protection against electrophiles. Required for full activity of KefC. Shows redox enzymatic activity, but this enzymatic activity is not required for activation of KefC. Can use a wide range of substrates, including electrophilic quinones, and its function could be to reduce the redox toxicity of electrophilic quinones in parallel with acting as triggers for the KefC efflux system. {ECO:0000255|HAMAP-Rule:MF_01414, ECO:0000269|PubMed:11053405, ECO:0000269|PubMed:19523906, ECO:0000269|PubMed:21742892}.

## Biological Role

Component of regulator of KefC-mediated potassium transport and quinone oxidoreductase (complex.ecocyc.CPLX0-7939).

## Annotation

FUNCTION: Regulatory subunit of a potassium efflux system that confers protection against electrophiles. Required for full activity of KefC. Shows redox enzymatic activity, but this enzymatic activity is not required for activation of KefC. Can use a wide range of substrates, including electrophilic quinones, and its function could be to reduce the redox toxicity of electrophilic quinones in parallel with acting as triggers for the KefC efflux system. {ECO:0000255|HAMAP-Rule:MF_01414, ECO:0000269|PubMed:11053405, ECO:0000269|PubMed:19523906, ECO:0000269|PubMed:21742892}.

## Outgoing Edges (2)

- `activates` --> [[reaction.ecocyc.TRANS-RXN-42|reaction.ecocyc.TRANS-RXN-42]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_component_of` --> [[complex.ecocyc.CPLX0-7939|complex.ecocyc.CPLX0-7939]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0046|gene.b0046]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A754`
- `KEGG:ecj:JW0045;eco:b0046;ecoc:C3026_00240;`
- `GeneID:89519427;944767;`
- `GO:GO:0003955; GO:0005886; GO:0006813; GO:0008753; GO:0009055; GO:0010181; GO:0042803; GO:0050136; GO:0051453; GO:0051454; GO:1901381; GO:1903103`
- `EC:1.6.5.2`

## Notes

Glutathione-regulated potassium-efflux system ancillary protein KefF (Quinone oxidoreductase KefF) (EC 1.6.5.2)
