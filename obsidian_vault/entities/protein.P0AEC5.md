---
entity_id: "protein.P0AEC5"
entity_type: "protein"
name: "barA"
source_database: "UniProt"
source_id: "P0AEC5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "barA b2786 JW2757"
---

# barA

`protein.P0AEC5`

## Static

- Type: `protein`
- Source: `UniProt:P0AEC5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system UvrY/BarA involved in the regulation of carbon metabolism via the CsrA/CsrB regulatory system (PubMed:12193630, PubMed:12533459). Phosphorylates UvrY, probably via a four-step phosphorelay (PubMed:11022030). {ECO:0000269|PubMed:11022030, ECO:0000269|PubMed:12193630, ECO:0000269|PubMed:12533459}. Represents the Asp-718 phosphorylated form of BARA-MONOMER "BarA" - the sensor histidine kinase of the BarA/UvrY two-component signal transduction system. Represents the His-302 phosphorylated form of BARA-MONOMER "BarA" - the sensor histidine kinase of the BarA/UvrY two-component signal transduction system. Represents the His-861 phosphorylated form of BARA-MONOMER "BarA" - the sensor histidine kinase of the BarA/UvrY two-component signal transduction system.

## Biological Role

Component of sensor histidine kinase BarA (complex.ecocyc.CPLX0-8302).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system UvrY/BarA involved in the regulation of carbon metabolism via the CsrA/CsrB regulatory system (PubMed:12193630, PubMed:12533459). Phosphorylates UvrY, probably via a four-step phosphorelay (PubMed:11022030). {ECO:0000269|PubMed:11022030, ECO:0000269|PubMed:12193630, ECO:0000269|PubMed:12533459}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8302|complex.ecocyc.CPLX0-8302]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2786|gene.b2786]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEC5`
- `KEGG:ecj:JW2757;eco:b2786;ecoc:C3026_15320;`
- `GeneID:75172870;75203823;947255;`
- `GO:GO:0000155; GO:0004673; GO:0004721; GO:0005524; GO:0005886; GO:0007165; GO:0009927; GO:0010034; GO:0042542; GO:0042803; GO:1901425`
- `EC:2.7.13.3`

## Notes

Signal transduction histidine-protein kinase BarA (EC 2.7.13.3)
