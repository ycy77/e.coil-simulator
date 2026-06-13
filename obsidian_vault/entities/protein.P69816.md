---
entity_id: "protein.P69816"
entity_type: "protein"
name: "frwB"
source_database: "UniProt"
source_id: "P69816"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "frwB yijK b3950 JW3922"
---

# frwB

`protein.P69816`

## Static

- Type: `protein`
- Source: `UniProt:P69816`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FrwABC PTS system is involved in fructose transport. {ECO:0000250|UniProtKB:P20966, ECO:0000305|PubMed:7773398}. Sequence analysis indicates that an frwB encoded protein has similarity to the IIB domains of the PTS Enzymes II specific for fructose. frwB and frwD are similar to each other and to the IIB domains of the PTS Enzymes II specific for fructose. frwB contains conserved cysteine (cys10) and histidine residues (his16) predicted to be involved in phosphoryl transfer

## Biological Role

Component of putative PTS enzyme II FrwCBDPtsA (complex.ecocyc.CPLX-160).

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FrwABC PTS system is involved in fructose transport. {ECO:0000250|UniProtKB:P20966, ECO:0000305|PubMed:7773398}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-160|complex.ecocyc.CPLX-160]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3950|gene.b3950]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69816`
- `KEGG:ecj:JW3922;eco:b3950;ecoc:C3026_21345;`
- `GeneID:89518892;948447;`
- `GO:GO:0005737; GO:0005886; GO:0009401; GO:0016301; GO:0022877; GO:0090582; GO:1902495; GO:1990539`
- `EC:2.7.1.202`

## Notes

PTS system fructose-like EIIB component 2 (EC 2.7.1.202) (Fructose-like phosphotransferase enzyme IIB component 2)
