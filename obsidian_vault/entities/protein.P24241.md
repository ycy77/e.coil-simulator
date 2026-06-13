---
entity_id: "protein.P24241"
entity_type: "protein"
name: "ascF"
source_database: "UniProt"
source_id: "P24241"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ascF b2715 JW5435"
---

# ascF

`protein.P24241`

## Static

- Type: `protein`
- Source: `UniProt:P24241`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in arbutin, cellobiose, and salicin transport.

## Biological Role

Component of β-glucoside specific PTS enzyme II (complex.ecocyc.CPLX-153).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in arbutin, cellobiose, and salicin transport.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-153|complex.ecocyc.CPLX-153]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2715|gene.b2715]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24241`
- `KEGG:ecj:JW5435;eco:b2715;ecoc:C3026_14940;`
- `GeneID:947154;`
- `GO:GO:0005886; GO:0008982; GO:0009401; GO:0015771; GO:0016301; GO:0090589`
- `EC:2.7.1.-`

## Notes

PTS system arbutin-, cellobiose-, and salicin-specific EIIBC component (EIIBC-Asc) (EII-Asc) [Includes: Arbutin-, cellobiose-, and salicin-specific phosphotransferase enzyme IIB component (EC 2.7.1.-) (PTS system arbutin-, cellobiose-, and salicin-specific EIIB component); Arbutin, cellobiose, and salicin permease IIC component (PTS system arbutin-, cellobiose-, and salicin-specific EIIC component)]
