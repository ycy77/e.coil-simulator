---
entity_id: "protein.P0A9G6"
entity_type: "protein"
name: "aceA"
source_database: "UniProt"
source_id: "P0A9G6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aceA icl b4015 JW3975"
---

# aceA

`protein.P0A9G6`

## Static

- Type: `protein`
- Source: `UniProt:P0A9G6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the metabolic adaptation in response to environmental changes. Catalyzes the reversible formation of succinate and glyoxylate from isocitrate, a key step of the glyoxylate cycle, which operates as an anaplerotic route for replenishing the tricarboxylic acid cycle during growth on fatty acid substrates. {ECO:0000269|PubMed:15748982, ECO:0000269|PubMed:3281659, ECO:0000269|PubMed:3291954, ECO:0000269|PubMed:7826335, ECO:0000269|Ref.9}.

## Biological Role

Catalyzes (2S,3R)-3-hydroxybutane-1,2,3-tricarboxylate pyruvate-lyase (succinate-forming) (reaction.R00409), isocitrate glyoxylate-lyase (succinate-forming) (reaction.R00479). Component of isocitrate lyase (complex.ecocyc.ISOCIT-LYASE).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Involved in the metabolic adaptation in response to environmental changes. Catalyzes the reversible formation of succinate and glyoxylate from isocitrate, a key step of the glyoxylate cycle, which operates as an anaplerotic route for replenishing the tricarboxylic acid cycle during growth on fatty acid substrates. {ECO:0000269|PubMed:15748982, ECO:0000269|PubMed:3281659, ECO:0000269|PubMed:3291954, ECO:0000269|PubMed:7826335, ECO:0000269|Ref.9}.

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00409|reaction.R00409]] `KEGG` `database` - via EC:4.1.3.30
- `catalyzes` --> [[reaction.R00479|reaction.R00479]] `KEGG` `database` - via EC:4.1.3.1
- `is_component_of` --> [[complex.ecocyc.ISOCIT-LYASE|complex.ecocyc.ISOCIT-LYASE]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b4015|gene.b4015]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9G6`
- `KEGG:ecj:JW3975;eco:b4015;ecoc:C3026_21690;`
- `GeneID:75204155;948517;`
- `GO:GO:0004451; GO:0005829; GO:0006097; GO:0006099; GO:0043169; GO:0046872`
- `EC:4.1.3.1`

## Notes

Isocitrate lyase (ICL) (EC 4.1.3.1) (Isocitrase) (Isocitratase)
