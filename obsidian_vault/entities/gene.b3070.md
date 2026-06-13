---
entity_id: "gene.b3070"
entity_type: "gene"
name: "nfeF"
source_database: "NCBI RefSeq"
source_id: "gene-b3070"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3070"
  - "nfeF"
---

# nfeF

`gene.b3070`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3070`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nfeF (gene.b3070) is a gene entity. It encodes yqjH (protein.Q46871). Encoded protein function: FUNCTION: Plays a role in iron homeostasis under excess nickel conditions. {ECO:0000269|PubMed:21097627}. EcoCyc product frame: G7593-MONOMER. EcoCyc synonyms: yqjH. Genomic coordinates: 3215727-3216491. EcoCyc protein note: NfeF is an NADPH-dependent ferric reductase; the enzyme contains FAD that is used as a cofactor rather than a substrate. The enzyme is only weakly active with purified ferric enterobactin ; the hydrolyzed ferric enterobactin complex is the most efficient of the tested substrates . Reports disagree on whether the FAD cofactor is covalently bound to a cysteine sidechain via a thioether bond or not covalently attached . A preliminary report of crystallization and structure analysis of the NfeF protein has appeared. NfeF is structurally related to the NAD(P)H:flavin oxidoreductase superfamily . The reaction mechanism of NfeF has been investigated in detail; a transient flavosemiquinone is involved in the single-electron transfer in a double-displacement (ping-pong)-type reaction. The K55 and R130 residues are required for substrate binding and enzymatic activity. While the enzyme has high affinity for the intact ferric enterobactin, the catalytic turnover rate is much slower than for the hydrolyzed ferric triscatecholate...

## Biological Role

Repressed by fur (protein.P0A9A9), yqjI (protein.P64588). Activated by ygaV (protein.P77295).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46871|protein.Q46871]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P77295|protein.P77295]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=nfeF; function=-
- `represses` <-- [[protein.P64588|protein.P64588]] `RegulonDB` `C` - regulator=NfeR; target=nfeF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010079,ECOCYC:G7593,GeneID:947582`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3215727-3216491:-; feature_type=gene
