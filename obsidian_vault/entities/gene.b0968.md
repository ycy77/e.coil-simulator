---
entity_id: "gene.b0968"
entity_type: "gene"
name: "yccX"
source_database: "NCBI RefSeq"
source_id: "gene-b0968"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0968"
  - "yccX"
---

# yccX

`gene.b0968`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0968`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yccX (gene.b0968) is a gene entity. It encodes yccX (protein.P0AB65). Encoded protein function: Acylphosphatase (EC 3.6.1.7) (Acylphosphate phosphohydrolase) EcoCyc product frame: G6502-MONOMER. Genomic coordinates: 1030064-1030342. EcoCyc protein note: yccX encodes an acylphosphatase with relatively low catalytic efficiency, but very high structural stability . A C5-C49 disulfide bond is not required for catalytic activity , but accelerates protein folding . The functional role of the enzyme in vivo is unknown . An NMR solution structure of YccX has been determined . A crystal structure of YccX was obtained to 2.55 Å resolution. A 3D model of this structure differs from the NMR structure in multiple ways, including the presence of an additional short alpha helix (residues 81-86) and an intertwined dimer in the C-terminal edge where the C-terminal β-strand was swapped between two protomers. This structure differs from the Pyrococcus horikoshii AcP dimer . yccX shows differential codon adaptation, resulting in differential translation efficiency signatures, in thermophilic microbes. It was therefore predicted to play a role in the heat shock response. A yccX deletion mutant was shown to be more sensitive than wild-type specifically to heat shock, but not other stresses...

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB65|protein.P0AB65]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003276,ECOCYC:G6502,GeneID:945304`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1030064-1030342:+; feature_type=gene
