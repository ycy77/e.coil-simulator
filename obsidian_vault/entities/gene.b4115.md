---
entity_id: "gene.b4115"
entity_type: "gene"
name: "adiC"
source_database: "NCBI RefSeq"
source_id: "gene-b4115"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4115"
  - "adiC"
---

# adiC

`gene.b4115`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4115`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

adiC (gene.b4115) is a gene entity. It encodes adiC (protein.P60061). Encoded protein function: FUNCTION: Major component of the acid-resistance (AR) system allowing enteric pathogens to survive the acidic environment in the stomach (Probable). Exchanges extracellular arginine for its intracellular decarboxylation product agmatine (Agm) thereby expelling intracellular protons (PubMed:12867448, PubMed:14594828, PubMed:19578361, PubMed:21368142). Probably undergoes several conformational states in order to translocate the substrate across the membrane; keeps the substrate accessible to only 1 side of the membrane at a time by opening and closing 3 membrane-internal gates (Probable). {ECO:0000269|PubMed:12867448, ECO:0000269|PubMed:14594828, ECO:0000269|PubMed:19578361, ECO:0000269|PubMed:21368142, ECO:0000305|PubMed:14594828, ECO:0000305|PubMed:21368142}. EcoCyc product frame: YJDE-MONOMER. EcoCyc synonyms: yjdD, yjdE. Genomic coordinates: 4335694-4337031.

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by DNA-binding transcriptional activator AdiY (complex.ecocyc.CPLX0-13978), DNA-binding transcriptional dual regulator TorR-phosphorylated (protein.ecocyc.PHOSPHO-TORR).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60061|protein.P60061]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-13978|complex.ecocyc.CPLX0-13978]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.ecocyc.PHOSPHO-TORR|protein.ecocyc.PHOSPHO-TORR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013473,ECOCYC:EG12462,GeneID:948628`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4335694-4337031:-; feature_type=gene
