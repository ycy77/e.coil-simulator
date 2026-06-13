---
entity_id: "protein.P0A9H3"
entity_type: "protein"
name: "cadA"
source_database: "UniProt"
source_id: "P0A9H3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cadA ldcI b4131 JW4092"
---

# cadA

`protein.P0A9H3`

## Static

- Type: `protein`
- Source: `UniProt:P0A9H3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Inducible lysine decarboxylase that catalyzes the proton-dependent decarboxylation of L-lysine to produce the polyamine cadaverine and carbon dioxide (PubMed:4590109). Plays a role in pH homeostasis by consuming protons and neutralizing the acidic by-products of carbohydrate fermentation (PubMed:17209032). {ECO:0000269|PubMed:17209032, ECO:0000269|PubMed:4590109}.

## Biological Role

Catalyzes L-lysine carboxy-lyase (cadaverine-forming) (reaction.R00462). Component of lysine decarboxylase 1 (complex.ecocyc.LYSDECARBOX-CPLX).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Inducible lysine decarboxylase that catalyzes the proton-dependent decarboxylation of L-lysine to produce the polyamine cadaverine and carbon dioxide (PubMed:4590109). Plays a role in pH homeostasis by consuming protons and neutralizing the acidic by-products of carbohydrate fermentation (PubMed:17209032). {ECO:0000269|PubMed:17209032, ECO:0000269|PubMed:4590109}.

## Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00462|reaction.R00462]] `KEGG` `database` - via EC:4.1.1.18
- `is_component_of` --> [[complex.ecocyc.LYSDECARBOX-CPLX|complex.ecocyc.LYSDECARBOX-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## Incoming Edges (1)

- `encodes` <-- [[gene.b4131|gene.b4131]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9H3`
- `KEGG:ecj:JW4092;eco:b4131;ecoc:C3026_22330;`
- `GeneID:75169650;75203986;948643;`
- `GO:GO:0005737; GO:0006554; GO:0008923; GO:0042802; GO:0097216`
- `EC:4.1.1.18`

## Notes

Inducible lysine decarboxylase (LDCI) (EC 4.1.1.18)
