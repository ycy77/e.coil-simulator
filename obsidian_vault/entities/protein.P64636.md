---
entity_id: "protein.P64636"
entity_type: "protein"
name: "yrfG"
source_database: "UniProt"
source_id: "P64636"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yrfG b3399 JW5865"
---

# yrfG

`protein.P64636`

## Static

- Type: `protein`
- Source: `UniProt:P64636`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dephosphorylation of different purine nucleotides (GMP and IMP). Also hydrolyzes flavin mononucleotide (FMN). {ECO:0000269|PubMed:16990279}. YrfG is a purine nucleotidase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. It shows a low level of discrimination between its preferred substrates .

## Biological Role

Catalyzes RXN-7607 (reaction.ecocyc.RXN-7607), RXN-7609 (reaction.ecocyc.RXN-7609). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the dephosphorylation of different purine nucleotides (GMP and IMP). Also hydrolyzes flavin mononucleotide (FMN). {ECO:0000269|PubMed:16990279}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-7607|reaction.ecocyc.RXN-7607]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-7609|reaction.ecocyc.RXN-7609]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3399|gene.b3399]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P64636`
- `KEGG:ecj:JW5865;eco:b3399;ecoc:C3026_18440;`
- `GeneID:86862203;93778599;947904;`
- `GO:GO:0000287; GO:0005829; GO:0006281; GO:0008253; GO:0008967; GO:0030145`
- `EC:3.1.3.5`

## Notes

GMP/IMP nucleotidase YrfG (EC 3.1.3.5)
