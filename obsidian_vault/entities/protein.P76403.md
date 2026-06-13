---
entity_id: "protein.P76403"
entity_type: "protein"
name: "trhP"
source_database: "UniProt"
source_id: "P76403"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trhP yegQ b2081 JW2066"
---

# trhP

`protein.P76403`

## Static

- Type: `protein`
- Source: `UniProt:P76403`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in prephenate-dependent formation of 5-hydroxyuridine (ho5U) modification at position 34 in tRNAs, the first step in 5-carboxymethoxyuridine (cmo5U) biosynthesis (PubMed:31253794). Involved differently in ho5U formation in each tRNA; tRNA(Leu3) and tRNA(Pro3) are major targets of TrhP (PubMed:31253794). {ECO:0000269|PubMed:31253794}. A ΔtrhP mutant contains reduced levels of the modified wobble base 5-oxyacetylU34-tRNA "cmo5U34": tRNALeu3 and tRNAPro3 retain only 5% of the wild type level of modification; tRNAAla1 and tRNAVal1 remain ~50% modified, and tRNASer1 and tRNAThr4 show reduced levels of modification. A ΔtrhP trhO double mutant has lost all modification of the U34 wobble base of tRNAVal1 and grows more slowly than wild type. Additional knockout of EG30094 serU, EG30104 thrW or EG30066 proK, which encode tRNAs responsible for decoding G-ending codons, results in further reduction of growth . TrhP requires PREPHENATE as a metabolite for 5-HYDROXYU34-TRNA ho5U34 formation . TrhP belongs to the U32 peptidase family; a prephenate-dependent hydroxylation chemistry that may be shared by U32-family proteins is described by . TrhP binds a single, redox-active CPD-7 [4Fe-4S] iron-sulfur cluster . Mutagenesis of any of the six conserved residues in the peptidase U32 domain of TrhP results in loss of complementation of the mutant strain...

## Annotation

FUNCTION: Involved in prephenate-dependent formation of 5-hydroxyuridine (ho5U) modification at position 34 in tRNAs, the first step in 5-carboxymethoxyuridine (cmo5U) biosynthesis (PubMed:31253794). Involved differently in ho5U formation in each tRNA; tRNA(Leu3) and tRNA(Pro3) are major targets of TrhP (PubMed:31253794). {ECO:0000269|PubMed:31253794}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b2081|gene.b2081]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76403`
- `KEGG:ecj:JW2066;eco:b2081;ecoc:C3026_11700;`
- `GeneID:946609;`
- `GO:GO:0002098; GO:0005829; GO:0006400; GO:0006508; GO:0008233; GO:0051539`
- `EC:3.4.-.-`

## Notes

tRNA hydroxylation protein P (EC 3.4.-.-)
