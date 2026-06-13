---
entity_id: "protein.P30855"
entity_type: "protein"
name: "evgS"
source_database: "UniProt"
source_id: "P30855"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:24957621, ECO:0000269|PubMed:24995530}; Single-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "evgS b2370 JW2367"
---

# evgS

`protein.P30855`

## Static

- Type: `protein`
- Source: `UniProt:P30855`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:24957621, ECO:0000269|PubMed:24995530}; Single-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system EvgS/EvgA (PubMed:9535079). Histidine kinase that phosphorylates EvgA via a four-step phosphorelay in response to environmental signals (PubMed:26151934, PubMed:9535079). Involved in adaptation to low pH environments and the control of acid resistance genes (PubMed:24957621, PubMed:24995530, PubMed:29140975). {ECO:0000269|PubMed:24957621, ECO:0000269|PubMed:24995530, ECO:0000269|PubMed:26151934, ECO:0000269|PubMed:29140975, ECO:0000269|PubMed:9535079}. This is the His-721 phosphorylated form of EVGS-MONOMER "EvgS" - the sensor histidine kinase of the EvgSA two-component signal transduction system. This is the His-1137 phosphorylated form of EVGS-MONOMER EvgS - the sensor histidine kinase of the EvgSA two-component signal transduction system. This is the Asp-1009 phosphorylated form of EVGS-MONOMER "EvgS" - the sensor histidine kinase of the EvgSA two-component signal transduction system.

## Biological Role

Component of sensor histidine kinase EvgS (complex.ecocyc.CPLX0-8314).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system EvgS/EvgA (PubMed:9535079). Histidine kinase that phosphorylates EvgA via a four-step phosphorelay in response to environmental signals (PubMed:26151934, PubMed:9535079). Involved in adaptation to low pH environments and the control of acid resistance genes (PubMed:24957621, PubMed:24995530, PubMed:29140975). {ECO:0000269|PubMed:24957621, ECO:0000269|PubMed:24995530, ECO:0000269|PubMed:26151934, ECO:0000269|PubMed:29140975, ECO:0000269|PubMed:9535079}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8314|complex.ecocyc.CPLX0-8314]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2370|gene.b2370]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30855`
- `KEGG:ecj:JW2367;eco:b2370;`
- `GeneID:946844;`
- `GO:GO:0000155; GO:0005524; GO:0005829; GO:0005886; GO:0007165; GO:0010038; GO:0010447; GO:0030288`
- `EC:2.7.13.3`

## Notes

Sensor protein EvgS (EC 2.7.13.3) (Sensor histidine protein kinase EvgS)
