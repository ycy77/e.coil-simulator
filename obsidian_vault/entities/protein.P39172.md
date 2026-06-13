---
entity_id: "protein.P39172"
entity_type: "protein"
name: "znuA"
source_database: "UniProt"
source_id: "P39172"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000250|UniProtKB:A1B9L0}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "znuA yebL yzzP b1857 JW5831"
---

# znuA

`protein.P39172`

## Static

- Type: `protein`
- Source: `UniProt:P39172`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000250|UniProtKB:A1B9L0}.

## Enriched Summary

FUNCTION: Part of the ATP-binding cassette (ABC) transport system ZnuABC involved in zinc import (PubMed:9680209). Binds zinc with high affinity and specificity and delivers it to the membrane permease for translocation into the cytoplasm (PubMed:18027003). {ECO:0000269|PubMed:18027003, ECO:0000269|PubMed:9680209}. ZnuA is the periplasmic binding protein of an ATP-dependent Zn2+ uptake system. High resolution crystal structures of ZnuA with bound Zn2+ consist of two structually similar domains (the N and C domains) connected by a long α-helix; a single Zn2+ binds at the interface between the two domains . Purified ZnuA interacts with Co2+, Ni2+, Cd 2+, Cu2+ and Cu+; purified ZnuA binds Zn2+ with high affinity (Kd znuA belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 . znu: Zn2+ uptake

## Biological Role

Component of Zn2+ ABC transporter (complex.ecocyc.ABC-63-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ATP-binding cassette (ABC) transport system ZnuABC involved in zinc import (PubMed:9680209). Binds zinc with high affinity and specificity and delivers it to the membrane permease for translocation into the cytoplasm (PubMed:18027003). {ECO:0000269|PubMed:18027003, ECO:0000269|PubMed:9680209}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-63-CPLX|complex.ecocyc.ABC-63-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1857|gene.b1857]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39172`
- `KEGG:ecj:JW5831;eco:b1857;ecoc:C3026_10580;`
- `GeneID:93776131;946375;`
- `GO:GO:0006829; GO:0007155; GO:0008270; GO:0016020; GO:0042597; GO:0055052; GO:0071578`

## Notes

High-affinity zinc uptake system protein ZnuA
