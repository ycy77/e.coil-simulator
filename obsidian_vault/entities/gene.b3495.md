---
entity_id: "gene.b3495"
entity_type: "gene"
name: "uspA"
source_database: "NCBI RefSeq"
source_id: "gene-b3495"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3495"
  - "uspA"
---

# uspA

`gene.b3495`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3495`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uspA (gene.b3495) is a gene entity. It encodes uspA (protein.P0AED0). Encoded protein function: FUNCTION: Required for resistance to DNA-damaging agents. EcoCyc product frame: EG11390-MONOMER. Genomic coordinates: 3640111-3640545.

## Biological Role

Repressed by fadR (protein.P0A8V6), nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AED0|protein.P0AED0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=uspA; function=+
- `represses` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `C` - regulator=FadR; target=uspA; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=uspA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011414,ECOCYC:EG11390,GeneID:948007`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3640111-3640545:+; feature_type=gene
