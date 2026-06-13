---
entity_id: "gene.b2177"
entity_type: "gene"
name: "yejA"
source_database: "NCBI RefSeq"
source_id: "gene-b2177"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2177"
  - "yejA"
---

# yejA

`gene.b2177`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2177`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yejA (gene.b2177) is a gene entity. It encodes yejA (protein.P33913). Encoded protein function: FUNCTION: Part of the ABC transporter complex YejABEF involved in the uptake of oligopeptides (PubMed:17873039, PubMed:21602342, PubMed:39739799). The transporter is involved in the uptake of microcin C (McC), a natural peptide-nucleotide antibiotic that targets aspartyl-tRNA synthetase (PubMed:17873039). It can transport synthetic McC analogs containing a minimal peptide chain length of 6 amino acids and an N-terminal formyl-methionyl-arginyl sequence (PubMed:21602342). The preferred peptide length for YejABEF-mediated uptake is more than 7 but less than 13 amino acids (PubMed:21602342). This subunit is the solute binding protein of the YejABEF transporter (PubMed:38334478, PubMed:39739799). It binds the formylated heptapeptide moiety of McC, whereas the 3-aminopropyl adenylate moiety of McC is not critical for ligand recognition (PubMed:39739799). YejA can accommodate formylated heptapeptides conjugated to molecules with diverse structures (PubMed:39739799). It selectively binds in vitro self-derived peptides containing a core motif of EPRYAFN (PubMed:38334478). The physiological significance of this 'auto-binding' is not clear, but it may have a function in the sensing of periplasmic or membrane stress (PubMed:38334478)...

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33913|protein.P33913]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007206,ECOCYC:EG12037,GeneID:946675`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2272364-2274178:+; feature_type=gene
