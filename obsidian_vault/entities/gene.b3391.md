---
entity_id: "gene.b3391"
entity_type: "gene"
name: "hofQ"
source_database: "NCBI RefSeq"
source_id: "gene-b3391"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3391"
  - "hofQ"
---

# hofQ

`gene.b3391`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3391`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hofQ (gene.b3391) is a gene entity. It encodes hofQ (protein.P34749). Encoded protein function: FUNCTION: Required for the use of extracellular DNA as a nutrient (PubMed:11591672). Could be the porin responsible for transport of DNA across the outer membrane (PubMed:16707682). {ECO:0000269|PubMed:11591672, ECO:0000305|PubMed:16707682}. EcoCyc product frame: EG12113-MONOMER. EcoCyc synonyms: hopQ. Genomic coordinates: 3519465-3520703. EcoCyc protein note: hofQ is a homologue of the H. influenzae competence gene comE. A mutant with a defect in this gene is out-competed by its wild-type parent during stationary phase and is unable to utilize DNA as a sole carbon or energy source, despite retaining the ability to be artificially induced to competence. This suggests separate mechanisms for DNA uptake depending on whether it will be used for nutrient acquisition or genetic transformation . HofQ is predicted to localize to the outer membrane and may be the porin responsible for transport of double-stranded DNA across the outer membrane . hofQ is poorly expressed . hofQ is not required for spontaneous plasmid transformation on nutrient plates with high agar concentration .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P34749|protein.P34749]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011071,ECOCYC:EG12113,GeneID:947901`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3519465-3520703:-; feature_type=gene
