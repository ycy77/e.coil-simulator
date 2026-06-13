---
entity_id: "protein.P21866"
entity_type: "protein"
name: "kdpE"
source_database: "UniProt"
source_id: "P21866"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:1532388}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kdpE b0694 JW5096"
---

# kdpE

`protein.P21866`

## Static

- Type: `protein`
- Source: `UniProt:P21866`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:1532388}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system KdpD/KdpE involved in the regulation of the kdp operon. {ECO:0000269|PubMed:1532388}.

## Biological Role

Component of DNA-binding transcriptional dual regulator KdpE-phosphorylated (complex.ecocyc.CPLX0-7795).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system KdpD/KdpE involved in the regulation of the kdp operon. {ECO:0000269|PubMed:1532388}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (7)

- `activates` --> [[gene.b0696|gene.b0696]] `RegulonDB` `C` - regulator=KdpE; target=kdpC; function=+
- `activates` --> [[gene.b0697|gene.b0697]] `RegulonDB` `C` - regulator=KdpE; target=kdpB; function=+
- `activates` --> [[gene.b0698|gene.b0698]] `RegulonDB` `C` - regulator=KdpE; target=kdpA; function=+
- `activates` --> [[gene.b4513|gene.b4513]] `RegulonDB` `C` - regulator=KdpE; target=kdpF; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7795|complex.ecocyc.CPLX0-7795]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0953|gene.b0953]] `RegulonDB` `S` - regulator=KdpE; target=rmf; function=-
- `represses` --> [[gene.b3995|gene.b3995]] `RegulonDB` `S` - regulator=KdpE; target=rsd; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0694|gene.b0694]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21866`
- `KEGG:ecj:JW5096;eco:b0694;ecoc:C3026_03465;`
- `GeneID:945302;`
- `GO:GO:0000156; GO:0000976; GO:0000987; GO:0001216; GO:0003700; GO:0005829; GO:0006355; GO:0032993; GO:0042803`

## Notes

KDP operon transcriptional regulatory protein KdpE
