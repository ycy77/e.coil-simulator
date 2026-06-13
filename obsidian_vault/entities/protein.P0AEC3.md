---
entity_id: "protein.P0AEC3"
entity_type: "protein"
name: "arcB"
source_database: "UniProt"
source_id: "P0AEC3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "arcB b3210 JW5536"
---

# arcB

`protein.P0AEC3`

## Static

- Type: `protein`
- Source: `UniProt:P0AEC3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system ArcB/ArcA. Sensor-regulator protein for anaerobic repression of the arc modulon. Activates ArcA via a four-step phosphorelay. ArcB can also dephosphorylate ArcA by a reverse phosphorelay involving His-717 and Asp-576. This is the histidine-717 phosphorylated form of ARCB-MONOMER "ArcB" - the sensor histidine kinase of the ArcAB two-component signal transduction system. This is the aspartate-576 phosphorylated form of ARCB-CPLX "ArcB" - the sensor histidine kinase of the ArcAB two-component signal transduction system. This is the histidine-292 phosphorylated form of ARCB-CPLX "ArcB" - the sensor histidine kinase of the ArcAB two-component signal transduction system. ArcB is the sensor histidine kinase of the ArcAB two-component system which mediates anaerobic repression of numerous enzymes associated with aerobic metabolism . ArcB is an integral membrane protein with a significant cytoplasmic domain; the protein contains two transmembrane regions and three cytoplasmic modules - a primary transmitter module with a conserved histidine residue (His-292), a receiver module with a conserved aspartate residue (Asp-576) and an alternative transmitter module with a conserved histidine (His-717)...

## Biological Role

Component of sensor histidine kinase ArcB (complex.ecocyc.ARCB-CPLX).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system ArcB/ArcA. Sensor-regulator protein for anaerobic repression of the arc modulon. Activates ArcA via a four-step phosphorelay. ArcB can also dephosphorylate ArcA by a reverse phosphorelay involving His-717 and Asp-576.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ARCB-CPLX|complex.ecocyc.ARCB-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3210|gene.b3210]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEC3`
- `KEGG:ecj:JW5536;eco:b3210;ecoc:C3026_17465;`
- `GeneID:93778771;947887;`
- `GO:GO:0000155; GO:0004721; GO:0005524; GO:0005829; GO:0005886; GO:0006355; GO:0007165; GO:0046777; GO:0070482`
- `EC:2.7.13.3`

## Notes

Aerobic respiration control sensor protein ArcB (EC 2.7.13.3)
