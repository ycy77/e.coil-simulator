---
entity_id: "protein.P0ADC1"
entity_type: "protein"
name: "lptE"
source_database: "UniProt"
source_id: "P0ADC1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_01186, ECO:0000269|PubMed:20446753, ECO:0000269|PubMed:21257904, ECO:0000269|PubMed:3316191}; Lipid-anchor {ECO:0000255|HAMAP-Rule:MF_01186, ECO:0000269|PubMed:20446753, ECO:0000269|PubMed:21257904, ECO:0000269|PubMed:3316191}. Note=A substantial portion is found inside the LptD beta-barrel."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lptE rlpB b0641 JW0636"
---

# lptE

`protein.P0ADC1`

## Static

- Type: `protein`
- Source: `UniProt:P0ADC1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_01186, ECO:0000269|PubMed:20446753, ECO:0000269|PubMed:21257904, ECO:0000269|PubMed:3316191}; Lipid-anchor {ECO:0000255|HAMAP-Rule:MF_01186, ECO:0000269|PubMed:20446753, ECO:0000269|PubMed:21257904, ECO:0000269|PubMed:3316191}. Note=A substantial portion is found inside the LptD beta-barrel.

## Enriched Summary

FUNCTION: Together with LptD, is involved in the assembly of lipopolysaccharide (LPS) at the surface of the outer membrane. Required for the proper assembly of LptD. Binds LPS and may serve as the LPS recognition site at the outer membrane. {ECO:0000255|HAMAP-Rule:MF_01186, ECO:0000269|PubMed:16861298, ECO:0000269|PubMed:18424520, ECO:0000269|PubMed:20203010}. LptE is part of the outer membrane LptDE complex that functions to assemble lipopolysaccharide (LPS) at the cell surface . lptE (formerly rlpB) encodes a minor lipoprotein; in vitro expression of the mature protein is inhibited by treatment with the signal peptidase II inhibitor, globomycin; the protein incorporates 3H-labeled palmitate and 3H-labeled glycerol in vitro . Purifed LptE binds LPS specifically . LptE binds LPS, disrupts LPS-LPS interactions and affects LPS aggregation propensity in vitro. LptE binds and solubilizes surface bound LPS in vitro. LptE containing the double mutation R91D K136D is able to bind, but cannot solubilize, surface bound LPS. These two amino acids may form part of an LPS interaction site that functions to disaggregate LPS and aid insertion into the outer membrane . LptE consists of 2 α-helices and 4 β-strands; two loops (one located between β-strands 2 and 3, the other between β-strand 4 and α-helix 2) form a lipid binding site...

## Biological Role

Component of lipopolysaccharide transport system - outer membrane assembly complex (complex.ecocyc.CPLX0-7628), lipopolysaccharide transport system (complex.ecocyc.CPLX0-7992).

## Annotation

FUNCTION: Together with LptD, is involved in the assembly of lipopolysaccharide (LPS) at the surface of the outer membrane. Required for the proper assembly of LptD. Binds LPS and may serve as the LPS recognition site at the outer membrane. {ECO:0000255|HAMAP-Rule:MF_01186, ECO:0000269|PubMed:16861298, ECO:0000269|PubMed:18424520, ECO:0000269|PubMed:20203010}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7628|complex.ecocyc.CPLX0-7628]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-7992|complex.ecocyc.CPLX0-7992]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0641|gene.b0641]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADC1`
- `KEGG:ecj:JW0636;eco:b0641;ecoc:C3026_03205;`
- `GeneID:93776841;946257;`
- `GO:GO:0001530; GO:0009279; GO:0015920; GO:0043165; GO:1990351`

## Notes

LPS-assembly lipoprotein LptE (Rare lipoprotein B)
