---
entity_id: "gene.b1347"
entity_type: "gene"
name: "rcbA"
source_database: "NCBI RefSeq"
source_id: "gene-b1347"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1347"
  - "rcbA"
---

# rcbA

`gene.b1347`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1347`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rcbA (gene.b1347) is a gene entity. It encodes rcbA (protein.P33230). Encoded protein function: FUNCTION: Helps to maintain the integrity of the chromosome by lowering the steady-state level of double strand breaks (PubMed:22343303). This region of DNA acts as an antitoxin to toxin RalR, a DNase, but it seems to be sRNA RalA that has the antitoxin activity and not this putative protein. Therefore the identity of this as a protein-coding gene has been cast into doubt (PubMed:24748661). {ECO:0000269|PubMed:22343303, ECO:0000269|PubMed:24748661}. EcoCyc product frame: EG11901-MONOMER. EcoCyc synonyms: ydaC. Genomic coordinates: 1413531-1413740. EcoCyc protein note: An rcbA deletion mutant has an increased level of chromosomal double strand breaks (DSB) . Overexpression of rcbA from a plasmid suppresses the lethal effect caused by the induced expression of the chromosomal replication initiation protein, DnaA, in DSB repair-defective mutants . Overproduction of DnaA is toxic in an rcbA deletion mutant but not in the isogenic rcbA+ strain . The mechanism of action of RcbA is not clear. Overexpression of rcbA increases fitness as well as resistance to toxic compounds and antibiotics, including erythromycin . It is possible that the RcbA phenotype is due to the expression of G0-16600 RalA, a small RNA antitoxin encoded on the opposite strand...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33230|protein.P33230]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004522,ECOCYC:EG11901,GeneID:947504`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1413531-1413740:-; feature_type=gene
