---
entity_id: "gene.b0051"
entity_type: "gene"
name: "rsmA"
source_database: "NCBI RefSeq"
source_id: "gene-b0051"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0051"
  - "rsmA"
---

# rsmA

`gene.b0051`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0051`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rsmA (gene.b0051) is a gene entity. It encodes rsmA (protein.P06992). Encoded protein function: FUNCTION: Specifically dimethylates two adjacent adenosines (A1518 and A1519) in the loop of a conserved hairpin near the 3'-end of 16S rRNA in the 30S particle. May play a critical role in biogenesis of 30S subunits. Also has a DNA glycosylase/AP lyase activity that removes C mispaired with oxidized T from DNA, and may play a role in protection of DNA against oxidative stress. {ECO:0000269|PubMed:18990185, ECO:0000269|PubMed:19223326, ECO:0000269|PubMed:3905517}. EcoCyc product frame: EG10523-MONOMER. EcoCyc synonyms: ksgA. Genomic coordinates: 51609-52430. EcoCyc protein note: RsmA is the methyltransferase responsible for dimethylation of 16S rRNA at the two adjacent adenosine bases A1518 and A1519 . In vitro, the enzyme is active on CPLX0-3953 "30S ribosomal subunits", but not the fully assembled 70S CPLX0-3964 . RsmA may play a role in biogenesis of the small subunit of the ribosome , providing a checkpoint where binding of RsmA keeps immature 30S subunits from entering the translational cycle . RsmA and the ribosome maturation factor EG11178-MONOMER RbfA function together in checkpointing maturation of the 30S subunit . Methylation of the 16S rRNA by RsmA is important for release of RbfA from the 30S subunit...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06992|protein.P06992]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000175,ECOCYC:EG10523,GeneID:944939`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:51609-52430:-; feature_type=gene
