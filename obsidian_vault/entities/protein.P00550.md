---
entity_id: "protein.P00550"
entity_type: "protein"
name: "mtlA"
source_database: "UniProt"
source_id: "P00550"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:6309813}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:368051}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mtlA b3599 JW3573"
---

# mtlA

`protein.P00550`

## Static

- Type: `protein`
- Source: `UniProt:P00550`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:6309813}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:368051}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in D-mannitol transport (PubMed:2123863, PubMed:368051, PubMed:6427236). Also able to use D-mannonic acid (PubMed:6427236). {ECO:0000269|PubMed:2123863, ECO:0000269|PubMed:368051, ECO:0000269|PubMed:6427236}.

## Biological Role

Component of mannitol-specific PTS enzyme II (complex.ecocyc.CPLX-166).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in D-mannitol transport (PubMed:2123863, PubMed:368051, PubMed:6427236). Also able to use D-mannonic acid (PubMed:6427236). {ECO:0000269|PubMed:2123863, ECO:0000269|PubMed:368051, ECO:0000269|PubMed:6427236}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-166|complex.ecocyc.CPLX-166]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3599|gene.b3599]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00550`
- `KEGG:ecj:JW3573;eco:b3599;ecoc:C3026_19515;`
- `GeneID:948118;`
- `GO:GO:0005886; GO:0009401; GO:0015795; GO:0015797; GO:0016301; GO:0022872; GO:0090563; GO:0090565`
- `EC:2.7.1.197`

## Notes

PTS system mannitol-specific EIICBA component (EIICBA-Mtl) (EII-Mtl) [Includes: Mannitol permease IIC component (PTS system mannitol-specific EIIC component); Mannitol-specific phosphotransferase enzyme IIB component (EC 2.7.1.197) (PTS system mannitol-specific EIIB component); Mannitol-specific phosphotransferase enzyme IIA component (PTS system mannitol-specific EIIA component)]
