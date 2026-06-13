---
entity_id: "protein.P14407"
entity_type: "protein"
name: "fumB"
source_database: "UniProt"
source_id: "P14407"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fumB b4122 JW4083"
---

# fumB

`protein.P14407`

## Static

- Type: `protein`
- Source: `UniProt:P14407`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible hydration of fumarate to (S)-malate. Functions in the generation of fumarate for use as an anaerobic electron acceptor. To a lesser extent, also displays D-tartrate dehydratase activity, but is not able to convert (R)-malate, L-tartrate or meso-tartrate. Is required for anaerobic growth on D-tartrate. {ECO:0000269|PubMed:17643228, ECO:0000269|PubMed:23405168, ECO:0000269|PubMed:3282546, ECO:0000269|Ref.6}. Fumarase B (FumB) is one of three characterized fumarase isozymes in E. coli (encoded by EG10356, EG10357, and EG10358), all of which participate in the TCA cycle. FumB belongs to the class I fumarases; like FumA, it is a homodimeric 4Fe-4S cluster-containing protein . Fumarase B is required for anaerobic growth on D-tartrate and appears to be involved in biofilm formation . The cell adapts to changing environmental oxygen conditions by utilizing different isozymes. Both FumA and FumB contain iron-sulfur centers; exposure to oxidative agents such as superoxide results in damage to the metal cofactor and loss of enzyme activity . Although FumB was previously reported to have a higher affinity for malate than for fumarate , recent kinetic data using a purified enzyme have shown it to be similar to FumA . FumB is thought to function as an alternative enzyme during anaerobiosis...

## Biological Role

Component of fumarase B (complex.ecocyc.FUMARASE-B).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible hydration of fumarate to (S)-malate. Functions in the generation of fumarate for use as an anaerobic electron acceptor. To a lesser extent, also displays D-tartrate dehydratase activity, but is not able to convert (R)-malate, L-tartrate or meso-tartrate. Is required for anaerobic growth on D-tartrate. {ECO:0000269|PubMed:17643228, ECO:0000269|PubMed:23405168, ECO:0000269|PubMed:3282546, ECO:0000269|Ref.6}.

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.FUMARASE-B|complex.ecocyc.FUMARASE-B]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4122|gene.b4122]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P14407`
- `KEGG:ecj:JW4083;eco:b4122;ecoc:C3026_22275;`
- `GeneID:948642;`
- `GO:GO:0004333; GO:0005829; GO:0006099; GO:0006974; GO:0042803; GO:0044010; GO:0046872; GO:0047808; GO:0051539`
- `EC:4.2.1.2; 4.2.1.81`

## Notes

Fumarate hydratase class I, anaerobic (EC 4.2.1.2) (D-tartrate dehydratase) (EC 4.2.1.81) (Fumarase B)
