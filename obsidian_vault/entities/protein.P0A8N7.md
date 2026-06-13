---
entity_id: "protein.P0A8N7"
entity_type: "protein"
name: "epmA"
source_database: "UniProt"
source_id: "P0A8N7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "epmA genX poxA yjeA b4155 JW4116"
---

# epmA

`protein.P0A8N7`

## Static

- Type: `protein`
- Source: `UniProt:P0A8N7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: With EpmB is involved in the beta-lysylation step of the post-translational modification of translation elongation factor P (EF-P) on 'Lys-34'. Catalyzes the ATP-dependent activation of (R)-beta-lysine produced by EpmB, forming a lysyl-adenylate, from which the beta-lysyl moiety is then transferred to the epsilon-amino group of EF-P 'Lys-34'. The substrate (R)-beta-lysine is 100-fold more efficient than either (S)-beta-lysine or L-alpha-lysine. Cannot ligate lysine to any tRNA. {ECO:0000255|HAMAP-Rule:MF_00174, ECO:0000269|PubMed:20729861, ECO:0000269|PubMed:21841797, ECO:0000269|PubMed:22128152}.

## Biological Role

Component of EF-P-lysine lysyltransferase (complex.ecocyc.CPLX0-7889).

## Annotation

FUNCTION: With EpmB is involved in the beta-lysylation step of the post-translational modification of translation elongation factor P (EF-P) on 'Lys-34'. Catalyzes the ATP-dependent activation of (R)-beta-lysine produced by EpmB, forming a lysyl-adenylate, from which the beta-lysyl moiety is then transferred to the epsilon-amino group of EF-P 'Lys-34'. The substrate (R)-beta-lysine is 100-fold more efficient than either (S)-beta-lysine or L-alpha-lysine. Cannot ligate lysine to any tRNA. {ECO:0000255|HAMAP-Rule:MF_00174, ECO:0000269|PubMed:20729861, ECO:0000269|PubMed:21841797, ECO:0000269|PubMed:22128152}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7889|complex.ecocyc.CPLX0-7889]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4155|gene.b4155]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8N7`
- `KEGG:ecj:JW4116;eco:b4155;ecoc:C3026_22460;`
- `GeneID:93777667;948672;`
- `GO:GO:0000049; GO:0004824; GO:0005524; GO:0005737; GO:0005829; GO:0006430; GO:0016880; GO:0042803; GO:0052868; GO:0071468`
- `EC:6.3.2.-`

## Notes

Elongation factor P--(R)-beta-lysine ligase (EF-P--(R)-beta-lysine ligase) (EC 6.3.2.-) (EF-P post-translational modification enzyme A) (EF-P-lysine lysyltransferase) (GX)
