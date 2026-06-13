---
entity_id: "protein.P39451"
entity_type: "protein"
name: "adhP"
source_database: "UniProt"
source_id: "P39451"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "adhP yddN b1478 JW1474"
---

# adhP

`protein.P39451`

## Static

- Type: `protein`
- Source: `UniProt:P39451`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Preferred specificity is towards 1-propanol.

## Biological Role

Catalyzes primary_alcohol:NAD+ oxidoreductase (reaction.R00623), secondary_alcohol:NAD+ oxidoreductase (reaction.R00624), ethanol:NAD+ oxidoreductase (reaction.R00754), retinol:NAD+ oxidoreductase (reaction.R02124), 1-octanol:NAD+ oxidoreductase (reaction.R02878), trans-3-chloro-2-propene-1-ol:NAD+ oxidoreductase (reaction.R05233), cis-3-chloro-2-propene-1-ol:NAD+ oxidoreductase (reaction.R05234), 1-hydroxymethylnaphthalene:NAD+ oxidoreductase (reaction.R06917), and 1 more. Component of ethanol dehydrogenase / alcohol dehydrogenase (complex.ecocyc.CPLX0-8015).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00626` Naphthalene degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

FUNCTION: Preferred specificity is towards 1-propanol.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00626` Naphthalene degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Outgoing Edges (10)

- `catalyzes` --> [[reaction.R00623|reaction.R00623]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R00624|reaction.R00624]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R00754|reaction.R00754]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R02124|reaction.R02124]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R02878|reaction.R02878]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R05233|reaction.R05233]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R05234|reaction.R05234]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R06917|reaction.R06917]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` --> [[reaction.R06927|reaction.R06927]] `KEGG` `database` - via EC:1.1.1.1
- `is_component_of` --> [[complex.ecocyc.CPLX0-8015|complex.ecocyc.CPLX0-8015]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1478|gene.b1478]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39451`
- `KEGG:ecj:JW1474;eco:b1478;ecoc:C3026_08570;`
- `GeneID:946036;`
- `GO:GO:0004022; GO:0006974; GO:0008270; GO:0045471; GO:0046187`
- `EC:1.1.1.1`

## Notes

Alcohol dehydrogenase, propanol-preferring (EC 1.1.1.1)
