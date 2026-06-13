---
entity_id: "gene.b3922"
entity_type: "gene"
name: "yiiS"
source_database: "NCBI RefSeq"
source_id: "gene-b3922"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3922"
  - "yiiS"
---

# yiiS

`gene.b3922`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3922`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yiiS (gene.b3922) is a gene entity. It encodes yiiS (protein.P32162). Encoded protein function: UPF0381 protein YiiS EcoCyc product frame: EG11876-MONOMER. Genomic coordinates: 4112967-4113266. EcoCyc protein note: The yiiS gene has an RpoE-dependent promoter . In an enterotoxigenic E. coli strain, yiiS transcription is regulated by Rns .

## Biological Role

Activated by rpoE (protein.P0AGB6), ydeO (protein.P76135).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32162|protein.P32162]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yiiS; function=+
- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=yiiS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012813,ECOCYC:EG11876,GeneID:948416`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4112967-4113266:+; feature_type=gene
