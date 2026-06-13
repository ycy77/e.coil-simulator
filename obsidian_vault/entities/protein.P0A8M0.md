---
entity_id: "protein.P0A8M0"
entity_type: "protein"
name: "asnS"
source_database: "UniProt"
source_id: "P0A8M0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "asnS tss b0930 JW0913"
---

# asnS

`protein.P0A8M0`

## Static

- Type: `protein`
- Source: `UniProt:P0A8M0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Asparagine--tRNA ligase (EC 6.1.1.22) (Asparaginyl-tRNA synthetase) (AsnRS) Asparagine—tRNA ligase (AsnRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. AsnRS belongs to the Class IIb aminoacyl-tRNA synthetases . AsnRS is a dimer in solution . Analysis of mutants suggests that the Y426 residue is involved in ATP binding ; a P231L mutation, which is located in the conserved motif 2 of class II aminoacyl-tRNA synthetases, leads to increases in the Km for asparagine and ATP . There is a general discrepancy between kcat values of aminoacyl-tRNA synthetases that were measured in vitro and values that were calculated as needed to support measured growth rates . Modeling of these parameters in E. coli has found that the required kcat values are on average 7.6-fold higher than those measured in vitro . Tss: "temperature-sensitive" AsnS: "asparaginyl-tRNA synthetase" Review:

## Biological Role

Component of asparagine—tRNA ligase (complex.ecocyc.ASNS-CPLX).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

Asparagine--tRNA ligase (EC 6.1.1.22) (Asparaginyl-tRNA synthetase) (AsnRS)

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ASNS-CPLX|complex.ecocyc.ASNS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0930|gene.b0930]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8M0`
- `KEGG:ecj:JW0913;eco:b0930;ecoc:C3026_05715;`
- `GeneID:93776484;945555;`
- `GO:GO:0003676; GO:0004816; GO:0005524; GO:0005737; GO:0006418; GO:0006421; GO:0042803`
- `EC:6.1.1.22`

## Notes

Asparagine--tRNA ligase (EC 6.1.1.22) (Asparaginyl-tRNA synthetase) (AsnRS)
