---
entity_id: "gene.b2007"
entity_type: "gene"
name: "tmaR"
source_database: "NCBI RefSeq"
source_id: "gene-b2007"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2007"
  - "tmaR"
---

# tmaR

`gene.b2007`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2007`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tmaR (gene.b2007) is a gene entity. It encodes tmaR (protein.P0A8M6). Encoded protein function: FUNCTION: Pole-localizer protein involved in the regulation of several cellular processes (PubMed:33376208, PubMed:36577380, PubMed:37934665). Regulated processes include sugar metabolism, cell motility and small RNA-mediated regulation (PubMed:33376208, PubMed:36577380, PubMed:37934665). TmaR controls the subcellular localization and the activity of PtsI, the general PTS system enzyme I (EI), by polar sequestration and release of PtsI (PubMed:33376208). Polar sequestration of PtsI restricts its activity, thus regulating sugar metabolism and enabling cell survival in mild acidic conditions (PubMed:33376208). TmaR does not affect localization of the phosphocarrier protein HPr (PubMed:33376208). It also plays a central role in cell motility (PubMed:37934665). It controls flagella production and, thus, cell motility and biofilm formation, by forming condensates that protect and stabilize flagella related transcripts at the poles (PubMed:37934665). In addition, TmaR affects small RNA-mediated regulation by recruiting the RNA-binding protein Hfq to the poles during certain stress conditions (PubMed:36577380). It plays a crucial role in Hfq condensation (PubMed:36577380). {ECO:0000269|PubMed:33376208, ECO:0000269|PubMed:36577380, ECO:0000269|PubMed:37934665}...

## Biological Role

Activated by DNA-binding transcriptional dual regulator Cra (complex.ecocyc.PC00061), cra (protein.P0ACP1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8M6|protein.P0A8M6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.PC00061|complex.ecocyc.PC00061]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=tmaR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006663,ECOCYC:G7087,GeneID:946541`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2079032-2079361:-; feature_type=gene
