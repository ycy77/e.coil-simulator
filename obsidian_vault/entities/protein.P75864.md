---
entity_id: "protein.P75864"
entity_type: "protein"
name: "rlmL"
source_database: "UniProt"
source_id: "P75864"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rlmL rlmK rlmKL ycbY b0948 JW0931"
---

# rlmL

`protein.P75864`

## Static

- Type: `protein`
- Source: `UniProt:P75864`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Specifically methylates the guanine in position 2445 (m2G2445) and the guanine in position 2069 (m7G2069) of 23S rRNA. Methylation occurs before assembly of 23S rRNA into 50S subunits. {ECO:0000269|PubMed:17010378, ECO:0000269|PubMed:22210896, ECO:0000269|PubMed:22362734}. RlmL is a fused dual methyltransferase responsible for methylation of 23S rRNA at the N2 position of the G2445 nucleotide as well as at the N7 position of the G2069 nucleotide . Both nucleotides are part of helix 54, and RlmL has RNA helicase activity that is able to unwind this region during substrate recognition and methylation . In vitro, recombinant RlmL is able to methylate naked 23S rRNA, but not 23S rRNA assembled into the 50S ribosomal subunit . Both m2G and m7G were shown to be formed during early steps of 50S ribosomal subunit assembly . The RlmL protein contains an N-terminal THUMP domain followed by two methyltransferase domains. Analysis of point mutants in the predicted active sites allowed separation of the RlmK (G2069 methyltransferase, C-terminal domain) and RlmL (G2445 methyltransferase, N-terminal domain) functions. RlmK activity enhances the efficiency of RlmL activity . The N- and C-terminal halves can be expressed separately and restore methylation at their respective target nucleotides...

## Biological Role

Catalyzes RXN-11574 (reaction.ecocyc.RXN-11574), RXN0-6950 (reaction.ecocyc.RXN0-6950).

## Annotation

FUNCTION: Specifically methylates the guanine in position 2445 (m2G2445) and the guanine in position 2069 (m7G2069) of 23S rRNA. Methylation occurs before assembly of 23S rRNA into 50S subunits. {ECO:0000269|PubMed:17010378, ECO:0000269|PubMed:22210896, ECO:0000269|PubMed:22362734}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-11574|reaction.ecocyc.RXN-11574]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6950|reaction.ecocyc.RXN0-6950]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0948|gene.b0948]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75864`
- `KEGG:ecj:JW0931;eco:b0948;ecoc:C3026_05805;`
- `GeneID:945564;`
- `GO:GO:0003723; GO:0005737; GO:0008990; GO:0031167; GO:0052915; GO:0070043; GO:0070475`
- `EC:2.1.1.173; 2.1.1.264`

## Notes

Ribosomal RNA large subunit methyltransferase K/L [Includes: 23S rRNA m2G2445 methyltransferase (EC 2.1.1.173) (rRNA (guanine-N(2)-)-methyltransferase RlmL); 23S rRNA m7G2069 methyltransferase (EC 2.1.1.264) (rRNA (guanine-N(7)-)-methyltransferase RlmK)]
