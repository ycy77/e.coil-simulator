---
entity_id: "gene.b3923"
entity_type: "gene"
name: "uspD"
source_database: "NCBI RefSeq"
source_id: "gene-b3923"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3923"
  - "uspD"
---

# uspD

`gene.b3923`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3923`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uspD (gene.b3923) is a gene entity. It encodes uspD (protein.P0AAB8). Encoded protein function: FUNCTION: Required for resistance to DNA-damaging agents. {ECO:0000269|PubMed:11849540}. EcoCyc product frame: EG11877-MONOMER. EcoCyc synonyms: yiiT. Genomic coordinates: 4113293-4113721.

## Biological Role

Activated by rpoE (protein.P0AGB6), ydeO (protein.P76135).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAB8|protein.P0AAB8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=uspD; function=+
- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=uspD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012816,ECOCYC:EG11877,GeneID:948415`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4113293-4113721:+; feature_type=gene
