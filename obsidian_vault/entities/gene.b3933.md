---
entity_id: "gene.b3933"
entity_type: "gene"
name: "ftsN"
source_database: "NCBI RefSeq"
source_id: "gene-b3933"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3933"
  - "ftsN"
---

# ftsN

`gene.b3933`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3933`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ftsN (gene.b3933) is a gene entity. It encodes ftsN (protein.P29131). Encoded protein function: FUNCTION: Essential cell division protein that activates septal peptidoglycan synthesis and constriction of the cell. Acts on both sides of the membrane, via interaction with FtsA in the cytoplasm and interaction with the FtsQBL complex in the periplasm. These interactions may induce a conformational switch in both FtsA and FtsQBL, leading to septal peptidoglycan synthesis by FtsI and associated synthases (Probable) (PubMed:25496160). Required for full FtsI activity (PubMed:25496160). Required for recruitment of AmiC to the septal ring (PubMed:12787347). {ECO:0000269|PubMed:12787347, ECO:0000269|PubMed:25496160, ECO:0000305|PubMed:25496050, ECO:0000305|PubMed:25571948}. EcoCyc product frame: EG11529-MONOMER. EcoCyc synonyms: msgA. Genomic coordinates: 4122380-4123339. EcoCyc protein note: FtsN is an essential cell division protein present at 3000-6000 molecules per cell; inactivation of ftsN results in filamentation and cell death . FtsN contains a small N-terminal cytoplasmic domain, a membrane-spanning region and a large periplasmic C-terminal domain . FtsN localizes to the septum during division; the periplasmic domain of FtsN is sufficient for correct localization...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P29131|protein.P29131]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012850,ECOCYC:EG11529,GeneID:948428`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4122380-4123339:-; feature_type=gene
