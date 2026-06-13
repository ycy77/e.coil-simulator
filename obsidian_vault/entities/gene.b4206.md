---
entity_id: "gene.b4206"
entity_type: "gene"
name: "ytfB"
source_database: "NCBI RefSeq"
source_id: "gene-b4206"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4206"
  - "ytfB"
---

# ytfB

`gene.b4206`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4206`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ytfB (gene.b4206) is a gene entity. It encodes ytfB (protein.P39310). Encoded protein function: FUNCTION: Cell division protein whose function is related to the generation of a transient cell wall structure. Function is linked to the late stages of cell division. {ECO:0000269|PubMed:29686141}. EcoCyc product frame: G7864-MONOMER. Genomic coordinates: 4428079-4428717. EcoCyc protein note: Overproduction of YtfB causes a filamentous phenotype . YtfB localizes to the septal ring; YtfB is recruited to the septal ring early and requires FtsZ but not later division proteins for septal localization. Cells lacking YtfB show no visible shape or growth defects however ΔytfB ΔdedD mutants form filaments . YtfB contains a C-terminal OapA (opacity-associated protein A) domain; the isolated and labelled OapA domain localizes to sites of septal constriction; the purified OapA domain binds peptidoglycan; a YtfB variant lacking the OapA domain localizes to the septal ring . YtfB is predicted to be a bitopic inner membrane protein .

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39310|protein.P39310]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ytfB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013756,ECOCYC:G7864,GeneID:948727`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4428079-4428717:-; feature_type=gene
