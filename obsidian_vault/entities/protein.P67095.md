---
entity_id: "protein.P67095"
entity_type: "protein"
name: "yfcE"
source_database: "UniProt"
source_id: "P67095"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yfcE b2300 JW5377"
---

# yfcE

`protein.P67095`

## Static

- Type: `protein`
- Source: `UniProt:P67095`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Shows phosphodiesterase activity (PubMed:15808744, PubMed:17586769, PubMed:18757371). Shows significant activity toward bis-p-nitrophenyl phosphate (bis-pNPP), an artificial substrate commonly used to detect phosphodiesterase activity (PubMed:15808744, PubMed:17586769, PubMed:18757371). Also hydrolyzes, with lower efficiency, two other artificial phosphodiesterase substrates, thymidine 5'-monophosphate p-nitrophenyl ester (pNP-TMP) and p-nitrophenylphosphorylcholine (pNPPC) (PubMed:15808744, PubMed:17586769). Shows phosphomonoesterase activity toward p-nitrophenyl phosphate (pNPP), with much lower catalytic efficiency (PubMed:18757371). No activity was detected against a wide variety of naturally occurring phosphomonoesters and phosphodiesters, including various 2',3'- and 3',5'-cyclic nucleotides, suggesting that YfcE is highly specific for its physiological substrate, which is not yet known (PubMed:17586769). {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:17586769, ECO:0000269|PubMed:18757371}.

## Biological Role

Component of phosphodiesterase YfcE (complex.ecocyc.CPLX0-8248).

## Annotation

FUNCTION: Shows phosphodiesterase activity (PubMed:15808744, PubMed:17586769, PubMed:18757371). Shows significant activity toward bis-p-nitrophenyl phosphate (bis-pNPP), an artificial substrate commonly used to detect phosphodiesterase activity (PubMed:15808744, PubMed:17586769, PubMed:18757371). Also hydrolyzes, with lower efficiency, two other artificial phosphodiesterase substrates, thymidine 5'-monophosphate p-nitrophenyl ester (pNP-TMP) and p-nitrophenylphosphorylcholine (pNPPC) (PubMed:15808744, PubMed:17586769). Shows phosphomonoesterase activity toward p-nitrophenyl phosphate (pNPP), with much lower catalytic efficiency (PubMed:18757371). No activity was detected against a wide variety of naturally occurring phosphomonoesters and phosphodiesters, including various 2',3'- and 3',5'-cyclic nucleotides, suggesting that YfcE is highly specific for its physiological substrate, which is not yet known (PubMed:17586769). {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:17586769, ECO:0000269|PubMed:18757371}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8248|complex.ecocyc.CPLX0-8248]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2300|gene.b2300]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P67095`
- `KEGG:ecj:JW5377;eco:b2300;`
- `GeneID:946755;`
- `GO:GO:0005829; GO:0008081; GO:0030145; GO:0032991; GO:0042802`
- `EC:3.1.4.-`

## Notes

Phosphodiesterase YfcE (EC 3.1.4.-)
