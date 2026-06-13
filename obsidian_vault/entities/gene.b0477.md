---
entity_id: "gene.b0477"
entity_type: "gene"
name: "gsk"
source_database: "NCBI RefSeq"
source_id: "gene-b0477"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0477"
  - "gsk"
---

# gsk

`gene.b0477`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0477`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gsk (gene.b0477) is a gene entity. It encodes gsk (protein.P0AEW6). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of guanosine and inosine to GMP and IMP, respectively (PubMed:10879466, PubMed:7665468, PubMed:7721718). Can also use deoxyguanosine and xanthosine, but not adenosine, uridine, cytidine or deoxythymidine (PubMed:10879466, PubMed:7665468). Shows a strong preference for guanosine (PubMed:10879466, PubMed:7665468). dATP can serve as a phosphate donor as well as ATP. Shows weaker activity with UTP and CTP (PubMed:10879466, PubMed:7665468). {ECO:0000269|PubMed:10879466, ECO:0000269|PubMed:7665468, ECO:0000269|PubMed:7721718}. EcoCyc product frame: GSK-MONOMER. Genomic coordinates: 500125-501429. EcoCyc protein note: Inosine-guanosine kinase (Gsk) catalyzes the phosphorylation of inosine and guanosine to IMP and GMP, respectively. It may be involved in the reutilization of endogenously formed nucleosides . Enzymatic activity is higher with guanosine than with inosine as the phosphate acceptor . Product inhibition studies suggest an ordered Bi Bi catalytic mechanism . Guanosine kinase activity of the wild-type gsk allele appears to be insufficient to allow efficient growth of a PRPP-less mutant by utilization of guanosine via the purine salvage pathway...

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEW6|protein.P0AEW6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001655,ECOCYC:EG11102,GeneID:946584`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:500125-501429:+; feature_type=gene
