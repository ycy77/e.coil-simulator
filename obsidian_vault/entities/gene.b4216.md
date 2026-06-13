---
entity_id: "gene.b4216"
entity_type: "gene"
name: "ytfJ"
source_database: "NCBI RefSeq"
source_id: "gene-b4216"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4216"
  - "ytfJ"
---

# ytfJ

`gene.b4216`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4216`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ytfJ (gene.b4216) is a gene entity. It encodes ytfJ (protein.P39187). Encoded protein function: Uncharacterized protein YtfJ EcoCyc product frame: G7871-MONOMER. EcoCyc synonyms: ecfJ. Genomic coordinates: 4438708-4439262. EcoCyc protein note: Transcription of ytfJ is regulated by RpoE (σE). A ytfJ null mutant shows temperature-sensitive growth above 43°C . YtfJ expression is negatively regulated by the small RNA Spot 42 . EcfJ: "extracytoplasmic function"

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0), rpoE (protein.P0AGB6), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39187|protein.P39187]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=ytfJ; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ytfJ; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013792,ECOCYC:G7871,GeneID:948737`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4438708-4439262:-; feature_type=gene
