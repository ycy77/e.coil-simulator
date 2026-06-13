---
entity_id: "gene.b1254"
entity_type: "gene"
name: "yciB"
source_database: "NCBI RefSeq"
source_id: "gene-b1254"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1254"
  - "yciB"
---

# yciB

`gene.b1254`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1254`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yciB (gene.b1254) is a gene entity. It encodes yciB (protein.P0A710). Encoded protein function: FUNCTION: Plays a role in cell envelope biogenesis, maintenance of cell envelope integrity and membrane homeostasis (PubMed:26391555, PubMed:26454142, PubMed:30368949, PubMed:33431434). Required for the normal cell elongation (PubMed:26391555). May participate in the cell division process (PubMed:26391555). Important for the septum site localization of the essential divisome protein ZipA (PubMed:26391555). {ECO:0000269|PubMed:26391555, ECO:0000269|PubMed:26454142, ECO:0000269|PubMed:30368949, ECO:0000269|PubMed:33431434}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from E.coli strain 869 across the inner membrane to the cytoplasm, where CdiA degrades DNA. Toxin transport is strain-specific, mutations in this gene do not confer resistance to several other tested CdiA toxins. {ECO:0000269|PubMed:26305955}. EcoCyc product frame: EG11122-MONOMER. Genomic coordinates: 1312351-1312890. EcoCyc protein note: YciB has sequence similarity with IspA - a Shigella flexneri protein with a role in cell division and intracellular spreading...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A710|protein.P0A710]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004200,ECOCYC:EG11122,GeneID:946228`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1312351-1312890:-; feature_type=gene
