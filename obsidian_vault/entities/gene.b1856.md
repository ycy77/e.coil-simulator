---
entity_id: "gene.b1856"
entity_type: "gene"
name: "mepM"
source_database: "NCBI RefSeq"
source_id: "gene-b1856"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1856"
  - "mepM"
---

# mepM

`gene.b1856`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1856`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mepM (gene.b1856) is a gene entity. It encodes mepM (protein.P0AFS9). Encoded protein function: FUNCTION: A murein DD-endopeptidase with specificity for D-Ala-meso-diaminopimelic acid (mDAP) cross-links. Its role is probably to cleave D-Ala-mDAP cross-links to allow insertion of new glycans and thus cell wall expansion. Functionally redundant with MepM and MepH. Partially suppresses an mepS disruption mutant. {ECO:0000269|PubMed:23062283}. EcoCyc product frame: EG10013-MONOMER. EcoCyc synonyms: yebA. Genomic coordinates: 1940313-1941635. EcoCyc protein note: Purified MepM is a dual specificity murein endopeptidase which cleaves both D-ala-m-DAP (4 → 3) and m-DAP-mDAP (3 → 3) cross-links with similar efficacy; the endopeptidase activity of MepM is associated with murein incorporation during cell growth. MepM is a metalloendopeptidase - activity is dependent on the presence of a divalent metal ion . In addition to promoting cell elongation, MepM influences the cell division process; elevated activity of the endopeptidases which promote cell elongation interferes with the activation of septal PG biogenesis by the divisome . An E. coli K-12 strain lacking all three murein endopeptidases MepM, G7147-MONOMER "MepS" and G6892-MONOMER "MepH" exhibits extensive cell lysis and a terminal phenotype...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFS9|protein.P0AFS9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006189,ECOCYC:EG10013,GeneID:946376`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1940313-1941635:-; feature_type=gene
