---
entity_id: "protein.P31554"
entity_type: "protein"
name: "lptD"
source_database: "UniProt"
source_id: "P31554"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_01411, ECO:0000269|PubMed:12207697, ECO:0000269|PubMed:12724388, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:20446753}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lptD imp ostA yabG b0054 JW0053"
---

# lptD

`protein.P31554`

## Static

- Type: `protein`
- Source: `UniProt:P31554`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_01411, ECO:0000269|PubMed:12207697, ECO:0000269|PubMed:12724388, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:20446753}.

## Enriched Summary

FUNCTION: Together with LptE, is involved in the assembly of lipopolysaccharide (LPS) at the surface of the outer membrane. Contributes to n-hexane resistance. {ECO:0000255|HAMAP-Rule:MF_01411, ECO:0000269|PubMed:12207697, ECO:0000269|PubMed:12724388, ECO:0000269|PubMed:16861298, ECO:0000269|PubMed:18424520, ECO:0000269|PubMed:20203010, ECO:0000269|PubMed:21339611, ECO:0000269|PubMed:2547691, ECO:0000269|PubMed:7811102}. The LptD (lipopolysaccharide transport) protein is an essential outer membrane (OM) protein which, in complex with LptE, functions to assemble lipopolysaccharides at the surface of the OM . LptD exhibits β barrel-like characteristics, including a high incidence of aromatic amino acids (13.1%) . Sequence analyses via the algorithm by Shirmer and Cowan and Zhai suggest that LptD is rich in transmembrane β-strands. LptD contains an N-terminal periplasmic domain and a C-terminal β-barrel domain . LptD contains four cysteines which form non-consecutive disulfide bonds (Cys31=Cys724 and Cys173=Cys755) that bridge the N-terminal and C-terminal domains . LptD is fully oxidised in vivo and formation of at least one correct disulfide bond is required for function . Folding of LptD involves DsbA and proceeds via an intermediate stage containing non-native disulfides . LptE is required for maturation to the active protein...

## Biological Role

Component of lipopolysaccharide transport system - outer membrane assembly complex (complex.ecocyc.CPLX0-7628), lipopolysaccharide transport system (complex.ecocyc.CPLX0-7992).

## Annotation

FUNCTION: Together with LptE, is involved in the assembly of lipopolysaccharide (LPS) at the surface of the outer membrane. Contributes to n-hexane resistance. {ECO:0000255|HAMAP-Rule:MF_01411, ECO:0000269|PubMed:12207697, ECO:0000269|PubMed:12724388, ECO:0000269|PubMed:16861298, ECO:0000269|PubMed:18424520, ECO:0000269|PubMed:20203010, ECO:0000269|PubMed:21339611, ECO:0000269|PubMed:2547691, ECO:0000269|PubMed:7811102}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7628|complex.ecocyc.CPLX0-7628]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-7992|complex.ecocyc.CPLX0-7992]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0054|gene.b0054]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31554`
- `KEGG:ecj:JW0053;eco:b0054;ecoc:C3026_00280;`
- `GeneID:945011;`
- `GO:GO:0009279; GO:0015920; GO:0043165; GO:1990351`

## Notes

LPS-assembly protein LptD (Organic solvent tolerance protein)
