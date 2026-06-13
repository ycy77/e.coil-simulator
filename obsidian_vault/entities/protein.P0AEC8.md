---
entity_id: "protein.P0AEC8"
entity_type: "protein"
name: "dcuS"
source_database: "UniProt"
source_id: "P0AEC8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:12167640, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dcuS yjdH b4125 JW4086"
---

# dcuS

`protein.P0AEC8`

## Static

- Type: `protein`
- Source: `UniProt:P0AEC8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:12167640, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system DcuR/DcuS (PubMed:12167640, PubMed:9765574, PubMed:9973351). Involved in the C4-dicarboxylate-stimulated regulation of the genes encoding the anaerobic fumarate respiratory system (frdABCD; nuoAN; dcuB; sdhCDAB; etc.) (PubMed:9765574, PubMed:9973351). Weakly regulates the aerobic C4-dicarboxylate transporter dctA (PubMed:9973351). Activates DcuR by phosphorylation (PubMed:12167640). {ECO:0000269|PubMed:12167640, ECO:0000269|PubMed:9765574, ECO:0000269|PubMed:9973351}. Represents the His-349 phosphorylated form of CPLX0-8307 DcuS - the sensor histidine kinase of the DcuSR two-component signal transduction system.

## Biological Role

Component of DcuS-DcuB sensor complex (complex.ecocyc.CPLX0-8304), DcuS-DctA sensor complex (complex.ecocyc.CPLX0-8306), sensor histidine kinase DcuS (complex.ecocyc.CPLX0-8307).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system DcuR/DcuS (PubMed:12167640, PubMed:9765574, PubMed:9973351). Involved in the C4-dicarboxylate-stimulated regulation of the genes encoding the anaerobic fumarate respiratory system (frdABCD; nuoAN; dcuB; sdhCDAB; etc.) (PubMed:9765574, PubMed:9973351). Weakly regulates the aerobic C4-dicarboxylate transporter dctA (PubMed:9973351). Activates DcuR by phosphorylation (PubMed:12167640). {ECO:0000269|PubMed:12167640, ECO:0000269|PubMed:9765574, ECO:0000269|PubMed:9973351}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8304|complex.ecocyc.CPLX0-8304]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-8306|complex.ecocyc.CPLX0-8306]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-8307|complex.ecocyc.CPLX0-8307]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4125|gene.b4125]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEC8`
- `KEGG:ecj:JW4086;eco:b4125;ecoc:C3026_22295;`
- `GeneID:75169643;948639;`
- `GO:GO:0000155; GO:0000160; GO:0004673; GO:0005524; GO:0005829; GO:0005886; GO:0006355; GO:0007165; GO:0009365; GO:0030288; GO:0042802`
- `EC:2.7.13.3`

## Notes

Sensor histidine kinase DcuS (EC 2.7.13.3) (Fumarate sensor)
