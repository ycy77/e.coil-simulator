---
entity_id: "gene.b1494"
entity_type: "gene"
name: "pqqL"
source_database: "NCBI RefSeq"
source_id: "gene-b1494"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1494"
  - "pqqL"
---

# pqqL

`gene.b1494`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1494`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pqqL (gene.b1494) is a gene entity. It encodes pqqL (protein.P31828). Encoded protein function: Probable zinc protease PqqL (EC 3.4.24.-) EcoCyc product frame: EG11744-MONOMER. EcoCyc synonyms: pqqM, pqqE, yddC. Genomic coordinates: 1572407-1575202. EcoCyc protein note: PqqL is a periplasmic protein; a 26 residue signal peptide is cleaved in vivo. Purified recombinant PqqL, crystallized in the absence of substrate, contains two M16 protease domains each of which forms one half of an extended 'clam-shell like' structure; the N-terminal domain contains a putative zinc ion in the protease active site. PqqL is flexible in solution. Purified PqqL cleaves a small subset of peptides within a combinatorial peptide library; it does not show proteolytic activity towards human ferredoxins and globins, or plant ferredoxin . pqqL is located in a 3 gene cluster (yddA-yddB-ppqL) which may represent a 3-component iron-uptake system . Distant homologs (fusD, fusA and fusC respectively) encode a ferredoxin uptake system (Fus) in plant pathogenic Pectobacterium spp. . pqqL expression increases under iron-limiting conditions; PqqL does not support growth during iron limitation in LB media but may have a niche specific role in iron acquisition from a distinct protein substrate...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31828|protein.P31828]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004979,ECOCYC:EG11744,GeneID:946059`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1572407-1575202:-; feature_type=gene
