---
entity_id: "gene.b0478"
entity_type: "gene"
name: "ybaL"
source_database: "NCBI RefSeq"
source_id: "gene-b0478"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0478"
  - "ybaL"
---

# ybaL

`gene.b0478`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0478`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybaL (gene.b0478) is a gene entity. It encodes ybaL (protein.P39830). Encoded protein function: Putative cation/proton antiporter YbaL EcoCyc product frame: YBAL-MONOMER. EcoCyc synonyms: ylaA. Genomic coordinates: 501562-503238. EcoCyc protein note: The YbaL protein is an uncharacterised member of the CPA2 family of monovalent cation:proton antiporters . ybaL has supercoiling-dependent transcription, which is associated with the osmotic stress response and acts through rpoS . In experimental evolution experiments requiring adaptation of E. coli to high growth temperature (45.9°C or 42.2°C), ybaL is frequently mutated .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39830|protein.P39830]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ybaL; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001658,ECOCYC:EG12623,GeneID:946576`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:501562-503238:-; feature_type=gene
