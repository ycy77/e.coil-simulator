---
entity_id: "protein.P33570"
entity_type: "protein"
name: "tktB"
source_database: "UniProt"
source_id: "P33570"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tktB b2465 JW2449"
---

# tktB

`protein.P33570`

## Static

- Type: `protein`
- Source: `UniProt:P33570`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible transfer of a two-carbon ketol group from sedoheptulose-7-phosphate to glyceraldehyde-3-phosphate, producing xylulose-5-phosphate and ribose-5-phosphate. Catalyzes the transfer of a two-carbon ketol group from a ketose donor to an aldose acceptor, via a covalent intermediate with the cofactor thiamine pyrophosphate. {ECO:0000269|PubMed:8396116}. Transketolase catalyzes the reversible transfer of a ketol group between several donor and acceptor substrates. This key enzyme is a reversible link between glycolysis and the pentose phosphate pathway. The enzyme is involved in the catabolism of pentose sugars, the formation of D-ribose 5-phosphate, and the provision of D-erythrose 4-phosphate, a precursor of aromatic amino acids and PLP . E. coli contains two transketolase isozymes, TktA and TktB. TktB is responsible for the minor transketolase activity . The subunit structure of transketolase 2 (TktB) has not been explicitly determined. However, transketolase 1 (TktA) is homodimeric . Overproduction of TktB suppresses the tktA mutant phenotype . A tktA tktB double mutant requires pyridoxine (or 4-hydroxy-L-threonine or glycolaldehyde), aromatic amino acids and vitamins for growth...

## Biological Role

Catalyzes D-sedoheptulose-7-phosphate:thiamin diphosphate glycolaldehydetransferase (reaction.R06863). Component of transketolase 2 (complex.ecocyc.CPLX0-1261).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible transfer of a two-carbon ketol group from sedoheptulose-7-phosphate to glyceraldehyde-3-phosphate, producing xylulose-5-phosphate and ribose-5-phosphate. Catalyzes the transfer of a two-carbon ketol group from a ketose donor to an aldose acceptor, via a covalent intermediate with the cofactor thiamine pyrophosphate. {ECO:0000269|PubMed:8396116}.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R06863|reaction.R06863]] `KEGG` `database` - via EC:2.2.1.1
- `is_component_of` --> [[complex.ecocyc.CPLX0-1261|complex.ecocyc.CPLX0-1261]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2465|gene.b2465]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33570`
- `KEGG:ecj:JW2449;eco:b2465;ecoc:C3026_13675;`
- `GeneID:945865;`
- `GO:GO:0004802; GO:0005829; GO:0006098; GO:0009052; GO:0046872`
- `EC:2.2.1.1`

## Notes

Transketolase 2 (TK 2) (EC 2.2.1.1)
