---
entity_id: "gene.b1696"
entity_type: "gene"
name: "ydiP"
source_database: "NCBI RefSeq"
source_id: "gene-b1696"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1696"
  - "ydiP"
---

# ydiP

`gene.b1696`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1696`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydiP (gene.b1696) is a gene entity. It encodes ydiP (protein.P77402). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YdiP EcoCyc product frame: G6919-MONOMER. Genomic coordinates: 1778390-1779301. EcoCyc protein note: YdiP is an AraC-type transcription factor , involved in the cold shock response . It contains a helix-turn-helix motif to bind DNA in its C-terminal domain . YdiP DNA-binding activity was probed in vivo in glucose M9 minimal medium through chromatin immunoprecipitation assays (ChIP-exo) . It was predicted that this protein regulates genes related to metabolism . However, the effect of YdiP on the transcription of any gene has not yet been demonstrated . In LB medium, the YdiP protein abundance was increased after 2 h of shifting to cold shock at 15°C relative to activity at 37°C . At 15°C but not at 37°C, YdiP binds with CspA, CspB, CspE, CspG, and CspI proteins in rich medium and with CspE in minimal medium . A ydiP knockout mutant showed impaired growth at 15°C but not at 37°C compared to wild type . This defect was exacerbated when cspABEGI was also deleted . YdiP protein abundance was increased after adaptation to 10°C relative to that at 37°C . ydiP transcript level was increased 4 h after a shift to 15°C relative to abundance at 37°C...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77402|protein.P77402]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ydiP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005660,ECOCYC:G6919,GeneID:945095`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1778390-1779301:-; feature_type=gene
