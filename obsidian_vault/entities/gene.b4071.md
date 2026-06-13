---
entity_id: "gene.b4071"
entity_type: "gene"
name: "nrfB"
source_database: "NCBI RefSeq"
source_id: "gene-b4071"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4071"
  - "nrfB"
---

# nrfB

`gene.b4071`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4071`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nrfB (gene.b4071) is a gene entity. It encodes nrfB (protein.P0ABL1). Encoded protein function: FUNCTION: Plays a role in nitrite reduction. EcoCyc product frame: CYTOCHROMEC-MONOMER. EcoCyc synonyms: yjcI. Genomic coordinates: 4289245-4289811.

## Biological Role

Repressed by fis (protein.P0A6R3), narL (protein.P0AF28), nsrR (protein.P0AF63). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), narL (protein.P0AF28), narP (protein.P31802).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABL1|protein.P0ABL1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nrfB; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=nrfB; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=nrfB; function=-+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `C` - regulator=NarP; target=nrfB; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nrfB; function=-
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=nrfB; function=-+
- `represses` <-- [[protein.P0AF63|protein.P0AF63]] `RegulonDB` `C` - regulator=NsrR; target=nrfB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013344,ECOCYC:EG11945,GeneID:948573`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4289245-4289811:+; feature_type=gene
