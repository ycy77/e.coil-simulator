---
entity_id: "gene.b3559"
entity_type: "gene"
name: "glyS"
source_database: "NCBI RefSeq"
source_id: "gene-b3559"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3559"
  - "glyS"
---

# glyS

`gene.b3559`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3559`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glyS (gene.b3559) is a gene entity. It encodes glyS (protein.P00961). Encoded protein function: Glycine--tRNA ligase beta subunit (EC 6.1.1.14) (Glycyl-tRNA synthetase beta subunit) (GlyRS) EcoCyc product frame: GLYS-MONOMER. Genomic coordinates: 3722328-3724397. EcoCyc protein note: The isolated β subunit of GlyRS is monomeric in solution and binds tRNAGly; there is one binding site per monomer . The N-terminal domain of the β subunit contains residues required for adenylate synthesis, while the C-terminal domain appears to be dispensable for catalytic activity . A crystal structure of GlyRS has been solved at 2.68 Å resolution, revealing an unusual X-shaped architecture with an α subunit dimer at the center. The α subunit contains binding sites for glycine and ATP, while the β subunit interacts with the γ-phosphate of ATP. Site-directed mutagenesis supported the proposed roles for the α and β subunits . Site-directed mutagenesis of the cysteine residues C98, C395 and C450 established that β subunit cysteine thiols are not required for catalytic activity of GlyRS; however, C395 can be alkylated by NEM, resulting in loss of GlyRS activity . There is a general discrepancy between kcat values of aminoacyl-tRNA synthetases that were measured in vitro and values that were calculated as needed to support measured growth rates . Modeling of these parameters in E...

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00961|protein.P00961]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011624,ECOCYC:EG10410,GeneID:948080`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3722328-3724397:-; feature_type=gene
