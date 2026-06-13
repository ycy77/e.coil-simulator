---
entity_id: "gene.b1447"
entity_type: "gene"
name: "ydcZ"
source_database: "NCBI RefSeq"
source_id: "gene-b1447"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1447"
  - "ydcZ"
---

# ydcZ

`gene.b1447`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1447`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydcZ (gene.b1447) is a gene entity. It encodes ydcZ (protein.P76111). Encoded protein function: Inner membrane protein YdcZ EcoCyc product frame: G6758-MONOMER. Genomic coordinates: 1517882-1518331. EcoCyc protein note: YdcZ is predicted to be an inner membrane protein with five transmembrane domains; experimental topology analysis suggests the C terminus is located in the cytoplasm . YdcZ appears to be required for normal swarming, but not swimming motility . In the Transporter Classification Database , YdcZ is an uncharacterized member of the Drug/Metabolite Transporter (DMT) superfamily. A ΔydcZ strain shows ability to take up membrane-permeable, cationic fluorescent dyes and increased sensitivity to CPD0-2336 .

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76111|protein.P76111]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ydcZ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004823,ECOCYC:G6758,GeneID:946008`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1517882-1518331:-; feature_type=gene
