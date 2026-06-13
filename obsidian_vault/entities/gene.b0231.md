---
entity_id: "gene.b0231"
entity_type: "gene"
name: "dinB"
source_database: "NCBI RefSeq"
source_id: "gene-b0231"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0231"
  - "dinB"
---

# dinB

`gene.b0231`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0231`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dinB (gene.b0231) is a gene entity. It encodes dinB (protein.Q47155). Encoded protein function: FUNCTION: Poorly processive, error-prone DNA polymerase involved in translesion repair and untargeted mutagenesis (PubMed:10488344, PubMed:10801133). Copies undamaged DNA at stalled replication forks, which arise in vivo from mismatched or misaligned primer ends. These misaligned primers can be extended by Pol IV. Exhibits no 3'-5' exonuclease (proofreading) activity (PubMed:10488344). Overexpression of Pol IV results in increased frameshift mutagenesis. It is required for stationary-phase adaptive mutation, which provides the bacterium with flexibility in dealing with environmental stress, enhancing long-term survival and evolutionary fitness. Not seen to be involved in translesion snythesis even when stimulated by the beta slding-clamp and clamp-loading complex, which do however increase non-targeted DNA polymerase efficiency 3,000-fold, may be due to targeting to stalled replication forks on nondamaged DNA (PubMed:10801133, PubMed:16168375). Involved in translesional synthesis, in conjunction with the beta clamp from PolIII (PubMed:14592985, PubMed:14729336)...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47155|protein.Q47155]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000789,ECOCYC:G6115,GeneID:944922`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:250898-251953:+; feature_type=gene
