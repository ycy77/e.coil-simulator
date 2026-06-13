---
entity_id: "gene.b3531"
entity_type: "gene"
name: "bcsZ"
source_database: "NCBI RefSeq"
source_id: "gene-b3531"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3531"
  - "bcsZ"
---

# bcsZ

`gene.b3531`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3531`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bcsZ (gene.b3531) is a gene entity. It encodes bcsZ (protein.P37651). Encoded protein function: FUNCTION: Hydrolyzes carboxymethylcellulose. EcoCyc product frame: EG12258-MONOMER. EcoCyc synonyms: bcsC, yhjM. Genomic coordinates: 3689155-3690261. EcoCyc protein note: The bcsZ gene encodes an endo-1,4-D-glucanase which belongs to glycosyl hydrolase family 8 . BcsZ has a predicted signal sequence ; a computational prediction that BcsZ is a lipoprotein is thought to be a probable false positive . In cell fractionation assays, the enzymatic activity appeared to be primarily extracellular , although the publication reported no positive controls. Crystal structures of apo-BcsZ and that of a catalytically inactive mutant bound to the substrate cellopentaose have been solved . BcsZ is encoded in a predicted operon together with bcsA, bcsB, and bcsC. In other organisms, these genes are involved in cellulose biosynthesis, a characteristic of the rdar morphotype. However, the K-12 laboratory strain of E. coli does not show a rdar morphotype and does not produce cellulose . In E. coli K-12 strains such as W3110 and MG1655, a "domesticating SNP" consists of a point mutation that introduces a stop codon after the first 5 amino acids of the wild-type bcsQ ORF. This domesticating SNP lowers expression of both bcsQ and the downstream bcsA gene...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37651|protein.P37651]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011541,ECOCYC:EG12258,GeneID:948046`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3689155-3690261:-; feature_type=gene
