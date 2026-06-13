---
entity_id: "gene.b1921"
entity_type: "gene"
name: "fliZ"
source_database: "NCBI RefSeq"
source_id: "gene-b1921"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1921"
  - "fliZ"
---

# fliZ

`gene.b1921`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1921`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliZ (gene.b1921) is a gene entity. It encodes fliZ (protein.P52627). Encoded protein function: FUNCTION: During the post-exponential growth phase transiently interferes with RpoS (sigma S) activity without affecting expression of RpoS itself. It is probably not an anti-sigma factor as its overexpression is detrimental in rapidly growing cells where there is almost no sigma S factor. There is a strong overlap between Crl-activated genes and FliZ-down-regulated genes. FliZ acts as a timing device for expression of the genes for the adhesive curli fimbriae by indirectly decreasing expression of the curli regulator CsgD. {ECO:0000269|PubMed:18765794}. EcoCyc product frame: EG11356-MONOMER. EcoCyc synonyms: yedH. Genomic coordinates: 2000473-2001024. EcoCyc protein note: The transcriptional repressor FliZ controls the transcription of genes involved in the regulation of curli expression and the motility system . During the post-exponential growth phase, this regulator is an abundant protein in the genome, with about 21,500 molecules per cell. Transcriptome expression analysis showed a global antagonistic effect between FliZ and σS that resulted in physiological traits, including flagellum-mediated motility and curli fimbria-mediated adhesion . Overexpression of FliZ slightly increased polyP accumulation...

## Biological Role

Repressed by csgD (protein.P52106), ecpR (protein.P71301), sutR (protein.P77626). Activated by rpoD (protein.P00579), fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52627|protein.P52627]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fliZ; function=+
- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=fliZ; function=+
- `represses` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=fliZ; function=-
- `represses` <-- [[protein.P71301|protein.P71301]] `RegulonDB` `S` - regulator=MatA; target=fliZ; function=-
- `represses` <-- [[protein.P77626|protein.P77626]] `RegulonDB` `S` - regulator=SutR; target=fliZ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006394,ECOCYC:EG11356,GeneID:946833`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2000473-2001024:-; feature_type=gene
