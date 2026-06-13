---
entity_id: "protein.P36672"
entity_type: "protein"
name: "treB"
source_database: "UniProt"
source_id: "P36672"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000305|PubMed:2160944}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00426}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "treB b4240 JW4199"
---

# treB

`protein.P36672`

## Static

- Type: `protein`
- Source: `UniProt:P36672`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00426, ECO:0000305|PubMed:2160944}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00426}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in trehalose transport at low osmolarity. {ECO:0000269|PubMed:2160944, ECO:0000305|PubMed:7608078}. TreB contains PTS Enzyme IIB and IIC domains

## Biological Role

Component of trehalose-specific PTS enzyme II (complex.ecocyc.CPLX-168).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in trehalose transport at low osmolarity. {ECO:0000269|PubMed:2160944, ECO:0000305|PubMed:7608078}.

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-168|complex.ecocyc.CPLX-168]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4240|gene.b4240]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36672`
- `KEGG:ecj:JW4199;eco:b4240;`
- `GeneID:948761;`
- `GO:GO:0005886; GO:0008982; GO:0009401; GO:0015574; GO:0015771; GO:0016301; GO:0090589`
- `EC:2.7.1.201`

## Notes

PTS system trehalose-specific EIIBC component (EIIBC-Tre) (EII-Tre) [Includes: Trehalose-specific phosphotransferase enzyme IIB component (EC 2.7.1.201) (PTS system trehalose-specific EIIB component); Trehalose permease IIC component (PTS system trehalose-specific EIIC component)]
