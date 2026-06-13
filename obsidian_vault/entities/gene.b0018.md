---
entity_id: "gene.b0018"
entity_type: "gene"
name: "mokC"
source_database: "NCBI RefSeq"
source_id: "gene-b0018"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0018"
  - "mokC"
---

# mokC

`gene.b0018`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0018`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mokC (gene.b0018) is a gene entity. It encodes mokC (protein.P33236). Encoded protein function: FUNCTION: Might be the toxic component of a type I toxin-antitoxin (TA) system (By similarity). Regulatory peptide which completely overlaps hokC and enables hokC expression. {ECO:0000250|UniProtKB:P0ACG4, ECO:0000305|PubMed:10361310}. EcoCyc product frame: EG10373-MONOMER. EcoCyc synonyms: gefL. Genomic coordinates: 16751-16960. EcoCyc protein note: Sequence analysis indicates that the G0-9563 gene is a homologue of the hok (host killing) gene which is responsible for mediating plasmid stabilization by post-segregational killing (PSK) in plasmid R1. hok encodes a stable mRNA whose translation is inhibited by a less stable mRNA encoded by sok. The stable mRNA from hokC encodes a polypeptide that induction experiments have shown to be toxic to Escherichia coli host cells, resulting in cell growth arrest, morphological changes, and rapid cell killing. The hokC system is inactive due to insertion of the insertion element IS186 22 bp downstream of the gene. Sequence analysis shows that after the removal of the IS186 element sequence, the hokC system contains regulatory elements described for the hok/sok system from plasmid R1 including a fold-back inhibition element (fbi), a translational activation element (tac), a promoter, and an overlapping open reading frame named mokC...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33236|protein.P33236]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000064,ECOCYC:EG10373,GeneID:944756`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:16751-16960:-; feature_type=gene
