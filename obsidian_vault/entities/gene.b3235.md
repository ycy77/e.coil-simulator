---
entity_id: "gene.b3235"
entity_type: "gene"
name: "degS"
source_database: "NCBI RefSeq"
source_id: "gene-b3235"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3235"
  - "degS"
---

# degS

`gene.b3235`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3235`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

degS (gene.b3235) is a gene entity. It encodes degS (protein.P0AEE3). Encoded protein function: FUNCTION: A site-1 protease (S1P) that cleaves the peptide bond between 'Val-148' and 'Ser-149' in RseA. Part of a regulated intramembrane proteolysis (RIP) cascade. When heat shock or other environmental stresses disrupt protein folding in the periplasm, DegS senses the accumulation of unassembled outer membrane porins (OMP) and then initiates RseA (anti sigma-E factor) degradation by cleaving its periplasmic domain, making it a substrate for subsequent cleavage by RseP. This cascade ultimately leads to the sigma-E-driven expression of a variety of factors dealing with folding stress in the periplasm and OMP assembly. Required for basal and stress-induced degradation of RseA. {ECO:0000269|PubMed:10500101, ECO:0000269|PubMed:11442831, ECO:0000269|PubMed:12183368, ECO:0000269|PubMed:12183369, ECO:0000269|PubMed:12679035, ECO:0000269|PubMed:17360428, ECO:0000269|PubMed:17938245, ECO:0000269|PubMed:18945679, ECO:0000269|PubMed:19695325, ECO:0000269|PubMed:19706448}. EcoCyc product frame: EG11652-MONOMER. EcoCyc synonyms: hhoB, htrH. Genomic coordinates: 3382200-3383267.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEE3|protein.P0AEE3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=degS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010611,ECOCYC:EG11652,GeneID:947865`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3382200-3383267:+; feature_type=gene
