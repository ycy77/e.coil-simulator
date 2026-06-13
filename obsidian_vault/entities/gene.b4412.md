---
entity_id: "gene.b4412"
entity_type: "gene"
name: "hokC"
source_database: "NCBI RefSeq"
source_id: "gene-b4412"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4412"
  - "hokC"
---

# hokC

`gene.b4412`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4412`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hokC (gene.b4412) is a gene entity. It encodes hokC (protein.P0ACG4). Encoded protein function: FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. When overexpressed kills cells within minutes; causes collapse of the transmembrane potential and arrest of respiration (PubMed:10361310). Its toxic effect is probably neutralized by antisense antitoxin RNA SokC (PubMed:10361310). {ECO:0000269|PubMed:10361310, ECO:0000305|PubMed:10361310}. EcoCyc product frame: MONOMER0-1564. EcoCyc synonyms: gef. Genomic coordinates: 16751-16903. EcoCyc protein note: HokC is a member of a conserved Hok family of toxin proteins . Sequence analysis indicates that the hokC gene is a homologue of the hok (host killing) gene which is responsible for mediating plasmid stabilization by post-segregational killing (PSK) in plasmid R1. E. coli has five chromosomal hok-like genes ; HokC has similarity to E. coli EG11130-MONOMER HokD and the episomal Hok protein . hok encodes a stable mRNA whose translation is inhibited by a less stable mRNA encoded by sok. The stable mRNA from hokC encodes a polypeptide that induction experiments have shown to be toxic to Escherichia coli host cells, resulting in cell growth arrest, morphological changes, and rapid cell killing. The hokC system is inactive due to insertion of the insertion element IS186 22 bp downstream of the gene...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACG4|protein.P0ACG4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0047278,ECOCYC:G0-9563,GeneID:2847744`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:16751-16903:-; feature_type=gene
