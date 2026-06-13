---
entity_id: "protein.P37188"
entity_type: "protein"
name: "gatB"
source_database: "UniProt"
source_id: "P37188"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:8955298}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gatB b2093 JW2077"
---

# gatB

`protein.P37188`

## Static

- Type: `protein`
- Source: `UniProt:P37188`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:8955298}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. The enzyme II complex composed of GatA, GatB and GatC is involved in galactitol transport. It can also use D-glucitol. {ECO:0000269|PubMed:1100608, ECO:0000269|PubMed:8955298}. GatB has sequence similarity to the IIB protein of the ascorbate PTS and to IIBSgc (the IIB protein of a predicted PTS of unknown specificity) . gatB sequenced from a wild-type isolate of E. coli, strain EC3132, encodes a small hydrophilic protein .

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

- `encodes` <-- [[gene.b2093|gene.b2093]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37188`
- `KEGG:ecj:JW2077;eco:b2093;ecoc:C3026_11750;`
- `GeneID:946610;`
- `GO:GO:0005829; GO:0008982; GO:0009401; GO:0015796; GO:0019402; GO:0090584; GO:1902495`
- `EC:2.7.1.200`

## Notes

PTS system galactitol-specific EIIB component (EIIB-Gat) (Galactitol-specific phosphotransferase enzyme IIB component) (EC 2.7.1.200)
