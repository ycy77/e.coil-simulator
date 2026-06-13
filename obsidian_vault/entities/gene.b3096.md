---
entity_id: "gene.b3096"
entity_type: "gene"
name: "mzrA"
source_database: "NCBI RefSeq"
source_id: "gene-b3096"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3096"
  - "mzrA"
---

# mzrA

`gene.b3096`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3096`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mzrA (gene.b3096) is a gene entity. It encodes mzrA (protein.P42615). Encoded protein function: FUNCTION: Modulates the activity of the EnvZ/OmpR two-component regulatory system, probably by directly modulating EnvZ enzymatic activity and increasing stability of phosphorylated OmpR. Links the two-component systems CpxA/CpxR and EnvZ/OmpR. {ECO:0000255|HAMAP-Rule:MF_00904, ECO:0000269|PubMed:19432797, ECO:0000269|PubMed:20889743}. EcoCyc product frame: G7610-MONOMER. EcoCyc synonyms: ecfM, yqjB. Genomic coordinates: 3248439-3248822. EcoCyc protein note: The MzrA protein functions to regulate the EnvZ/OmpR osmoregulatory two-component signal transduction system. Overexpression of mzrA suppresses the conditionally lethal phenotype of a degP bamB double deletion mutant and results in reduced levels of OmpF, LamB and to a smaller extent MalE. This effect was OmpR and EnvZ dependent . MzrA interacts with EnvZ in vivo . Constitutively activated CpxA/CpxR strains regulate EnvZ/OmpR in an MzrA dependent manner suggesting that MzrA links these two signal transduction systems MzrA is an inner membrane protein with its C-terminus exposed to the periplasm and its N-terminus exposed to the cytoplasm . Transcription of mzrA is regulated by RpoE (σE) . MzrA: "modulator of EnvZ and OmpR A"

## Biological Role

Activated by rpoD (protein.P00579), cpxR (protein.P0AE88), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42615|protein.P42615]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mzrA; function=+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=mzrA; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=mzrA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010183,ECOCYC:G7610,GeneID:947619`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3248439-3248822:+; feature_type=gene
