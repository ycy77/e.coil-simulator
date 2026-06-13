---
entity_id: "gene.b4140"
entity_type: "gene"
name: "fxsA"
source_database: "NCBI RefSeq"
source_id: "gene-b4140"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4140"
  - "fxsA"
---

# fxsA

`gene.b4140`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4140`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fxsA (gene.b4140) is a gene entity. It encodes fxsA (protein.P37147). Encoded protein function: FUNCTION: Overexpression alleviates the exclusion of phage T7 in cells harboring the F plasmid. EcoCyc product frame: G7832-MONOMER. EcoCyc synonyms: yjeG. Genomic coordinates: 4368664-4369140. EcoCyc protein note: FxsA overproduction inhibits F exclusion of bacteriophage T7 . FxsA localizes to the inner membrane . A gain-of-function mutation in the fxsA promoter that causes fxsA overexpression results in resistance to coexpression of gene 10 from bacteriophage T7 with the pifA gene from the F plasmid . This gain-of-function mutation also results in resistance to coexpression of gene 1.2 from bacteriophage T7 with the pifA gene from the F plasmid . An fxsA null mutant is viable . Fxs: "F exclusion of bacteriophage T7" . Regulation has been described .

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37147|protein.P37147]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=fxsA; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013557,ECOCYC:G7832,GeneID:948657`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4368664-4369140:+; feature_type=gene
