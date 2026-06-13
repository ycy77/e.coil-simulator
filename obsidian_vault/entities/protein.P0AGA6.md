---
entity_id: "protein.P0AGA6"
entity_type: "protein"
name: "uhpA"
source_database: "UniProt"
source_id: "P0AGA6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uhpA b3669 JW3644"
---

# uhpA

`protein.P0AGA6`

## Static

- Type: `protein`
- Source: `UniProt:P0AGA6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the UhpABC signaling cascade that controls the expression of the hexose phosphate transporter UhpT. Activates the transcription of the uhpT gene. Acts by binding specifically to the uhpT promoter region. {ECO:0000269|PubMed:3038843, ECO:0000269|PubMed:8999880}.

## Biological Role

Component of DNA-binding transcriptional activator UhpA-phosphorylated (complex.ecocyc.CPLX0-7754).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the UhpABC signaling cascade that controls the expression of the hexose phosphate transporter UhpT. Activates the transcription of the uhpT gene. Acts by binding specifically to the uhpT promoter region. {ECO:0000269|PubMed:3038843, ECO:0000269|PubMed:8999880}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (3)

- `activates` --> [[gene.b3666|gene.b3666]] `RegulonDB` `C` - regulator=UhpA; target=uhpT; function=+
- `activates` --> [[gene.b4829|gene.b4829]] `RegulonDB` `C` - regulator=UhpA; target=uhpU; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7754|complex.ecocyc.CPLX0-7754]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3669|gene.b3669]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGA6`
- `KEGG:ecj:JW3644;eco:b3669;ecoc:C3026_19885;`
- `GeneID:93778410;948178;`
- `GO:GO:0000160; GO:0000976; GO:0003677; GO:0003700; GO:0005737; GO:0006355`

## Notes

Transcriptional regulatory protein UhpA
