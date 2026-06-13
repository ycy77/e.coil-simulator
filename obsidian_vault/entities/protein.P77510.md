---
entity_id: "protein.P77510"
entity_type: "protein"
name: "dpiB"
source_database: "UniProt"
source_id: "P77510"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dpiB citA mpdB ybeP b0619 JW0611"
---

# dpiB

`protein.P77510`

## Static

- Type: `protein`
- Source: `UniProt:P77510`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system DpiA/DpiB, which is essential for expression of citrate-specific fermentation genes and genes involved in plasmid inheritance. Could be involved in response to both the presence of citrate and external redox conditions. Functions as a sensor kinase that phosphorylates DpiA in the presence of citrate. {ECO:0000269|PubMed:11889485, ECO:0000269|PubMed:19202292}. Represents the His-347 phosphorylated form of G6345-MONOMER "DpiB" - the sensor histidine kinase of the DpiBA two-component signal transduction system. DpiB is the membrane associated sensor kinase of the DpiAB two component system which regulates the expression of genes involved in co-substrate dependent anaerobic citrate fermentation. Sequence analysis suggests that DpiB contains a periplasmic sensing domain surrounded by two transmembrane segments plus a cytoplasmic effector domain . The purified periplasmic domain of DpiB has a high affinity for citrate in vitro; it also binds isocitrate and tricarballylate . DpiB is suggested to be a redox sensitive, citrate sensing histidine kinase; autophosphorylation of the purified cytoplasmic domain of DpiB (DpiB-C) is enhanced in the presence of dithiothreitol; transfer of the phosphate group to DpiA has not been conclusively demonstrated...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system DpiA/DpiB, which is essential for expression of citrate-specific fermentation genes and genes involved in plasmid inheritance. Could be involved in response to both the presence of citrate and external redox conditions. Functions as a sensor kinase that phosphorylates DpiA in the presence of citrate. {ECO:0000269|PubMed:11889485, ECO:0000269|PubMed:19202292}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0619|gene.b0619]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77510`
- `KEGG:ecj:JW0611;eco:b0619;ecoc:C3026_03095;`
- `GeneID:945233;`
- `GO:GO:0000155; GO:0000160; GO:0004673; GO:0005524; GO:0005829; GO:0005886; GO:0006355; GO:0009927; GO:0030288`
- `EC:2.7.13.3`

## Notes

Sensor histidine kinase DpiB (EC 2.7.13.3) (Sensor histidine kinase CitA)
