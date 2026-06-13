---
entity_id: "protein.P0A955"
entity_type: "protein"
name: "eda"
source_database: "UniProt"
source_id: "P0A955"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "eda hga kdgA b1850 JW1839"
---

# eda

`protein.P0A955`

## Static

- Type: `protein`
- Source: `UniProt:P0A955`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Involved in the degradation of glucose via the Entner-Doudoroff pathway (PubMed:15659677, PubMed:1624451). Catalyzes the reversible, stereospecific retro-aldol cleavage of 2-keto-3-deoxy-6-phosphogluconate (KDPG) to pyruvate and D-glyceraldehyde-3-phosphate (PubMed:11342129, PubMed:17962400, PubMed:17981470). In vitro, can also catalyze the cleavage of 2-keto-4-hydroxy-4-(2'-pyridyl)butyrate (KHPB), 2-keto-3-deoxy-6-phosphogalactonate (KDPGal), and of the substrate analogs 2-keto-3-deoxy-gluconate (KDG) and 2-keto-4-hydroxyoctonate (KHO) (PubMed:17962400). Can accept some nucleophiles other than pyruvate, including 2-oxobutanoate, phenylpyruvate and fluorobutanoate (PubMed:17981470). In addition to its KDPG aldolase activity, catalyzes the reversible cleavage of 2-keto-4-hydroxyglutarate (KHG) to glyoxylate and pyruvate (PubMed:1098660, PubMed:1339418, PubMed:4560498, PubMed:7016177). The enzyme is stereoselective for the S-enantiomer of KHG (PubMed:1098660, PubMed:4560498). Cleavage of KHG could serve in tricarboxylic acid (TCA) cycle regulation or, when operating in the reverse direction, in the detoxification of glyoxylate (Probable). Finally, also shows a high level of oxaloacetate beta-decarboxylase activity (PubMed:1339418, PubMed:4560498)...

## Biological Role

Catalyzes 4-hydroxy-2-oxoglutarate glyoxylate-lyase (pyruvate-forming) (reaction.R00470). Component of KHG/KDPG aldolase (complex.ecocyc.KDPGALDOL-4OH2OXOGLUTARALDOL-CPLX).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Involved in the degradation of glucose via the Entner-Doudoroff pathway (PubMed:15659677, PubMed:1624451). Catalyzes the reversible, stereospecific retro-aldol cleavage of 2-keto-3-deoxy-6-phosphogluconate (KDPG) to pyruvate and D-glyceraldehyde-3-phosphate (PubMed:11342129, PubMed:17962400, PubMed:17981470). In vitro, can also catalyze the cleavage of 2-keto-4-hydroxy-4-(2'-pyridyl)butyrate (KHPB), 2-keto-3-deoxy-6-phosphogalactonate (KDPGal), and of the substrate analogs 2-keto-3-deoxy-gluconate (KDG) and 2-keto-4-hydroxyoctonate (KHO) (PubMed:17962400). Can accept some nucleophiles other than pyruvate, including 2-oxobutanoate, phenylpyruvate and fluorobutanoate (PubMed:17981470). In addition to its KDPG aldolase activity, catalyzes the reversible cleavage of 2-keto-4-hydroxyglutarate (KHG) to glyoxylate and pyruvate (PubMed:1098660, PubMed:1339418, PubMed:4560498, PubMed:7016177). The enzyme is stereoselective for the S-enantiomer of KHG (PubMed:1098660, PubMed:4560498). Cleavage of KHG could serve in tricarboxylic acid (TCA) cycle regulation or, when operating in the reverse direction, in the detoxification of glyoxylate (Probable). Finally, also shows a high level of oxaloacetate beta-decarboxylase activity (PubMed:1339418, PubMed:4560498). The enzyme could have several physiological roles and function as a stress response protein in addition to its role in the catabolism of sugar acids (PubMed:15659677). {ECO:0000269|PubMed:1098660, ECO:0000269|PubMed:11342129, ECO:0000269|PubMed:1339418, ECO:0000269|PubMed:15659677, ECO:0000269|PubMed:1624451, ECO:0000269|PubMed:17962400, ECO:0000269|PubMed:17981470, ECO:0000269|PubMed:4560498, ECO:0000269|PubMed:7016177, ECO:0000305|PubMed:15659677}.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00470|reaction.R00470]] `KEGG` `database` - via EC:4.1.3.42
- `is_component_of` --> [[complex.ecocyc.KDPGALDOL-4OH2OXOGLUTARALDOL-CPLX|complex.ecocyc.KDPGALDOL-4OH2OXOGLUTARALDOL-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b1850|gene.b1850]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A955`
- `KEGG:ecj:JW1839;eco:b1850;ecoc:C3026_10540;`
- `GeneID:86859390;93776117;946367;`
- `GO:GO:0005829; GO:0008675; GO:0008700; GO:0008948; GO:0009255; GO:0016020; GO:0016832; GO:0016833; GO:0042802; GO:0106009`
- `EC:4.1.1.112; 4.1.2.14; 4.1.3.42`

## Notes

KHG/KDPG aldolase ((4S)-4-hydroxy-2-oxoglutarate aldolase) (EC 4.1.3.42) (2-dehydro-3-deoxy-phosphogluconate aldolase) (EC 4.1.2.14) (2-keto-3-deoxy-6-phosphogluconate aldolase) (KDPG aldolase) (2-keto-4-hydroxyglutarate aldolase) (KHG aldolase) (Ketohydroxyglutarate aldolase) (Entner-Douderoff aldolase) (Oxaloacetate decarboxylase) (EC 4.1.1.112) (Phospho-2-dehydro-3-deoxygluconate aldolase) (Phospho-2-keto-3-deoxygluconate aldolase)
