---
entity_id: "protein.P76128"
entity_type: "protein"
name: "ddpA"
source_database: "UniProt"
source_id: "P76128"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ddpA yddS b1487 JW5240"
---

# ddpA

`protein.P76128`

## Static

- Type: `protein`
- Source: `UniProt:P76128`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex DdpABCDF, which is probably involved in D,D-dipeptide transport. DdpA is the predicted periplasmic binding protein of a putative ATP-dependent D,D-dipeptide uptake system that may function to import D-alanyl-D-alanine for use as an energy source under starvation conditions . ArcA appears to activate ddpA gene expression under anaerobiosis. A putative ArcA binding site was identified 103 bp upstream of this gene ; but no promoter upstream of it has been identified. Instead, ddpA is transcribed from a promoter that is located usptream of ddpX gene. ddp: D,D-dipeptide

## Biological Role

Component of putative D,D-dipeptide ABC transporter (complex.ecocyc.ABC-59-CPLX).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex DdpABCDF, which is probably involved in D,D-dipeptide transport.

## Pathways

- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-59-CPLX|complex.ecocyc.ABC-59-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1487|gene.b1487]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76128`
- `KEGG:ecj:JW5240;eco:b1487;ecoc:C3026_08615;`
- `GeneID:946052;`
- `GO:GO:0015031; GO:0016020; GO:0030288; GO:0042938; GO:0055052; GO:1904680`

## Notes

Probable D,D-dipeptide-binding periplasmic protein DdpA
