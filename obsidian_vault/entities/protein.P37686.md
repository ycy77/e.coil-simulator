---
entity_id: "protein.P37686"
entity_type: "protein"
name: "yiaY"
source_database: "UniProt"
source_id: "P37686"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yiaY b3589 JW5648"
---

# yiaY

`protein.P37686`

## Static

- Type: `protein`
- Source: `UniProt:P37686`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Probable alcohol dehydrogenase (EC 1.1.1.1) YiaY appears to have NAD-dependent L-threonine dehydrogenase activity . A yiaY deletion mutant constructed by the authors of does not appear to grow in minimal medium lacking glycine. However, the yiaY deletion mutant strain of the Keio collection is able to grow in minimal medium without glycine supplementation .

## Biological Role

Catalyzes primary_alcohol:NAD+ oxidoreductase (reaction.R00623), secondary_alcohol:NAD+ oxidoreductase (reaction.R00624), ethanol:NAD+ oxidoreductase (reaction.R00754), retinol:NAD+ oxidoreductase (reaction.R02124), 1-octanol:NAD+ oxidoreductase (reaction.R02878), trans-3-chloro-2-propene-1-ol:NAD+ oxidoreductase (reaction.R05233), cis-3-chloro-2-propene-1-ol:NAD+ oxidoreductase (reaction.R05234), 1-hydroxymethylnaphthalene:NAD+ oxidoreductase (reaction.R06917), and 2 more.

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

Probable alcohol dehydrogenase (EC 1.1.1.1)

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
- `catalyzes` --> [[reaction.ecocyc.RXN-14249|reaction.ecocyc.RXN-14249]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3589|gene.b3589]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37686`
- `KEGG:ecj:JW5648;eco:b3589;ecoc:C3026_19460;`
- `GeneID:948102;`
- `GO:GO:0004022; GO:0008743; GO:0046872`
- `EC:1.1.1.1`

## Notes

Probable alcohol dehydrogenase (EC 1.1.1.1)
