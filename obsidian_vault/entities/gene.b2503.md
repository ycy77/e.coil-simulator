---
entity_id: "gene.b2503"
entity_type: "gene"
name: "pdeF"
source_database: "NCBI RefSeq"
source_id: "gene-b2503"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2503"
  - "pdeF"
---

# pdeF

`gene.b2503`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2503`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdeF (gene.b2503) is a gene entity. It encodes pdeF (protein.P77172). Encoded protein function: FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG. Truncated proteins consisting of the GGDEF/EAL domains (residues 319-747) or of the EAL domain alone (481-747) have c-di-GMP phosphodiesterase activity. They do not have diguanylate cyclase activity. Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. {ECO:0000269|PubMed:20522491}. EcoCyc product frame: G7314-MONOMER. EcoCyc synonyms: yfgF. Genomic coordinates: 2626695-2628938.

## Biological Role

Repressed by hns (protein.P0ACF8), nac (protein.Q47005). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77172|protein.P77172]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=pdeF; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=pdeF; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=pdeF; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008240,ECOCYC:G7314,GeneID:946968`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2626695-2628938:-; feature_type=gene
