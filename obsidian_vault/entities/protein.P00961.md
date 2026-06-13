---
entity_id: "protein.P00961"
entity_type: "protein"
name: "glyS"
source_database: "UniProt"
source_id: "P00961"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glyS glyS(B) b3559 JW3530"
---

# glyS

`protein.P00961`

## Static

- Type: `protein`
- Source: `UniProt:P00961`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Glycine--tRNA ligase beta subunit (EC 6.1.1.14) (Glycyl-tRNA synthetase beta subunit) (GlyRS) The isolated β subunit of GlyRS is monomeric in solution and binds tRNAGly; there is one binding site per monomer . The N-terminal domain of the β subunit contains residues required for adenylate synthesis, while the C-terminal domain appears to be dispensable for catalytic activity . A crystal structure of GlyRS has been solved at 2.68 Å resolution, revealing an unusual X-shaped architecture with an α subunit dimer at the center. The α subunit contains binding sites for glycine and ATP, while the β subunit interacts with the γ-phosphate of ATP. Site-directed mutagenesis supported the proposed roles for the α and β subunits . Site-directed mutagenesis of the cysteine residues C98, C395 and C450 established that β subunit cysteine thiols are not required for catalytic activity of GlyRS; however, C395 can be alkylated by NEM, resulting in loss of GlyRS activity . There is a general discrepancy between kcat values of aminoacyl-tRNA synthetases that were measured in vitro and values that were calculated as needed to support measured growth rates . Modeling of these parameters in E. coli has found that the required kcat values are on average 7.6-fold higher than those measured in vitro .

## Biological Role

Component of glycine—tRNA ligase (complex.ecocyc.GLYS-CPLX).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

Glycine--tRNA ligase beta subunit (EC 6.1.1.14) (Glycyl-tRNA synthetase beta subunit) (GlyRS)

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.GLYS-CPLX|complex.ecocyc.GLYS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3559|gene.b3559]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00961`
- `KEGG:ecj:JW3530;eco:b3559;ecoc:C3026_19295;`
- `GeneID:948080;`
- `GO:GO:0000049; GO:0004814; GO:0004820; GO:0005524; GO:0005829; GO:0006420; GO:0006426; GO:0009345`
- `EC:6.1.1.14`

## Notes

Glycine--tRNA ligase beta subunit (EC 6.1.1.14) (Glycyl-tRNA synthetase beta subunit) (GlyRS)
