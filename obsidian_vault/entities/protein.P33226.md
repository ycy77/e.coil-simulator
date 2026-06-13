---
entity_id: "protein.P33226"
entity_type: "protein"
name: "torC"
source_database: "UniProt"
source_id: "P33226"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Single-pass type II membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "torC b0996 JW0981"
---

# torC

`protein.P33226`

## Static

- Type: `protein`
- Source: `UniProt:P33226`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Single-pass type II membrane protein.

## Enriched Summary

FUNCTION: Part of the anaerobic respiratory chain of trimethylamine-N-oxide reductase TorA which acts by transferring electrons from the membranous menaquinones to TorA (PubMed:11056172, PubMed:39769096). This transfer probably involves an electron transfer pathway from menaquinones to the N-terminal domain of TorC, then from the N-terminus to the C-terminus, and finally to TorA (PubMed:11056172). TorC apocytochrome negatively autoregulates the torCAD operon probably by inhibiting the TorS kinase activity (PubMed:10411745, PubMed:11562502). {ECO:0000269|PubMed:10411745, ECO:0000269|PubMed:11056172, ECO:0000269|PubMed:11562502, ECO:0000269|PubMed:39769096}. TorC is a pentaheme c-type cytochrome that is anchored to the inner membrane . The protein is predicted to be largely hydrophilic but contains a small stretch of hydrophobic amino acids towards the N-terminus . TorC is required for anaerobic growth in the presence of trimethylamine N-oxide; TorC shuttles electrons from a membrane quinol to TorA in the periplasm...

## Biological Role

Component of menaquinol:trimethylamine N-oxide oxidoreductase I (complex.ecocyc.TMAOREDUCTI-CPLX).

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the anaerobic respiratory chain of trimethylamine-N-oxide reductase TorA which acts by transferring electrons from the membranous menaquinones to TorA (PubMed:11056172, PubMed:39769096). This transfer probably involves an electron transfer pathway from menaquinones to the N-terminal domain of TorC, then from the N-terminus to the C-terminus, and finally to TorA (PubMed:11056172). TorC apocytochrome negatively autoregulates the torCAD operon probably by inhibiting the TorS kinase activity (PubMed:10411745, PubMed:11562502). {ECO:0000269|PubMed:10411745, ECO:0000269|PubMed:11056172, ECO:0000269|PubMed:11562502, ECO:0000269|PubMed:39769096}.

## Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TMAOREDUCTI-CPLX|complex.ecocyc.TMAOREDUCTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0996|gene.b0996]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33226`
- `KEGG:ecj:JW0981;eco:b0996;ecoc:C3026_06070;`
- `GeneID:75204082;946252;`
- `GO:GO:0005506; GO:0005886; GO:0006885; GO:0009055; GO:0009060; GO:0009061; GO:0009276; GO:0009968; GO:0016020; GO:0019645; GO:0020037; GO:0030288; GO:1904852`

## Notes

Cytochrome c-type protein TorC
