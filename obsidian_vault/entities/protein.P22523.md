---
entity_id: "protein.P22523"
entity_type: "protein"
name: "mukB"
source_database: "UniProt"
source_id: "P22523"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm, nucleoid {ECO:0000269|PubMed:11886550, ECO:0000269|PubMed:22380631}. Note=Restricted to the nucleoid region, far from the cell poles."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mukB b0924 JW0907"
---

# mukB

`protein.P22523`

## Static

- Type: `protein`
- Source: `UniProt:P22523`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm, nucleoid {ECO:0000269|PubMed:11886550, ECO:0000269|PubMed:22380631}. Note=Restricted to the nucleoid region, far from the cell poles.

## Enriched Summary

FUNCTION: Plays a central role in chromosome condensation, segregation and cell cycle progression. Functions as a homodimer, which is essential for chromosome partition. Involved in negative DNA supercoiling in vivo, and by this means organizes and compacts chromosomes. May achieve or facilitate chromosome segregation by condensation of DNA from both sides of a centrally located replisome during cell division. Stimulates both DNA relaxation and to a lesser extent decatenation activity of topoisomerase IV. {ECO:0000269|PubMed:10660686}. The MukB protein belongs to the family of SMC (Structural Maintenance of Chromosomes) proteins found in TAX-543 . It is the ATPase subunit of the CPLX0-2561 complex that is involved in chromosome condensation and partitioning (e.g. segregation) through its interactions with CPLX0-2424 (Topo IV) and CPLX0-7789 MatP . MukB acts as a macromolecular clamp that condenses DNA in a cooperative manner; ATP stimulates initiation of condensation but is not required for binding to DNA, bridging between two DNA strands, nor translocating along the chromosome . GFP-marked MukB protein is observed to occupy the same location as the nucleoid in the presence of MukE and MukF but appears to not co-localize with the FtsZ ring based on fluorescent antibody labelling...

## Biological Role

Component of bacterial condensin MukBEF (complex.ecocyc.CPLX0-2561), chromosome partitioning protein MukB (complex.ecocyc.CPLX0-7696).

## Annotation

FUNCTION: Plays a central role in chromosome condensation, segregation and cell cycle progression. Functions as a homodimer, which is essential for chromosome partition. Involved in negative DNA supercoiling in vivo, and by this means organizes and compacts chromosomes. May achieve or facilitate chromosome segregation by condensation of DNA from both sides of a centrally located replisome during cell division. Stimulates both DNA relaxation and to a lesser extent decatenation activity of topoisomerase IV. {ECO:0000269|PubMed:10660686}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2561|complex.ecocyc.CPLX0-2561]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7696|complex.ecocyc.CPLX0-7696]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0924|gene.b0924]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P22523`
- `KEGG:ecj:JW0907;eco:b0924;ecoc:C3026_05680;`
- `GeneID:945549;`
- `GO:GO:0000796; GO:0003677; GO:0005524; GO:0005525; GO:0005737; GO:0005829; GO:0006260; GO:0007059; GO:0007062; GO:0009295; GO:0016887; GO:0030261; GO:0042802; GO:0051301`

## Notes

Chromosome partition protein MukB (Structural maintenance of chromosome-related protein)
