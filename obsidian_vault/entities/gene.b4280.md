---
entity_id: "gene.b4280"
entity_type: "gene"
name: "nanY"
source_database: "NCBI RefSeq"
source_id: "gene-b4280"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4280"
  - "nanY"
---

# nanY

`gene.b4280`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4280`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nanY (gene.b4280) is a gene entity. It encodes nanY (protein.P39353). Encoded protein function: FUNCTION: Hydratase involved in the degradation of sialic acids (PubMed:32542330, PubMed:32669363). Catalyzes the reversible conversion of the dehydrated form of N-acetylneuraminate (Neu5Ac), 2,7-anhydro-N-acetylneuraminate (2,7-AN), to Neu5Ac (PubMed:32542330, PubMed:32669363). Also catalyzes the irreversible conversion of 2-deoxy-2,3-didehydro-N-acetylneuraminate (2,3-EN) to Neu5Ac (PubMed:32542330). The reaction mechanism involves keto intermediates and the transient formation of NADH (PubMed:32542330). {ECO:0000269|PubMed:32542330, ECO:0000269|PubMed:32669363}. EcoCyc product frame: G7901-MONOMER. EcoCyc synonyms: yjhC. Genomic coordinates: 4505287-4506405.

## Biological Role

Repressed by nanR (protein.P0A8W0). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39353|protein.P39353]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nanY; function=+
- `represses` <-- [[protein.P0A8W0|protein.P0A8W0]] `RegulonDB` `C` - regulator=NanR; target=nanY; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014027,ECOCYC:G7901,GeneID:948808`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4505287-4506405:+; feature_type=gene
