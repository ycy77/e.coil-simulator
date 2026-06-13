---
entity_id: "protein.P08722"
entity_type: "protein"
name: "bglF"
source_database: "UniProt"
source_id: "P08722"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bglF bglC bglS b3722 JW3700"
---

# bglF

`protein.P08722`

## Static

- Type: `protein`
- Source: `UniProt:P08722`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in beta-glucoside transport.; FUNCTION: Acts both as a kinase and as a phosphatase on BglG.

## Biological Role

Component of β-glucoside specific PTS enzyme II / BglG kinase / BglG phosphatase (complex.ecocyc.CPLX-154), β-glucoside specific PTS enzyme II - cys24 phosphorylated (complex.ecocyc.CPLX0-8115).

## Enriched Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in beta-glucoside transport.; FUNCTION: Acts both as a kinase and as a phosphatase on BglG.

## Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX-154|complex.ecocyc.CPLX-154]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8115|complex.ecocyc.CPLX0-8115]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3722|gene.b3722]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08722`
- `KEGG:ecj:JW3700;eco:b3722;ecoc:C3026_20175;`
- `GeneID:948236;`
- `GO:GO:0005886; GO:0008982; GO:0009401; GO:0015771; GO:0016301; GO:0090589`
- `EC:2.7.1.-`

## Notes

PTS system beta-glucoside-specific EIIBCA component (EIIBCA-Bgl) (EII-Bgl) [Includes: Beta-glucoside-specific phosphotransferase enzyme IIB component (EC 2.7.1.-) (PTS system beta-glucoside-specific EIIB component); Beta-glucoside permease IIC component (PTS system beta-glucoside-specific EIIC component); Beta-glucoside-specific phosphotransferase enzyme IIA component (PTS system beta-glucoside-specific EIIA component)]
