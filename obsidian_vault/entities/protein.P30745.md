---
entity_id: "protein.P30745"
entity_type: "protein"
name: "moaA"
source_database: "UniProt"
source_id: "P30745"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "moaA bisA chlA chlA1 narA b0781 JW0764"
---

# moaA

`protein.P30745`

## Static

- Type: `protein`
- Source: `UniProt:P30745`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes, together with MoaC, the conversion of 5'-GTP to cyclic pyranopterin monophosphate (cPMP or molybdopterin precursor Z).; FUNCTION: Catalyzes the cyclization of GTP to (8S)-3',8-cyclo-7,8-dihydroguanosine 5'-triphosphate. {ECO:0000255|HAMAP-Rule:MF_01225}. MoaA, a member of the radical SAM superfamily of enzymes , participates in the PWY-6823 pathway. Biochemical characterization of the enzyme and its reaction mechanism have been performed with the Staphylococcus aureus enzyme, which was shown to catalyze a complex rearrangement reaction that involves the insertion of the C8 carbon of the purine moiety of GTP into the C2'-C3' bond of its ribose moiety . Under anaerobic conditions, the A-type Fe-S cluster carrier proteins CPLX0-7617 and CPLX0-7908 are involved in insertion of [4Fe-4S] clusters into MoaA . Using an E. coli strain overproducing MoaA and EG11666-MONOMER MoaC, PRECURSOR-Z (precursor Z) was produced, purified, and chemically characterized . In earlier work, expression of genes moaABC in a EG10153 mutant resulted in the production of "compound Z", an oxidized product of precursor Z . Mutants in molybdenum cofactor (MoCo) biosynthesis genes were initially identified by their chlorate resistance and hence named "chl"; the mutant phenotype is due to the lack of several enzymes that require MoCo for activity, such as nitrate reductase (see e.g. )...

## Biological Role

Catalyzes RXN-8340 (reaction.ecocyc.RXN-8340). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

FUNCTION: Catalyzes, together with MoaC, the conversion of 5'-GTP to cyclic pyranopterin monophosphate (cPMP or molybdopterin precursor Z).; FUNCTION: Catalyzes the cyclization of GTP to (8S)-3',8-cyclo-7,8-dihydroguanosine 5'-triphosphate. {ECO:0000255|HAMAP-Rule:MF_01225}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-8340|reaction.ecocyc.RXN-8340]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0781|gene.b0781]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30745`
- `KEGG:ecj:JW0764;eco:b0781;ecoc:C3026_04955;`
- `GeneID:945392;`
- `GO:GO:0005525; GO:0006777; GO:0009408; GO:0046872; GO:0051539; GO:0061798; GO:0061799; GO:1904047`
- `EC:4.1.99.22`

## Notes

GTP 3',8-cyclase (EC 4.1.99.22) (Molybdenum cofactor biosynthesis protein A)
