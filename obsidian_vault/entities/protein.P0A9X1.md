---
entity_id: "protein.P0A9X1"
entity_type: "protein"
name: "znuC"
source_database: "UniProt"
source_id: "P0A9X1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01725}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01725}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "znuC yebM b1858 JW1847"
---

# znuC

`protein.P0A9X1`

## Static

- Type: `protein`
- Source: `UniProt:P0A9X1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01725}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01725}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex ZnuABC involved in zinc import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01725, ECO:0000269|PubMed:9680209}. znuC encodes the predicted ATP-binding subunit of a high-affinity zinc uptake system ; ZnuC contains sequence motifs conserved in ATP-binding cassette proteins . znuC belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 . znu: Zn2+ uptake

## Biological Role

Component of Zn2+ ABC transporter (complex.ecocyc.ABC-63-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex ZnuABC involved in zinc import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01725, ECO:0000269|PubMed:9680209}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-63-CPLX|complex.ecocyc.ABC-63-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1858|gene.b1858]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9X1`
- `KEGG:ecj:JW1847;eco:b1858;ecoc:C3026_10585;`
- `GeneID:93776132;946374;`
- `GO:GO:0005524; GO:0010043; GO:0015633; GO:0016020; GO:0016887; GO:0042626; GO:0043190; GO:0055052; GO:0071578`
- `EC:7.2.2.20`

## Notes

Zinc import ATP-binding protein ZnuC (EC 7.2.2.20)
