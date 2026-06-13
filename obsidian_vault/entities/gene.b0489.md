---
entity_id: "gene.b0489"
entity_type: "gene"
name: "qmcA"
source_database: "NCBI RefSeq"
source_id: "gene-b0489"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0489"
  - "qmcA"
---

# qmcA

`gene.b0489`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0489`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

qmcA (gene.b0489) is a gene entity. It encodes qmcA (protein.P0AA53). Encoded protein function: FUNCTION: Identified as a multi-copy suppressor of an FtsH/HtpX protease double disruption mutant. May play a role in the quality control of integral membrane proteins. EcoCyc product frame: G6265-MONOMER. EcoCyc synonyms: ybbK. Genomic coordinates: 514856-515773. EcoCyc protein note: QmcA is an integral inner membrane protein with a large cytoplasmic C-terminal domain; QmcA is a member of the prohibitin homology (PHB) domain family . Overexpression of qmcA suppresses the temperature sensitive growth defect of a ΔftsH Δ htpX double deletion mutant; plasmids carrying qmcA plus the downstream ORF ybbJ, show a stronger suppression activity than those carrying only qmcA; qmcA is non-essential under normal growth conditions . Sedimentation analysis suggests QmcA forms an oligomeric complex; affinity chromatography suggests a physical interaction between QmcA and FtsH . QmcA is a prokaryotic member of the stomatin, prohibitin, flotillin, and HflK/C (SPFH) protein superfamily ; SPFH domain proteins localize in eukaryotic lipid rafts and the function and localization of E. coli SPFH proteins, including QmcA has been investigated (see also ). QmcA: "quality control-related membrane complex"

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA53|protein.P0AA53]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001697,ECOCYC:G6265,GeneID:947257`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:514856-515773:-; feature_type=gene
