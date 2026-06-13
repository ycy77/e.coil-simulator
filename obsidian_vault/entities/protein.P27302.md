---
entity_id: "protein.P27302"
entity_type: "protein"
name: "tktA"
source_database: "UniProt"
source_id: "P27302"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tktA tkt b2935 JW5478"
---

# tktA

`protein.P27302`

## Static

- Type: `protein`
- Source: `UniProt:P27302`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the transfer of a two-carbon ketol group from a ketose donor to an aldose acceptor, via a covalent intermediate with the cofactor thiamine pyrophosphate. Thus, catalyzes the reversible transfer of a two-carbon ketol group from sedoheptulose-7-phosphate to glyceraldehyde-3-phosphate, producing xylulose-5-phosphate and ribose-5-phosphate. {ECO:0000269|PubMed:17914867, ECO:0000269|PubMed:7607225}. Transketolase catalyzes the reversible transfer of a ketol group between several donor and acceptor substrates. This key enzyme is a reversible link between glycolysis and the pentose phosphate pathway. The enzyme is involved in the catabolism of pentose sugars, the formation of D-ribose 5-phosphate, and the provision of D-erythrose 4-phosphate, a precursor of aromatic amino acids and PLP . E. coli contains two transketolase isozymes, TktA and TktB. TktA is responsible for the major transketolase activity . In addition to its function in central carbon metabolism, transketolase appears to also have an unexpected role in chromosome structure; a tktA mutant affects chromosome topology . Crystal structures of TktA in complex with donor and acceptor substrates and inhibitors have been solved, elucidating the reaction mechanism and mode of action of transketolase...

## Biological Role

Catalyzes D-sedoheptulose-7-phosphate:thiamin diphosphate glycolaldehydetransferase (reaction.R06863). Component of transketolase 1 (complex.ecocyc.TRANSKETOI-CPLX).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of a two-carbon ketol group from a ketose donor to an aldose acceptor, via a covalent intermediate with the cofactor thiamine pyrophosphate. Thus, catalyzes the reversible transfer of a two-carbon ketol group from sedoheptulose-7-phosphate to glyceraldehyde-3-phosphate, producing xylulose-5-phosphate and ribose-5-phosphate. {ECO:0000269|PubMed:17914867, ECO:0000269|PubMed:7607225}.

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
- `is_component_of` --> [[complex.ecocyc.TRANSKETOI-CPLX|complex.ecocyc.TRANSKETOI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2935|gene.b2935]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27302`
- `KEGG:ecj:JW5478;eco:b2935;ecoc:C3026_16070;`
- `GeneID:75205229;947420;`
- `GO:GO:0000287; GO:0004802; GO:0005829; GO:0006098; GO:0009052; GO:0030145; GO:0030976; GO:0042803`
- `EC:2.2.1.1`

## Notes

Transketolase 1 (TK 1) (EC 2.2.1.1)
