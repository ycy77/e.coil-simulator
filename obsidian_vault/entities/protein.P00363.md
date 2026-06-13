---
entity_id: "protein.P00363"
entity_type: "protein"
name: "frdA"
source_database: "UniProt"
source_id: "P00363"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:10373108, ECO:0000305|PubMed:20484676}; Peripheral membrane protein {ECO:0000305|PubMed:10373108}; Cytoplasmic side {ECO:0000305|PubMed:10373108}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "frdA b4154 JW4115"
---

# frdA

`protein.P00363`

## Static

- Type: `protein`
- Source: `UniProt:P00363`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:10373108, ECO:0000305|PubMed:20484676}; Peripheral membrane protein {ECO:0000305|PubMed:10373108}; Cytoplasmic side {ECO:0000305|PubMed:10373108}.

## Enriched Summary

FUNCTION: Two distinct, membrane-bound, FAD-containing enzymes are responsible for the catalysis of fumarate and succinate interconversion; fumarate reductase is used during anaerobic growth, and succinate dehydrogenase is used during aerobic growth. The QFR enzyme complex binds 2 quinones in or near the membrane; 1 near the [3Fe-4S] cluster (QP is proximal to the [3Fe-4S] cluster, on the cytoplasmic side of the membrane) while QD (the distal cluster) is on the other side of the membrane. It is not clear if both of the quinol-binding sites are functionally relevant (PubMed:10373108, PubMed:11850430). {ECO:0000269|PubMed:10373108, ECO:0000269|PubMed:11850430, ECO:0000269|PubMed:24374335}. FrdA is one of two catalytic subunits in the four subunit fumarate reductase complex. This subunit contains the FAD cofactor . This protein has similarity to the SdhA subunit of succinate dehydrogenase . A 2.2 Å crystal structure of L-aspartate oxidase suggests that an unusual tertiary structure is shared by L-aspartate oxidase, the SdhA subunit of succinate dehydrogenase, and the FrdA subunit of fumarate reductase...

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

FUNCTION: Two distinct, membrane-bound, FAD-containing enzymes are responsible for the catalysis of fumarate and succinate interconversion; fumarate reductase is used during anaerobic growth, and succinate dehydrogenase is used during aerobic growth. The QFR enzyme complex binds 2 quinones in or near the membrane; 1 near the [3Fe-4S] cluster (QP is proximal to the [3Fe-4S] cluster, on the cytoplasmic side of the membrane) while QD (the distal cluster) is on the other side of the membrane. It is not clear if both of the quinol-binding sites are functionally relevant (PubMed:10373108, PubMed:11850430). {ECO:0000269|PubMed:10373108, ECO:0000269|PubMed:11850430, ECO:0000269|PubMed:24374335}.

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

- `encodes` <-- [[gene.b4154|gene.b4154]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00363`
- `KEGG:ecj:JW4115;eco:b4154;ecoc:C3026_22455;`
- `GeneID:93777668;948667;`
- `GO:GO:0000104; GO:0005829; GO:0005886; GO:0006113; GO:0006974; GO:0008177; GO:0009055; GO:0009061; GO:0016020; GO:0019645; GO:0044780; GO:0045283; GO:0050660; GO:0071949`
- `EC:1.3.5.1`

## Notes

Fumarate reductase flavoprotein subunit (EC 1.3.5.1) (Quinol-fumarate reductase flavoprotein subunit) (QFR flavoprotein subunit)
