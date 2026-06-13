---
entity_id: "protein.P76491"
entity_type: "protein"
name: "yfbR"
source_database: "UniProt"
source_id: "P76491"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01100, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yfbR b2291 JW2288"
---

# yfbR

`protein.P76491`

## Static

- Type: `protein`
- Source: `UniProt:P76491`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01100, ECO:0000305}.

## Enriched Summary

FUNCTION: Essential component of the deoxycytidine triphosphate (dCTP) pathway for de novo synthesis of thymidylate. Catalyzes the strictly specific dephosphorylation of 2'-deoxyribonucleoside 5'-monophosphates (dAMP, dGMP, dTMP, dUMP, dIMP and dCMP) and does not dephosphorylate 5'-ribonucleotides or ribonucleoside 3'-monophosphates. {ECO:0000269|PubMed:15489502, ECO:0000269|PubMed:17827303, ECO:0000269|PubMed:18353368}. YfbR is a 5'-deoxynucleotidase that functions as a dCMP phosphohydrolase in a salvage pathway for the synthesis of dUMP in a dcd deoA mutant . The protein contains a conserved HD domain . YfbR has phosphatase activity with deoxyribonucleoside 5'-monophosphates and does not hydrolyze ribonucleotides or deoxyribonucloside 3'-monophosphates. The enzyme requires divalent metal cations for activity . Nucleotidase activity of YfbR was discovered in a high-throughput screen of purified proteins . Crystal structures of YfbR have been solved; based on an analysis of crystal packing and size-exclusion chromatography, it was suggested that the biological unit is a dimer. Site-directed mutagenesis confirmed the importance of certain conserved active site residues, and mechanisms for substrate selectivity and catalysis were proposed . yfbR and alaA may form an operon .

## Biological Role

Component of dCMP phosphohydrolase (complex.ecocyc.CPLX0-7625).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Essential component of the deoxycytidine triphosphate (dCTP) pathway for de novo synthesis of thymidylate. Catalyzes the strictly specific dephosphorylation of 2'-deoxyribonucleoside 5'-monophosphates (dAMP, dGMP, dTMP, dUMP, dIMP and dCMP) and does not dephosphorylate 5'-ribonucleotides or ribonucleoside 3'-monophosphates. {ECO:0000269|PubMed:15489502, ECO:0000269|PubMed:17827303, ECO:0000269|PubMed:18353368}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7625|complex.ecocyc.CPLX0-7625]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2291|gene.b2291]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76491`
- `KEGG:ecj:JW2288;eco:b2291;ecoc:C3026_12780;`
- `GeneID:946771;`
- `GO:GO:0000166; GO:0002953; GO:0005737; GO:0006226; GO:0010139; GO:0042802; GO:0050897`
- `EC:3.1.3.89`

## Notes

5'-deoxynucleotidase YfbR (EC 3.1.3.89) (5'-deoxyribonucleotidase) (Nucleoside 5'-monophosphate phosphohydrolase)
