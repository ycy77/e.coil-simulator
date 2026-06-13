---
entity_id: "protein.P0ACG4"
entity_type: "protein"
name: "hokC"
source_database: "UniProt"
source_id: "P0ACG4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:1943700}; Single-pass type II membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hokC gef b4412 JW5002 b0018.1"
---

# hokC

`protein.P0ACG4`

## Static

- Type: `protein`
- Source: `UniProt:P0ACG4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:1943700}; Single-pass type II membrane protein.

## Enriched Summary

FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. When overexpressed kills cells within minutes; causes collapse of the transmembrane potential and arrest of respiration (PubMed:10361310). Its toxic effect is probably neutralized by antisense antitoxin RNA SokC (PubMed:10361310). {ECO:0000269|PubMed:10361310, ECO:0000305|PubMed:10361310}. HokC is a member of a conserved Hok family of toxin proteins . Sequence analysis indicates that the hokC gene is a homologue of the hok (host killing) gene which is responsible for mediating plasmid stabilization by post-segregational killing (PSK) in plasmid R1. E. coli has five chromosomal hok-like genes ; HokC has similarity to E. coli EG11130-MONOMER HokD and the episomal Hok protein . hok encodes a stable mRNA whose translation is inhibited by a less stable mRNA encoded by sok. The stable mRNA from hokC encodes a polypeptide that induction experiments have shown to be toxic to Escherichia coli host cells, resulting in cell growth arrest, morphological changes, and rapid cell killing. The hokC system is inactive due to insertion of the insertion element IS186 22 bp downstream of the gene...

## Biological Role

Component of small toxic polypeptide HokC (complex.ecocyc.CPLX0-2621).

## Annotation

FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. When overexpressed kills cells within minutes; causes collapse of the transmembrane potential and arrest of respiration (PubMed:10361310). Its toxic effect is probably neutralized by antisense antitoxin RNA SokC (PubMed:10361310). {ECO:0000269|PubMed:10361310, ECO:0000305|PubMed:10361310}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2621|complex.ecocyc.CPLX0-2621]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4412|gene.b4412]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACG4`
- `KEGG:ecj:JW5002;eco:b4412;ecoc:C3026_00085;`
- `GeneID:2847744;86862532;`
- `GO:GO:0005886; GO:0042597`

## Notes

Toxic protein HokC (Protein Gef)
