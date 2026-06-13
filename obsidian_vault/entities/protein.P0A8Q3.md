---
entity_id: "protein.P0A8Q3"
entity_type: "protein"
name: "frdD"
source_database: "UniProt"
source_id: "P0A8Q3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00709, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00709, ECO:0000269|PubMed:10373108}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "frdD b4151 JW4112"
---

# frdD

`protein.P0A8Q3`

## Static

- Type: `protein`
- Source: `UniProt:P0A8Q3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00709, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00709, ECO:0000269|PubMed:10373108}.

## Enriched Summary

FUNCTION: Two distinct, membrane-bound, FAD-containing enzymes are responsible for the catalysis of fumarate and succinate interconversion; fumarate reductase is used in anaerobic growth, and succinate dehydrogenase is used in aerobic growth. Anchors the catalytic components of the fumarate reductase complex to the cell inner membrane, binds quinones (PubMed:10373108). The QFR enzyme complex binds 2 quinones in or near the membrane; 1 near the [3Fe-4S] cluster (QP is proximal to the [3Fe-4S] cluster, on the cytoplasmic side of the membrane) while QD (the distal cluster) is on the other side of the membrane. It is not clear if both of the quinol-binding sites are functionally relevant (PubMed:10373108, PubMed:11850430). {ECO:0000269|PubMed:10373108, ECO:0000269|PubMed:11850430}. This is one of two integral membrane proteins in the four subunit fumarate reductase complex . FrdC and FrdD each have three transmembrane helices connected by periplasmic loops; the N-terminus is located in the cytoplasm and the C-terminus is located in the periplasm. The transmembrane helices are positioned to form two menaquinone binding pockets Despite similar function, hydrophobicity, and protein size, the FrdC and FrdD subunits of fumarate reductase do not share significant sequence identity with the corresponding membrane-binding subunits of succinate dehydrogenase, SdhC and SdhD...

## Biological Role

Component of fumarate reductase (complex.ecocyc.FUMARATE-REDUCTASE).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Two distinct, membrane-bound, FAD-containing enzymes are responsible for the catalysis of fumarate and succinate interconversion; fumarate reductase is used in anaerobic growth, and succinate dehydrogenase is used in aerobic growth. Anchors the catalytic components of the fumarate reductase complex to the cell inner membrane, binds quinones (PubMed:10373108). The QFR enzyme complex binds 2 quinones in or near the membrane; 1 near the [3Fe-4S] cluster (QP is proximal to the [3Fe-4S] cluster, on the cytoplasmic side of the membrane) while QD (the distal cluster) is on the other side of the membrane. It is not clear if both of the quinol-binding sites are functionally relevant (PubMed:10373108, PubMed:11850430). {ECO:0000269|PubMed:10373108, ECO:0000269|PubMed:11850430}.

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.FUMARATE-REDUCTASE|complex.ecocyc.FUMARATE-REDUCTASE]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4151|gene.b4151]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8Q3`
- `KEGG:ecj:JW4112;eco:b4151;ecoc:C3026_22440;`
- `GeneID:75169672;948668;`
- `GO:GO:0000104; GO:0005886; GO:0006106; GO:0006113; GO:0009061; GO:0016020; GO:0019645; GO:0044780; GO:0045283`

## Notes

Fumarate reductase subunit D (Fumarate reductase 13 kDa hydrophobic protein) (Quinol-fumarate reductase subunit D) (QFR subunit D)
