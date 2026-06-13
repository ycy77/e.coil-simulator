---
entity_id: "gene.b1452"
entity_type: "gene"
name: "yncE"
source_database: "NCBI RefSeq"
source_id: "gene-b1452"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1452"
  - "yncE"
---

# yncE

`gene.b1452`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1452`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yncE (gene.b1452) is a gene entity. It encodes yncE (protein.P76116). Encoded protein function: Uncharacterized protein YncE EcoCyc product frame: G6763-MONOMER. Genomic coordinates: 1523307-1524368. EcoCyc protein note: YncE was hypothesized to be involved in iron acquisition . Processing of YncE, and thus presumably transport across the inner membrane, is SecB-dependent . YncE binds DNA with a preference for single-stranded DNA , and ATP binding increases the stability of the protein . A preliminary crystallographic structure has been reported , and crystal structures of the protein lacking the predicted signal sequence have been solved, showing that YncE adopts a seven-bladed β-propeller structure . A positively charged region near the central channel of the protein was expected to be involved in substrate binding; point mutants in these residues affect DNA binding . Sequence similarity suggested that YncE may contain β-barrel structure(s) . In a secB mutant, YncE aggregates in the cytoplasm. Localization of YncE to the periplasm was predicted by PSORT . Expression of yncE is repressed by the global iron regulator Fe2+-Fur .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), arcA (protein.P0A9Q1). Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76116|protein.P76116]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=yncE; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=yncE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004843,ECOCYC:G6763,GeneID:946006`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1523307-1524368:+; feature_type=gene
