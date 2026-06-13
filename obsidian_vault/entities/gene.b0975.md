---
entity_id: "gene.b0975"
entity_type: "gene"
name: "hyaD"
source_database: "NCBI RefSeq"
source_id: "gene-b0975"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0975"
  - "hyaD"
---

# hyaD

`gene.b0975`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0975`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hyaD (gene.b0975) is a gene entity. It encodes hyaD (protein.P19930). Encoded protein function: FUNCTION: Protease involved in the C-terminal processing of HyaB, the large subunit of hydrogenase 1. {ECO:0000305}. EcoCyc product frame: EG10471-MONOMER. Genomic coordinates: 1035770-1036357. EcoCyc protein note: The HyaD protein is required for the synthesis of active hydrogenase isoenzyme 1 (HYD1) . HyaD is similar to HybD, the maturation protease for hydrogenase 2 . It is therefore likely that HyaD is an endopeptidase required for maturation of hydrogenase 1.

## Biological Role

Repressed by iscR (protein.P0AGK8). Activated by ydeO (protein.P76135).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P19930|protein.P19930]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=hyaD; function=+
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=hyaD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003292,ECOCYC:EG10471,GeneID:945575`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1035770-1036357:+; feature_type=gene
