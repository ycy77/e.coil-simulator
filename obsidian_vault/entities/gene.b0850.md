---
entity_id: "gene.b0850"
entity_type: "gene"
name: "ybjC"
source_database: "NCBI RefSeq"
source_id: "gene-b0850"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0850"
  - "ybjC"
---

# ybjC

`gene.b0850`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0850`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybjC (gene.b0850) is a gene entity. It encodes ybjC (protein.P46119). Encoded protein function: Uncharacterized protein YbjC EcoCyc product frame: EG12842-MONOMER. Genomic coordinates: 890913-891200. EcoCyc protein note: ybjC expression is down regulated in an E. coli K-12 strain engineered for increased tolerance to n-butanol; a ΔybjC strain has increased n-butanol tolerance . A YbjC-GFP fusion protein localizes to the membrane region . The nfsA and ybjC genes are co-transcribed; transcription is induced by paraquat and appears to be directly regulated by SoxS .

## Biological Role

Repressed by oxyR (protein.P0ACQ4). Activated by rpoD (protein.P00579), soxS (protein.P0A9E2), marA (protein.P0ACH5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46119|protein.P46119]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ybjC; function=+
- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=ybjC; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=ybjC; function=+
- `represses` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=ybjC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002898,ECOCYC:EG12842,GeneID:945481`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:890913-891200:+; feature_type=gene
