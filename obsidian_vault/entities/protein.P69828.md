---
entity_id: "protein.P69828"
entity_type: "protein"
name: "gatA"
source_database: "UniProt"
source_id: "P69828"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:8955298}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gatA b2094 JW2078/JW2081"
---

# gatA

`protein.P69828`

## Static

- Type: `protein`
- Source: `UniProt:P69828`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:8955298}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. The enzyme II complex composed of GatA, GatB and GatC is involved in galactitol transport. It can also use D-glucitol. {ECO:0000269|PubMed:1100608, ECO:0000269|PubMed:8955298}. gatA sequenced from a wild-type isolate of E. coli, strain EC3132, encodes a small hydrophilic protein .

## Biological Role

Component of galactitol-specific PTS enzyme II (complex.ecocyc.CPLX0-231).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. The enzyme II complex composed of GatA, GatB and GatC is involved in galactitol transport. It can also use D-glucitol. {ECO:0000269|PubMed:1100608, ECO:0000269|PubMed:8955298}.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-231|complex.ecocyc.CPLX0-231]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2094|gene.b2094]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69828`
- `KEGG:ecj:JW2078;ecj:JW2081;eco:b2094;ecoc:C3026_11755;`
- `GeneID:75172215;946633;`
- `GO:GO:0005829; GO:0009401; GO:0015796; GO:0016301; GO:0019402; GO:0030295; GO:0090584; GO:1902495`

## Notes

PTS system galactitol-specific EIIA component (EIIB-Gat) (Galactitol-specific phosphotransferase enzyme IIA component)
