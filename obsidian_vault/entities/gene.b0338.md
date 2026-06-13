---
entity_id: "gene.b0338"
entity_type: "gene"
name: "cynR"
source_database: "NCBI RefSeq"
source_id: "gene-b0338"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0338"
  - "cynR"
---

# cynR

`gene.b0338`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0338`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cynR (gene.b0338) is a gene entity. It encodes cynR (protein.P27111). Encoded protein function: FUNCTION: Positively regulates the cynTSX operon, and negatively regulates its own transcription. Binds specifically to the cynR-cynTSX intergenic region. {ECO:0000269|PubMed:1592818}. EcoCyc product frame: PD00291. Genomic coordinates: 357791-358690.

## Biological Role

Repressed by cynR (protein.P27111), nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27111|protein.P27111]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cynR; function=+
- `represses` <-- [[protein.P27111|protein.P27111]] `RegulonDB` `S` - regulator=CynR; target=cynR; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cynR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001165,ECOCYC:EG11421,GeneID:945001`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:357791-358690:-; feature_type=gene
