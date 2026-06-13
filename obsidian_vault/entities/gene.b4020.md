---
entity_id: "gene.b4020"
entity_type: "gene"
name: "yjbB"
source_database: "NCBI RefSeq"
source_id: "gene-b4020"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4020"
  - "yjbB"
---

# yjbB

`gene.b4020`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4020`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjbB (gene.b4020) is a gene entity. It encodes yjbB (protein.P0AF43). Encoded protein function: FUNCTION: Might be involved in phosphate export (PubMed:21488939). Overproduction of YjbB reduces the elevated levels of polyphosphate (polyP) in a phoU mutant that accumulates 1000-fold higher levels of polyP than the wild type, suggesting that YjbB exports excess intracellular phosphate (Pi) in the phoU mutant and thus reduces the levels of polyP (PubMed:21488939). {ECO:0000269|PubMed:21488939}. EcoCyc product frame: EG11919-MONOMER. Genomic coordinates: 4227731-4229362. EcoCyc protein note: YjbB is a putative inorganic phosphate (Pi) export protein. Overproduction of YjbB reduces the increased levels of polyphosphate that accumulate in a phoU mutant . Overproduction of YjbB increases the rate of Pi export when a phoA, yjbB, pitA, pitB, phnC, pstSCAB-phoU mutant strain is grown on glycerol-3-phosphate as the sole carbon source . YjbB contains an N-terminal Na+/Pi cotransporter domain .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF43|protein.P0AF43]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yjbB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013143,ECOCYC:EG11919,GeneID:948521`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4227731-4229362:+; feature_type=gene
