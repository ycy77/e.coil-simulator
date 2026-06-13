---
entity_id: "gene.b1655"
entity_type: "gene"
name: "mepH"
source_database: "NCBI RefSeq"
source_id: "gene-b1655"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1655"
  - "mepH"
---

# mepH

`gene.b1655`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1655`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mepH (gene.b1655) is a gene entity. It encodes mepH (protein.P76190). Encoded protein function: FUNCTION: A murein DD-endopeptidase with specificity for D-Ala-meso-diaminopimelic acid (mDAP) cross-links. Its role is probably to cleave D-Ala-mDAP cross-links to allow insertion of new glycans and thus cell wall expansion. Functionally redundant with MepM and MepH. Partially suppresses an mepS disruption mutant. {ECO:0000269|PubMed:23062283}. EcoCyc product frame: G6892-MONOMER. EcoCyc synonyms: ydhO. Genomic coordinates: 1734435-1735250. EcoCyc protein note: Purified MepH is a murein DD-endopeptidase with specificity for D-ala-m-DAP (4→3) cross-links; the endopeptidase activity of MepH is associated with murein incorporation during cell growth; purified MepH has no LD carboxypeptidase activity . Purified MepH has weak hydrolytic activity on m-DAP-m-DAP (3→3) cross-links and, in contradiction of earlier results, also displays L,D-carboxypeptidase activity . An E. coli K-12 strain lacking all three murein endopeptidases MepH, G7147-MONOMER "MepS" and EG10013-MONOMER "MepM" exhibits extensive cell lysis and a terminal phenotype. Incorporation of labelled mDAP into the peptidoglycan sacculi is decreased by up to 80% in the triple deletion strain. Over-expression of any of the three genes from a plasmid allows the triple deletion mutant to grow normally...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76190|protein.P76190]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005533,ECOCYC:G6892,GeneID:945210`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1734435-1735250:+; feature_type=gene
