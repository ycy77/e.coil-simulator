---
entity_id: "gene.b2767"
entity_type: "gene"
name: "ygcO"
source_database: "NCBI RefSeq"
source_id: "gene-b2767"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2767"
  - "ygcO"
---

# ygcO

`gene.b2767`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2767`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygcO (gene.b2767) is a gene entity. It encodes ygcO (protein.Q46905). Encoded protein function: FUNCTION: Could be a 3Fe-4S cluster-containing protein. Probably participates in a redox process with YgcN, YgcQ and YgcR. EcoCyc product frame: G7433-MONOMER. Genomic coordinates: 2893919-2894179. EcoCyc protein note: A ygcO mutant has reduced ability to act as a recipient in cell-to-cell transfer of a plasmid and shows reduced transformation efficiency using the CaCl2 transformation method .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46905|protein.Q46905]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ygcO; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009072,ECOCYC:G7433,GeneID:945120`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2893919-2894179:+; feature_type=gene
