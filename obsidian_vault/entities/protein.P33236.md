---
entity_id: "protein.P33236"
entity_type: "protein"
name: "mokC"
source_database: "UniProt"
source_id: "P33236"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:P0ACG4}; Single-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mokC gefL b0018 JW5879"
---

# mokC

`protein.P33236`

## Static

- Type: `protein`
- Source: `UniProt:P33236`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:P0ACG4}; Single-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Might be the toxic component of a type I toxin-antitoxin (TA) system (By similarity). Regulatory peptide which completely overlaps hokC and enables hokC expression. {ECO:0000250|UniProtKB:P0ACG4, ECO:0000305|PubMed:10361310}. Sequence analysis indicates that the G0-9563 gene is a homologue of the hok (host killing) gene which is responsible for mediating plasmid stabilization by post-segregational killing (PSK) in plasmid R1. hok encodes a stable mRNA whose translation is inhibited by a less stable mRNA encoded by sok. The stable mRNA from hokC encodes a polypeptide that induction experiments have shown to be toxic to Escherichia coli host cells, resulting in cell growth arrest, morphological changes, and rapid cell killing. The hokC system is inactive due to insertion of the insertion element IS186 22 bp downstream of the gene. Sequence analysis shows that after the removal of the IS186 element sequence, the hokC system contains regulatory elements described for the hok/sok system from plasmid R1 including a fold-back inhibition element (fbi), a translational activation element (tac), a promoter, and an overlapping open reading frame named mokC...

## Annotation

FUNCTION: Might be the toxic component of a type I toxin-antitoxin (TA) system (By similarity). Regulatory peptide which completely overlaps hokC and enables hokC expression. {ECO:0000250|UniProtKB:P0ACG4, ECO:0000305|PubMed:10361310}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0018|gene.b0018]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33236`
- `KEGG:ecj:JW5879;eco:b0018;`
- `GeneID:944756;`
- `GO:GO:0005886`

## Notes

Regulatory protein MokC
