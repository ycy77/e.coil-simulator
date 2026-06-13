---
entity_id: "gene.b3297"
entity_type: "gene"
name: "rpsK"
source_database: "NCBI RefSeq"
source_id: "gene-b3297"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3297"
  - "rpsK"
---

# rpsK

`gene.b3297`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3297`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsK (gene.b3297) is a gene entity. It encodes rpsK (protein.P0A7R9). Encoded protein function: FUNCTION: Located on the platform of the 30S subunit, it bridges several disparate RNA helices of the 16S rRNA. Forms part of the Shine-Dalgarno cleft in the 70S ribosome (By similarity). {ECO:0000250}. EcoCyc product frame: EG10910-MONOMER. Genomic coordinates: 3441709-3442098. EcoCyc protein note: The S11 protein is a component of the 30S subunit of the ribosome. S11 is a component of the ribosomal P site and crosslinks to the D loop and anticodon loop of tRNA . S11 was also shown to crosslink to IF2 and IF3 . However, IF3 can interact with ribosomes lacking S11 . Footprinting of IF3 on 16S rRNA and modelling of IF3-30S subunit interactions suggested that IF3 is located near S7 and S11 . S11 binds to or can be crosslinked to 16S rRNA ; S11, S6, and S18 interact cooperatively with two loop regions of 16S rRNA . S11 crosslinks to S21 . S11 and S7 physically and functionally interact; disruption of this interaction by mutagenesis results in error-prone translation . S11 interacts with the endoribonuclease YbeY . S11 is methylated at the amino terminal alanine residue and contains isoaspartate . S11 was also found to be Ser/Thr-phosphorylated . rpsK is encoded within the so-called α operon; its expression is regulated at the translational level by the S4 ribosomal subunit . Review:

## Biological Role

Repressed by rpsD (protein.P0A7V8). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7R9|protein.P0A7R9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=rpsK; function=+
- `represses` <-- [[protein.P0A7V8|protein.P0A7V8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## External IDs

- `Dbxref:ASAP:ABE-0010807,ECOCYC:EG10910,GeneID:947792`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3441709-3442098:-; feature_type=gene
