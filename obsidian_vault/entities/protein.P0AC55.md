---
entity_id: "protein.P0AC55"
entity_type: "protein"
name: "glnK"
source_database: "UniProt"
source_id: "P0AC55"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:11847102, ECO:0000269|PubMed:14668330, ECO:0000269|PubMed:16864585}. Cell inner membrane {ECO:0000269|PubMed:11847102, ECO:0000269|PubMed:14668330, ECO:0000269|PubMed:16864585}. Note=During nitrogen limitation, GlnK is predominantly in its fully uridylylated state in the cytoplasmic fraction. In response to nitrogen shock, GlnK is deuridylylated rapidly and associates tightly with AmtB in the inner membrane. {ECO:0000269|PubMed:11847102, ECO:0000269|PubMed:14668330, ECO:0000269|PubMed:16864585}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glnK ybaI b0450 JW0440"
---

# glnK

`protein.P0AC55`

## Static

- Type: `protein`
- Source: `UniProt:P0AC55`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:11847102, ECO:0000269|PubMed:14668330, ECO:0000269|PubMed:16864585}. Cell inner membrane {ECO:0000269|PubMed:11847102, ECO:0000269|PubMed:14668330, ECO:0000269|PubMed:16864585}. Note=During nitrogen limitation, GlnK is predominantly in its fully uridylylated state in the cytoplasmic fraction. In response to nitrogen shock, GlnK is deuridylylated rapidly and associates tightly with AmtB in the inner membrane. {ECO:0000269|PubMed:11847102, ECO:0000269|PubMed:14668330, ECO:0000269|PubMed:16864585}.

## Enriched Summary

FUNCTION: Involved in the regulation of nitrogen metabolism (PubMed:10760266, PubMed:11847102, PubMed:12366843, PubMed:14668330, PubMed:28538158, PubMed:8843440). Regulates the activity of its targets by protein-protein interaction in response to the nitrogen status of the cell (PubMed:10760266, PubMed:11847102, PubMed:14668330, PubMed:8843440). Involved in the regulation of the ammonium transporter AmtB so as to optimize ammonium uptake under all growth conditions (PubMed:11847102, PubMed:14668330, PubMed:16864585). In nitrogen-limited conditions, GlnK does not interact with AmtB, which remains active and imports ammonium. When extracellular ammonium increases, GlnK associates tightly with AmtB in the inner membrane, thereby inhibiting the transporter activity (PubMed:11847102, PubMed:14668330, PubMed:16864585). Also involved in the regulation of the glutamine synthetase adenylyltransferase/adenylyl-removing (AT/AR) enzyme GlnE and the glutamine synthetase GlnA (PubMed:10760266, PubMed:28538158, PubMed:8843440). In nitrogen-limited conditions, formation of uridylylated GlnB(PII)/GlnK heterotrimers may fine-regulate the activation of GlnA: uridylylated heterotrimers stimulate the deadenylation and the activation of GlnA whereas uridylylated GlnK homotrimers do not stimulate, or hardly stimulate, the deadenylation of GlnA (PubMed:10760266)...

## Biological Role

Component of uridylyl-[protein PII-2] (complex.ecocyc.CPLX0-8570), nitrogen regulatory protein PII-2 (complex.ecocyc.PII2-CPLX).

## Annotation

FUNCTION: Involved in the regulation of nitrogen metabolism (PubMed:10760266, PubMed:11847102, PubMed:12366843, PubMed:14668330, PubMed:28538158, PubMed:8843440). Regulates the activity of its targets by protein-protein interaction in response to the nitrogen status of the cell (PubMed:10760266, PubMed:11847102, PubMed:14668330, PubMed:8843440). Involved in the regulation of the ammonium transporter AmtB so as to optimize ammonium uptake under all growth conditions (PubMed:11847102, PubMed:14668330, PubMed:16864585). In nitrogen-limited conditions, GlnK does not interact with AmtB, which remains active and imports ammonium. When extracellular ammonium increases, GlnK associates tightly with AmtB in the inner membrane, thereby inhibiting the transporter activity (PubMed:11847102, PubMed:14668330, PubMed:16864585). Also involved in the regulation of the glutamine synthetase adenylyltransferase/adenylyl-removing (AT/AR) enzyme GlnE and the glutamine synthetase GlnA (PubMed:10760266, PubMed:28538158, PubMed:8843440). In nitrogen-limited conditions, formation of uridylylated GlnB(PII)/GlnK heterotrimers may fine-regulate the activation of GlnA: uridylylated heterotrimers stimulate the deadenylation and the activation of GlnA whereas uridylylated GlnK homotrimers do not stimulate, or hardly stimulate, the deadenylation of GlnA (PubMed:10760266). In addition, regulates the expression of Ntr genes during nitrogen starvation, probably via the control of the levels of phosphorylated NRI during different stages of the response to nitrogen limitation (PubMed:12366843). {ECO:0000269|PubMed:10760266, ECO:0000269|PubMed:11847102, ECO:0000269|PubMed:12366843, ECO:0000269|PubMed:14668330, ECO:0000269|PubMed:16864585, ECO:0000269|PubMed:28538158, ECO:0000269|PubMed:8843440}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8570|complex.ecocyc.CPLX0-8570]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.PII2-CPLX|complex.ecocyc.PII2-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0450|gene.b0450]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC55`
- `KEGG:ecj:JW0440;eco:b0450;ecoc:C3026_02205;`
- `GeneID:86862995;93777000;945087;`
- `GO:GO:0005524; GO:0005829; GO:0005886; GO:0006808; GO:0030234; GO:0042802; GO:0045848`

## Notes

Nitrogen regulatory protein GlnK (Nitrogen regulatory protein P-II 2) (PII-like protein)
