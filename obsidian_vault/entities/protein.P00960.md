---
entity_id: "protein.P00960"
entity_type: "protein"
name: "glyQ"
source_database: "UniProt"
source_id: "P00960"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glyQ glyS(A) b3560 JW3531"
---

# glyQ

`protein.P00960`

## Static

- Type: `protein`
- Source: `UniProt:P00960`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Glycine--tRNA ligase alpha subunit (EC 6.1.1.14) (Glycyl-tRNA synthetase alpha subunit) (GlyRS) A crystal structure of GlyRS has been solved at 2.68 Å resolution, revealing an unusual X-shaped architecture with an α subunit dimer at the center. The α subunit contains binding sites for glycine and ATP, while the β subunit interacts with the γ-phosphate of ATP. Site-directed mutagenesis supported the proposed roles for the α and β subunits . CfcA: "control the frequency of cell division"

## Biological Role

Component of glycine—tRNA ligase (complex.ecocyc.GLYS-CPLX).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

Glycine--tRNA ligase alpha subunit (EC 6.1.1.14) (Glycyl-tRNA synthetase alpha subunit) (GlyRS)

## Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.GLYS-CPLX|complex.ecocyc.GLYS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3560|gene.b3560]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00960`
- `KEGG:ecj:JW3531;eco:b3560;`
- `GeneID:948079;`
- `GO:GO:0004820; GO:0005524; GO:0005829; GO:0006426; GO:0009345`
- `EC:6.1.1.14`

## Notes

Glycine--tRNA ligase alpha subunit (EC 6.1.1.14) (Glycyl-tRNA synthetase alpha subunit) (GlyRS)
