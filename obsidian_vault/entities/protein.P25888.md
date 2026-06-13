---
entity_id: "protein.P25888"
entity_type: "protein"
name: "rhlE"
source_database: "UniProt"
source_id: "P25888"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00968, ECO:0000269|PubMed:18083833}. Note=Ribosome-associated. Can either bind to the intact 70S ribosome or to individual ribosomal subunits."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rhlE b0797 JW0781"
---

# rhlE

`protein.P25888`

## Static

- Type: `protein`
- Source: `UniProt:P25888`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00968, ECO:0000269|PubMed:18083833}. Note=Ribosome-associated. Can either bind to the intact 70S ribosome or to individual ribosomal subunits.

## Enriched Summary

FUNCTION: DEAD-box RNA helicase involved in ribosome assembly. Has RNA-dependent ATPase activity and unwinds double-stranded RNA. May play a role in the interconversion of ribosomal RNA-folding intermediates that are further processed by DeaD or SrmB during ribosome maturation. {ECO:0000255|HAMAP-Rule:MF_00968, ECO:0000269|PubMed:15196029, ECO:0000269|PubMed:18083833}. RhlE is a ribosome-associated factor that may be involved in ribosome maturation . RhlE is a member of the DEAD-box-containing ATP-dependent RNA helicase family . Its ATPase activity is stimulated by both long RNAs and short oligoribonucleotides . Of the three E. coli DEAD-box RNA helicases DeaD, SrmB and RhlE, only RhlE can unwind substrates with short or no single-stranded extensions, but the enzyme shows low processivity . RhlE physically interacts with EG10690-MONOMER and EG10859-MONOMER . RhlE can functionally replace RhlB within the degradosome . An rhlE mutant does not have any obvious growth defect . Overexpression of RhlE can substitute for the essential function of DeaD during cold shock , but exacerbates the cold-sensitive growth defect of an srmB mutant . Conversely, the cold-sensitive growth defect of an rhlE deaD double mutant is enhanced, while that of an rhlE srmB double mutant is alleviated . Both DeaD and SrmB are involved in ribosome maturation, indicating that RhlE may play a similar role...

## Biological Role

Catalyzes RXN-24178 (reaction.ecocyc.RXN-24178).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

FUNCTION: DEAD-box RNA helicase involved in ribosome assembly. Has RNA-dependent ATPase activity and unwinds double-stranded RNA. May play a role in the interconversion of ribosomal RNA-folding intermediates that are further processed by DeaD or SrmB during ribosome maturation. {ECO:0000255|HAMAP-Rule:MF_00968, ECO:0000269|PubMed:15196029, ECO:0000269|PubMed:18083833}.

## Pathways

- `eco03018` RNA degradation (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-24178|reaction.ecocyc.RXN-24178]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0797|gene.b0797]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25888`
- `KEGG:ecj:JW0781;eco:b0797;ecoc:C3026_05035;`
- `GeneID:75204912;945425;`
- `GO:GO:0003723; GO:0003724; GO:0005524; GO:0005829; GO:0009408; GO:0016887; GO:0042255`
- `EC:3.6.4.13`

## Notes

ATP-dependent RNA helicase RhlE (EC 3.6.4.13)
