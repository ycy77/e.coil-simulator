---
entity_id: "protein.P0ABE2"
entity_type: "protein"
name: "bolA"
source_database: "UniProt"
source_id: "P0ABE2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bolA b0435 JW5060"
---

# bolA

`protein.P0ABE2`

## Static

- Type: `protein`
- Source: `UniProt:P0ABE2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional regulator that plays an important role in general stress response. Has many effects on cell morphology, cell growth and cell division. Acts by regulating the transcription of many genes, including dacA (PBP-5), dacC (PBP-6), ampC and mreB. Probably involved in the coordination of genes that adapt the cell physiology in order to enhance cell adaptation and survival under stress conditions. Essential for normal cell morphology in stationary phase and under conditions of starvation (PubMed:10361282, PubMed:12354237, PubMed:19111750, PubMed:21464593, PubMed:25691594). Also regulates a complex network of genes encoding proteins related to biofilm development, and negatively modulates flagellar biosynthesis and swimming capacity. Could be a motile/adhesive transcriptional switch, specifically involved in the transition between the planktonic and the attachment stage of biofilm formation (PubMed:25691594). Overexpression produces round cell shape, impairs cell growth rate and induces biofilm development (PubMed:15345459, PubMed:21464593, PubMed:305364). {ECO:0000269|PubMed:10361282, ECO:0000269|PubMed:12354237, ECO:0000269|PubMed:15345459, ECO:0000269|PubMed:19111750, ECO:0000269|PubMed:21464593, ECO:0000269|PubMed:25691594, ECO:0000269|PubMed:305364}...

## Biological Role

Component of Grx4-BolA complex (complex.ecocyc.CPLX0-7942).

## Annotation

FUNCTION: Transcriptional regulator that plays an important role in general stress response. Has many effects on cell morphology, cell growth and cell division. Acts by regulating the transcription of many genes, including dacA (PBP-5), dacC (PBP-6), ampC and mreB. Probably involved in the coordination of genes that adapt the cell physiology in order to enhance cell adaptation and survival under stress conditions. Essential for normal cell morphology in stationary phase and under conditions of starvation (PubMed:10361282, PubMed:12354237, PubMed:19111750, PubMed:21464593, PubMed:25691594). Also regulates a complex network of genes encoding proteins related to biofilm development, and negatively modulates flagellar biosynthesis and swimming capacity. Could be a motile/adhesive transcriptional switch, specifically involved in the transition between the planktonic and the attachment stage of biofilm formation (PubMed:25691594). Overexpression produces round cell shape, impairs cell growth rate and induces biofilm development (PubMed:15345459, PubMed:21464593, PubMed:305364). {ECO:0000269|PubMed:10361282, ECO:0000269|PubMed:12354237, ECO:0000269|PubMed:15345459, ECO:0000269|PubMed:19111750, ECO:0000269|PubMed:21464593, ECO:0000269|PubMed:25691594, ECO:0000269|PubMed:305364}.

## Outgoing Edges (5)

- `activates` --> [[gene.b4320|gene.b4320]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `is_component_of` --> [[complex.ecocyc.CPLX0-7942|complex.ecocyc.CPLX0-7942]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `represses` --> [[gene.b3249|gene.b3249]] `RegulonDB` `S` - regulator=BolA; target=mreD; function=-
- `represses` --> [[gene.b3250|gene.b3250]] `RegulonDB` `S` - regulator=BolA; target=mreC; function=-
- `represses` --> [[gene.b3251|gene.b3251]] `RegulonDB` `S` - regulator=BolA; target=mreB; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0435|gene.b0435]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABE2`
- `KEGG:ecj:JW5060;eco:b0435;ecoc:C3026_02125;`
- `GeneID:93777019;947043;`
- `GO:GO:0003677; GO:0005829; GO:0006351; GO:0006879; GO:0016226; GO:0045454; GO:1990229`

## Notes

DNA-binding transcriptional regulator BolA
