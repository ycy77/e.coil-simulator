---
entity_id: "gene.b2171"
entity_type: "gene"
name: "yeiP"
source_database: "NCBI RefSeq"
source_id: "gene-b2171"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2171"
  - "yeiP"
---

# yeiP

`gene.b2171`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2171`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeiP (gene.b2171) is a gene entity. It encodes efpL (protein.P0A6N8). Encoded protein function: FUNCTION: Involved in peptide bond synthesis. Alleviates ribosome stalling at di-proline-containing sequences; in rare cases stalled nascent peptides lacking di-Pro can also be rescued. Rescues stalling of the MgtL leader peptide, which has 4 non-consecutive Pro residues in its first 9 residues. Its function partially overlaps with EF-P and UUP. Can also cause translational pausing, probably by blocking tRNA translocation to the E-site. Acts as a sensor for the metabolic state of the cell via lysine acylation (PubMed:39622818). A tRNA(Pro) in the P-site and guanosine in the first position of the E-site codon promote EfpL (and EF-P) binding to the ribosome (Probable) (PubMed:39622818). {ECO:0000269|PubMed:39622818, ECO:0000305|PubMed:39622818}. EcoCyc product frame: EG12035-MONOMER. EcoCyc synonyms: yeiP. Genomic coordinates: 2265450-2266022. EcoCyc protein note: EfpL, a paralog of EG12099-MONOMER, is also involved in translational stress response through rescuing ribosome stalling at polyproline (XP(P)X)-containing proteins and acts as a sensor for the metabolic state of the cell via lysine acylation . A third protein, UUP-MONOMER, is also involved in rescuing polyproline-dependent ribosome stalling in E. coli...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6N8|protein.P0A6N8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007187,ECOCYC:EG12035,GeneID:946674`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2265450-2266022:+; feature_type=gene
