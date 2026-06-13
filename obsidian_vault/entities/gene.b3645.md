---
entity_id: "gene.b3645"
entity_type: "gene"
name: "dinD"
source_database: "NCBI RefSeq"
source_id: "gene-b3645"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3645"
  - "dinD"
---

# dinD

`gene.b3645`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3645`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dinD (gene.b3645) is a gene entity. It encodes dinD (protein.P23840). Encoded protein function: DNA damage-inducible protein D EcoCyc product frame: EG11193-MONOMER. EcoCyc synonyms: pcsA, yicD. Genomic coordinates: 3817760-3818584. EcoCyc protein note: dinD expression increases in response to agents that induce the SOS response such as the DNA damaging agent CPD-17518, and UV treatment . Induction also occurs in response to bile salts and hydrogen peroxide . Its expression fails to respond to DNA damage in recA and lexA mutants . dinD expression is repressed in uninduced cells by LexA . Expression of dinD is reduced upon photoreactivation after UV induction of the SOS response, identifying the cyclobutane pyrimidine dimer as the possible primary inducer of SOS response genes upon UV exposure . A specific dinD mutant was shown to have a cold-sensitive phenotype, forming long filaments with large nucleoid masses in the central region . The mutation also leads to the induction of the SOS response at low temperature even without DNA damaging agents . This cold-sensitivity is suppressed in recA and lexA mutants , as well as by multicopy expression of lexA, dinG, and dinI . Deletion of dinD resulted in no discernible phenotype .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23840|protein.P23840]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011918,ECOCYC:EG11193,GeneID:948153`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3817760-3818584:+; feature_type=gene
