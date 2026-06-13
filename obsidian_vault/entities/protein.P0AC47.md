---
entity_id: "protein.P0AC47"
entity_type: "protein"
name: "frdB"
source_database: "UniProt"
source_id: "P0AC47"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:10373108}; Peripheral membrane protein {ECO:0000305|PubMed:10373108}; Cytoplasmic side {ECO:0000305|PubMed:10373108}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "frdB b4153 JW4114"
---

# frdB

`protein.P0AC47`

## Static

- Type: `protein`
- Source: `UniProt:P0AC47`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:10373108}; Peripheral membrane protein {ECO:0000305|PubMed:10373108}; Cytoplasmic side {ECO:0000305|PubMed:10373108}.

## Enriched Summary

FUNCTION: Two distinct, membrane-bound, FAD-containing enzymes are responsible for the catalysis of fumarate and succinate interconversion; fumarate reductase is used during anaerobic growth, and succinate dehydrogenase is used during aerobic growth. The QFR enzyme complex binds 2 quinones in or near the membrane; 1 near the [3Fe-4S] cluster (QP is proximal to the [3Fe-4S] cluster, on the cytoplasmic side of the membrane) while QD (the distal cluster) is on the other side of the membrane. It is not clear if both of the quinol-binding sites are functionally relevant (PubMed:10373108, PubMed:11850430). {ECO:0000269|PubMed:10373108, ECO:0000269|PubMed:11850430}. This is one of two catalytic subunits of the four subunit fumarate reductase complex. FrdB contains 11 cysteine residues arranged in three clusters predicted to form the iron-sulfur clusters . This subunit contains three iron-sulfur clusters: a 4Fe-4S, a 3Fe-4S and a 2Fe-2S . This subunit has 38% identity to the succinate dehydrogenase iron-sulfur binding subunit, SdhB .

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

FUNCTION: Two distinct, membrane-bound, FAD-containing enzymes are responsible for the catalysis of fumarate and succinate interconversion; fumarate reductase is used during anaerobic growth, and succinate dehydrogenase is used during aerobic growth. The QFR enzyme complex binds 2 quinones in or near the membrane; 1 near the [3Fe-4S] cluster (QP is proximal to the [3Fe-4S] cluster, on the cytoplasmic side of the membrane) while QD (the distal cluster) is on the other side of the membrane. It is not clear if both of the quinol-binding sites are functionally relevant (PubMed:10373108, PubMed:11850430). {ECO:0000269|PubMed:10373108, ECO:0000269|PubMed:11850430}.

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

- `encodes` <-- [[gene.b4153|gene.b4153]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC47`
- `KEGG:ecj:JW4114;eco:b4153;ecoc:C3026_22450;`
- `GeneID:86861452;93777669;948666;`
- `GO:GO:0005829; GO:0005886; GO:0006099; GO:0006113; GO:0008177; GO:0009055; GO:0009061; GO:0016020; GO:0019645; GO:0044780; GO:0045283; GO:0046872; GO:0051536; GO:0051537; GO:0051538; GO:0051539`
- `EC:1.3.5.1`

## Notes

Fumarate reductase iron-sulfur subunit (EC 1.3.5.1) (Quinol-fumarate reductase iron-sulfur subunit) (QFR iron-sulfur subunit)
