---
entity_id: "protein.P0AC33"
entity_type: "protein"
name: "fumA"
source_database: "UniProt"
source_id: "P0AC33"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fumA b1612 JW1604"
---

# fumA

`protein.P0AC33`

## Static

- Type: `protein`
- Source: `UniProt:P0AC33`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible hydration of fumarate to (S)-malate. Functions as an aerobic enzyme in the direction of malate formation as part of the citric acid cycle. Accounts for about 80% of the fumarase activity when the bacteria grow aerobically. To a lesser extent, also displays D-tartrate dehydratase activity in vitro, but is not able to convert (R)-malate, L-tartrate or meso-tartrate. Can also catalyze the isomerization of enol- to keto-oxaloacetate. {ECO:0000269|PubMed:1329945, ECO:0000269|PubMed:23405168, ECO:0000269|PubMed:3282546, ECO:0000269|PubMed:8422384, ECO:0000269|Ref.7}. Fumarase A (FumA) is one of three characterized fumarase isozymes in E. coli (encoded by EG10356, EG10357, and EG10358), all of which participate in the TCA cycle. FumA is a dimeric [4Fe-4S] cluster-containing protein and belongs to the class I fumarases . Fumarase A can also catalyze the isomerization of enol- to keto-oxalacetate . The cell adapts to changing environmental oxygen conditions by utilizing different isozymes. Both FumA and FumB contain iron-sulfur centers; exposure to oxidative agents such as superoxide results in damage to the metal cofactor and loss of enzyme activity . In contrast, FumC is an iron-independent enzyme and is insensitive to oxidative damage...

## Biological Role

Component of fumarase A (complex.ecocyc.FUMARASE-A).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible hydration of fumarate to (S)-malate. Functions as an aerobic enzyme in the direction of malate formation as part of the citric acid cycle. Accounts for about 80% of the fumarase activity when the bacteria grow aerobically. To a lesser extent, also displays D-tartrate dehydratase activity in vitro, but is not able to convert (R)-malate, L-tartrate or meso-tartrate. Can also catalyze the isomerization of enol- to keto-oxaloacetate. {ECO:0000269|PubMed:1329945, ECO:0000269|PubMed:23405168, ECO:0000269|PubMed:3282546, ECO:0000269|PubMed:8422384, ECO:0000269|Ref.7}.

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.FUMARASE-A|complex.ecocyc.FUMARASE-A]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1612|gene.b1612]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC33`
- `KEGG:ecj:JW1604;eco:b1612;ecoc:C3026_09275;`
- `GeneID:75204456;946826;`
- `GO:GO:0004333; GO:0005829; GO:0006099; GO:0042802; GO:0042803; GO:0046872; GO:0050163; GO:0051539`
- `EC:4.2.1.2; 5.3.2.2`

## Notes

Fumarate hydratase class I, aerobic (EC 4.2.1.2) (Fumarase A) (Oxaloacetate keto--enol-isomerase) (OAAKE isomerase) (Oxaloacetate tautomerase) (EC 5.3.2.2)
