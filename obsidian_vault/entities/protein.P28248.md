---
entity_id: "protein.P28248"
entity_type: "protein"
name: "dcd"
source_database: "UniProt"
source_id: "P28248"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dcd dus paxA b2065 JW2050"
---

# dcd

`protein.P28248`

## Static

- Type: `protein`
- Source: `UniProt:P28248`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the deamination of dCTP to dUTP. {ECO:0000255|HAMAP-Rule:MF_00146, ECO:0000269|PubMed:1324907, ECO:0000269|PubMed:15539408, ECO:0000269|PubMed:17651436, ECO:0000269|PubMed:17996716}. dCTP deaminase (Dcd) catalyzes the deamination of dCTP to dUTP in the main pathway for dTTP biosynthesis in E. coli, PWY-7187 . dCTP deaminase is unusual among nucleoside and nucleotide deaminases in that it does not require a metal ion for catalysis. Crystal structures of wild-type and mutant forms of the enzyme in complexes with the substrate, product or inhibitor have been determined . Site-directed mutagenesis of predicted active site residues produced catalytically inactive enzymes . The true substrate of dCTP deaminase appears to be the dCTP·Mg2+ complex; a catalytic mechanism was proposed . Mutations in the S111 and E138 residues alter the enzyme's inhibition by dTTP . dcd mutants require thymidine supplementation for optimal growth. deoA mutations bypass the requirement for thymidine supplementation by enabling diversion of an intermediate of the PWY0-181 . Mutations in dcd suppress the temperature-sensitive lethal phenotype of a dut-1 ΔxthA double mutant , the temperature-sensitive dut-22 mutant , and the synthetic lethality of a dut-1/dut-11 rec double mutant . However, various dcd mutations are unable to suppress the lethal phenotype of a dut insertion mutant...

## Biological Role

Component of dCTP deaminase (complex.ecocyc.DCTP-DEAM-CPLX).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the deamination of dCTP to dUTP. {ECO:0000255|HAMAP-Rule:MF_00146, ECO:0000269|PubMed:1324907, ECO:0000269|PubMed:15539408, ECO:0000269|PubMed:17651436, ECO:0000269|PubMed:17996716}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DCTP-DEAM-CPLX|complex.ecocyc.DCTP-DEAM-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b2065|gene.b2065]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P28248`
- `KEGG:ecj:JW2050;eco:b2065;ecoc:C3026_11615;`
- `GeneID:946593;`
- `GO:GO:0000166; GO:0005829; GO:0006226; GO:0006229; GO:0006235; GO:0008829; GO:0009314; GO:0015949; GO:0032991; GO:0042802; GO:0070207`
- `EC:3.5.4.13`

## Notes

dCTP deaminase (EC 3.5.4.13) (Deoxycytidine triphosphate deaminase)
