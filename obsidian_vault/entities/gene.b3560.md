---
entity_id: "gene.b3560"
entity_type: "gene"
name: "glyQ"
source_database: "NCBI RefSeq"
source_id: "gene-b3560"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3560"
  - "glyQ"
---

# glyQ

`gene.b3560`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3560`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glyQ (gene.b3560) is a gene entity. It encodes glyQ (protein.P00960). Encoded protein function: Glycine--tRNA ligase alpha subunit (EC 6.1.1.14) (Glycyl-tRNA synthetase alpha subunit) (GlyRS) EcoCyc product frame: GLYQ-MONOMER. EcoCyc synonyms: cfcA, glyS(A). Genomic coordinates: 3724407-3725318. EcoCyc protein note: A crystal structure of GlyRS has been solved at 2.68 Å resolution, revealing an unusual X-shaped architecture with an α subunit dimer at the center. The α subunit contains binding sites for glycine and ATP, while the β subunit interacts with the γ-phosphate of ATP. Site-directed mutagenesis supported the proposed roles for the α and β subunits . CfcA: "control the frequency of cell division"

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00960|protein.P00960]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011626,ECOCYC:EG10409,GeneID:948079`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3724407-3725318:-; feature_type=gene
