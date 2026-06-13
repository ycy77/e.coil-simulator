---
entity_id: "protein.P76346"
entity_type: "protein"
name: "mtfA"
source_database: "UniProt"
source_id: "P76346"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01593, ECO:0000269|PubMed:16855233}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mtfA yeeI b1976 JW1958"
---

# mtfA

`protein.P76346`

## Static

- Type: `protein`
- Source: `UniProt:P76346`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01593, ECO:0000269|PubMed:16855233}.

## Enriched Summary

FUNCTION: Involved in the modulation of the activity of the glucose-phosphotransferase system (glucose-PTS) (PubMed:16855233). Interacts with the transcriptional repressor Mlc, preventing its interaction with DNA and leading to the modulation of expression of genes regulated by Mlc, including ptsG, which encodes the PTS system glucose-specific EIICB component (PubMed:16855233, PubMed:22178967). {ECO:0000269|PubMed:16855233, ECO:0000269|PubMed:22178967}.; FUNCTION: Shows zinc-dependent metallopeptidase activity (By similarity). In vitro, can cleave several artificial substrates (PubMed:22178967). The greatest activity and specificity is observed for L-alanine fused to 4-nitroanilide (L-alanine-pNA) (PubMed:22178967). Shows significantly lower activity towards L-arginine-pNA, L-proline-pNA, hippuryl-L-phenylalanine and hippuryl-L-arginine, and cannot use FTC-casein (PubMed:22178967). Mlc does not appear to be a biologically relevant peptidase substrate (PubMed:22178967). Biologically relevant targets may have a function in growth transition under changing environmental conditions (PubMed:22178967). {ECO:0000250|UniProtKB:A6TB83, ECO:0000269|PubMed:22178967}. MtfA interacts with the transcriptional repressor PD01896 Mlc, thereby modulating the expression of genes which are regulated by Mlc . Binding of MtfA to Mlc prevents interaction of Mlc with the ptsG operator region...

## Biological Role

Catalyzes RXN0-5052 (reaction.ecocyc.RXN0-5052).

## Annotation

FUNCTION: Involved in the modulation of the activity of the glucose-phosphotransferase system (glucose-PTS) (PubMed:16855233). Interacts with the transcriptional repressor Mlc, preventing its interaction with DNA and leading to the modulation of expression of genes regulated by Mlc, including ptsG, which encodes the PTS system glucose-specific EIICB component (PubMed:16855233, PubMed:22178967). {ECO:0000269|PubMed:16855233, ECO:0000269|PubMed:22178967}.; FUNCTION: Shows zinc-dependent metallopeptidase activity (By similarity). In vitro, can cleave several artificial substrates (PubMed:22178967). The greatest activity and specificity is observed for L-alanine fused to 4-nitroanilide (L-alanine-pNA) (PubMed:22178967). Shows significantly lower activity towards L-arginine-pNA, L-proline-pNA, hippuryl-L-phenylalanine and hippuryl-L-arginine, and cannot use FTC-casein (PubMed:22178967). Mlc does not appear to be a biologically relevant peptidase substrate (PubMed:22178967). Biologically relevant targets may have a function in growth transition under changing environmental conditions (PubMed:22178967). {ECO:0000250|UniProtKB:A6TB83, ECO:0000269|PubMed:22178967}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5052|reaction.ecocyc.RXN0-5052]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1976|gene.b1976]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76346`
- `KEGG:ecj:JW1958;eco:b1976;ecoc:C3026_11165;`
- `GeneID:75172093;75205786;946489;`
- `GO:GO:0004177; GO:0005829; GO:0006508; GO:0008237; GO:0008270`
- `EC:3.4.11.-`

## Notes

Mlc titration factor A (Mlc-binding protein) (Probable zinc metallopeptidase MtfA) (EC 3.4.11.-)
