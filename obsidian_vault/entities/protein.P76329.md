---
entity_id: "protein.P76329"
entity_type: "protein"
name: "yedP"
source_database: "UniProt"
source_id: "P76329"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00617}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yedP b1955 JW1938"
---

# yedP

`protein.P76329`

## Static

- Type: `protein`
- Source: `UniProt:P76329`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00617}.

## Enriched Summary

Mannosyl-3-phosphoglycerate phosphatase (MPGP) (EC 3.1.3.70) YedP is a predicted phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. No phosphatase activity was detected using a variety of possible substrates; thus, the enzyme may be highly substrate-specific . Later, YedP was annotated as a mannosyl-3-phosphoglycerate phosphatase based on its membership in subcluster C2.B.2 of the HAD superfamily .

## Biological Role

Catalyzes alpha-D-mannosyl-3-phosphoglycerate phosphohydrolase (reaction.R05790).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

Mannosyl-3-phosphoglycerate phosphatase (MPGP) (EC 3.1.3.70)

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R05790|reaction.R05790]] `KEGG` `database` - via EC:3.1.3.70

## Incoming Edges (1)

- `encodes` <-- [[gene.b1955|gene.b1955]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76329`
- `KEGG:ecj:JW1938;eco:b1955;ecoc:C3026_11060;`
- `GeneID:946472;`
- `GO:GO:0000287; GO:0005829; GO:0016791; GO:0050531; GO:0051479`
- `EC:3.1.3.70`

## Notes

Mannosyl-3-phosphoglycerate phosphatase (MPGP) (EC 3.1.3.70)
