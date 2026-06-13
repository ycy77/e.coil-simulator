---
entity_id: "gene.b0537"
entity_type: "gene"
name: "intD"
source_database: "NCBI RefSeq"
source_id: "gene-b0537"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0537"
  - "intD"
---

# intD

`gene.b0537`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0537`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

intD (gene.b0537) is a gene entity. It encodes intD (protein.P24218). Encoded protein function: FUNCTION: Integrase from the cryptic lambdoid prophage DLP12. Integrase is necessary for integration of the phage into the host genome by site-specific recombination. In conjunction with excisionase, integrase is also necessary for excision of the prophage from the host genome. EcoCyc product frame: EG10507-MONOMER. EcoCyc synonyms: int. Genomic coordinates: 564815-565978. EcoCyc protein note: IntD is the predicted integrase of the cryptic lambdoid prophage DLP12 . intD can be transcribed in vivo. An intD insertion mutant grows at the same rate as wild type cells . Review:

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24218|protein.P24218]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=intD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001842,ECOCYC:EG10507,GeneID:947162`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:564815-565978:-; feature_type=gene
