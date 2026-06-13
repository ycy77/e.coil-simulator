---
entity_id: "protein.P33913"
entity_type: "protein"
name: "yejA"
source_database: "UniProt"
source_id: "P33913"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:38334478}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yejA b2177 JW2165"
---

# yejA

`protein.P33913`

## Static

- Type: `protein`
- Source: `UniProt:P33913`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:38334478}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex YejABEF involved in the uptake of oligopeptides (PubMed:17873039, PubMed:21602342, PubMed:39739799). The transporter is involved in the uptake of microcin C (McC), a natural peptide-nucleotide antibiotic that targets aspartyl-tRNA synthetase (PubMed:17873039). It can transport synthetic McC analogs containing a minimal peptide chain length of 6 amino acids and an N-terminal formyl-methionyl-arginyl sequence (PubMed:21602342). The preferred peptide length for YejABEF-mediated uptake is more than 7 but less than 13 amino acids (PubMed:21602342). This subunit is the solute binding protein of the YejABEF transporter (PubMed:38334478, PubMed:39739799). It binds the formylated heptapeptide moiety of McC, whereas the 3-aminopropyl adenylate moiety of McC is not critical for ligand recognition (PubMed:39739799). YejA can accommodate formylated heptapeptides conjugated to molecules with diverse structures (PubMed:39739799). It selectively binds in vitro self-derived peptides containing a core motif of EPRYAFN (PubMed:38334478). The physiological significance of this 'auto-binding' is not clear, but it may have a function in the sensing of periplasmic or membrane stress (PubMed:38334478). {ECO:0000269|PubMed:17873039, ECO:0000269|PubMed:21602342, ECO:0000269|PubMed:38334478, ECO:0000269|PubMed:39739799}...

## Biological Role

Component of putative oligopeptide ABC transporter (complex.ecocyc.ABC-41-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex YejABEF involved in the uptake of oligopeptides (PubMed:17873039, PubMed:21602342, PubMed:39739799). The transporter is involved in the uptake of microcin C (McC), a natural peptide-nucleotide antibiotic that targets aspartyl-tRNA synthetase (PubMed:17873039). It can transport synthetic McC analogs containing a minimal peptide chain length of 6 amino acids and an N-terminal formyl-methionyl-arginyl sequence (PubMed:21602342). The preferred peptide length for YejABEF-mediated uptake is more than 7 but less than 13 amino acids (PubMed:21602342). This subunit is the solute binding protein of the YejABEF transporter (PubMed:38334478, PubMed:39739799). It binds the formylated heptapeptide moiety of McC, whereas the 3-aminopropyl adenylate moiety of McC is not critical for ligand recognition (PubMed:39739799). YejA can accommodate formylated heptapeptides conjugated to molecules with diverse structures (PubMed:39739799). It selectively binds in vitro self-derived peptides containing a core motif of EPRYAFN (PubMed:38334478). The physiological significance of this 'auto-binding' is not clear, but it may have a function in the sensing of periplasmic or membrane stress (PubMed:38334478). {ECO:0000269|PubMed:17873039, ECO:0000269|PubMed:21602342, ECO:0000269|PubMed:38334478, ECO:0000269|PubMed:39739799}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-41-CPLX|complex.ecocyc.ABC-41-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2177|gene.b2177]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33913`
- `KEGG:ecj:JW2165;eco:b2177;ecoc:C3026_12180;`
- `GeneID:946675;`
- `GO:GO:0006857; GO:0015421; GO:0015833; GO:0016020; GO:0030288; GO:0042884; GO:0055052; GO:1904680`

## Notes

Oligopeptide-binding protein YejA
