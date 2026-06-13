---
entity_id: "protein.P32125"
entity_type: "protein"
name: "mobB"
source_database: "UniProt"
source_id: "P32125"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mobB yihC b3856 JW5575"
---

# mobB

`protein.P32125`

## Static

- Type: `protein`
- Source: `UniProt:P32125`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: GTP-binding protein that is not required for the biosynthesis of Mo-molybdopterin guanine dinucleotide (Mo-MGD) cofactor, and not necessary for the formation of active molybdoenzymes using this form of molybdenum cofactor. May act as an adapter protein to achieve the efficient biosynthesis and utilization of MGD. Displays a weak intrinsic GTPase activity. Is also able to bind the nucleotides ATP, TTP and GDP, but with lower affinity than GTP. {ECO:0000269|PubMed:12682065, ECO:0000269|PubMed:9219527}.

## Biological Role

Component of molybdopterin-guanine dinucleotide biosynthesis adaptor protein (complex.ecocyc.CPLX0-8044).

## Annotation

FUNCTION: GTP-binding protein that is not required for the biosynthesis of Mo-molybdopterin guanine dinucleotide (Mo-MGD) cofactor, and not necessary for the formation of active molybdoenzymes using this form of molybdenum cofactor. May act as an adapter protein to achieve the efficient biosynthesis and utilization of MGD. Displays a weak intrinsic GTPase activity. Is also able to bind the nucleotides ATP, TTP and GDP, but with lower affinity than GTP. {ECO:0000269|PubMed:12682065, ECO:0000269|PubMed:9219527}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8044|complex.ecocyc.CPLX0-8044]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3856|gene.b3856]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32125`
- `KEGG:ecj:JW5575;eco:b3856;ecoc:C3026_20845;`
- `GeneID:948343;`
- `GO:GO:0005525; GO:0006777; GO:0042803`

## Notes

Molybdopterin-guanine dinucleotide biosynthesis adapter protein (MGD biosynthesis adapter protein) (Molybdenum cofactor biosynthesis adapter protein) (Moco biosynthesis adapter protein) (Molybdopterin-guanine dinucleotide biosynthesis protein B)
