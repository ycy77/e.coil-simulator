---
entity_id: "gene.b2180"
entity_type: "gene"
name: "yejF"
source_database: "NCBI RefSeq"
source_id: "gene-b2180"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2180"
  - "yejF"
---

# yejF

`gene.b2180`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2180`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yejF (gene.b2180) is a gene entity. It encodes yejF (protein.P33916). Encoded protein function: FUNCTION: Part of the ABC transporter complex YejABEF involved in the uptake of oligopeptides (PubMed:17873039, PubMed:21602342). The transporter is involved in the uptake of microcin C (McC), a natural peptide-nucleotide antibiotic that targets aspartyl-tRNA synthetase (PubMed:17873039). It can transport synthetic McC analogs containing a minimal peptide chain length of 6 amino acids and an N-terminal formyl-methionyl-arginyl sequence (PubMed:21602342). The preferred peptide length for YejABEF-mediated uptake is more than 7 but less than 13 amino acids (PubMed:21602342). This subunit is responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:17873039, ECO:0000269|PubMed:21602342, ECO:0000305}. EcoCyc product frame: YEJF-MONOMER. Genomic coordinates: 2276300-2277889. EcoCyc protein note: YejF is the ATP-binding subunit of a putative oligopeptide uptake system; YejF contains signature motifs conserved in ATP-binding cassette (ABC) domains; YejF contains an ABC-ABC domain .

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33916|protein.P33916]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007212,ECOCYC:EG12041,GeneID:946689`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2276300-2277889:+; feature_type=gene
