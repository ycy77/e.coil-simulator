---
entity_id: "protein.P22255"
entity_type: "protein"
name: "cysQ"
source_database: "UniProt"
source_id: "P22255"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02095, ECO:0000269|PubMed:15911532}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_02095, ECO:0000305}; Cytoplasmic side {ECO:0000255|HAMAP-Rule:MF_02095, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysQ amtA b4214 JW4172"
---

# cysQ

`protein.P22255`

## Static

- Type: `protein`
- Source: `UniProt:P22255`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02095, ECO:0000269|PubMed:15911532}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_02095, ECO:0000305}; Cytoplasmic side {ECO:0000255|HAMAP-Rule:MF_02095, ECO:0000305}.

## Enriched Summary

FUNCTION: Converts adenosine-3',5'-bisphosphate (PAP) to AMP. May also convert adenosine 3'-phosphate 5'-phosphosulfate (PAPS) to adenosine 5'-phosphosulfate (APS). Has 10000-fold lower activity towards inositol 1,4-bisphosphate (Ins(1,4)P2). {ECO:0000269|PubMed:10224133, ECO:0000269|PubMed:16682444, ECO:0000269|PubMed:7493934}. CysQ is an adenosine-3',5'-bisphosphate nucleotidase which recycles adenosine-3',5'-bisphosphate (PAP) that is generated during sulfate assimilation (see SO4ASSIM-PWY) and holo-ACP synthesis for the biosynthesis of fatty acids (see HOLO-ACP-SYNTH-CPLX and EG12221-MONOMER). CysQ is inhibited by Li+, and the enzyme is the main target for lithium toxicity in E. coli . The protein is similar to SuhB and mammalian inositol monophosphatase . cysQ mutants require cysteine or sulfite to grow under aerobic conditions, though they continue to carry out normal uptake of sulfate . A cysQ mutation can be complemented with the rice gene RHL, which encodes an enzyme catalyzing the conversion of adenosine 3'-phosphate 5'-phosphosulfate (PAPS) to adenosine 5'-phosphosulfate (APS) . The cysQ mutant phenotype is likely due to inhibition of PAPSSULFOTRANS-CPLX by accumulating adenosine-3',5'-bisphosphate. CysQ was initially identified as a putative ammonium transporter . This functional assignment was later shown to be incorrect...

## Biological Role

Catalyzes adenosine-3',5'-bisphosphate 3'-phosphohydrolase (reaction.R00188), 3'-phospho-5'-adenylyl sulfate 3'-phosphohydrolase (reaction.R00508), 325-BISPHOSPHATE-NUCLEOTIDASE-RXN (reaction.ecocyc.325-BISPHOSPHATE-NUCLEOTIDASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Converts adenosine-3',5'-bisphosphate (PAP) to AMP. May also convert adenosine 3'-phosphate 5'-phosphosulfate (PAPS) to adenosine 5'-phosphosulfate (APS). Has 10000-fold lower activity towards inositol 1,4-bisphosphate (Ins(1,4)P2). {ECO:0000269|PubMed:10224133, ECO:0000269|PubMed:16682444, ECO:0000269|PubMed:7493934}.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00188|reaction.R00188]] `KEGG` `database` - via EC:3.1.3.7
- `catalyzes` --> [[reaction.R00508|reaction.R00508]] `KEGG` `database` - via EC:3.1.3.7
- `catalyzes` --> [[reaction.ecocyc.325-BISPHOSPHATE-NUCLEOTIDASE-RXN|reaction.ecocyc.325-BISPHOSPHATE-NUCLEOTIDASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4214|gene.b4214]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P22255`
- `KEGG:ecj:JW4172;eco:b4214;ecoc:C3026_22760;`
- `GeneID:948728;`
- `GO:GO:0000103; GO:0000287; GO:0005886; GO:0008441; GO:0046854; GO:0050427`
- `EC:3.1.3.7`

## Notes

3'(2'),5'-bisphosphate nucleotidase CysQ (EC 3.1.3.7) (3'(2'),5-bisphosphonucleoside 3'(2')-phosphohydrolase) (3'-phosphoadenosine 5'-phosphate phosphatase) (PAP phosphatase) (DPNPase)
