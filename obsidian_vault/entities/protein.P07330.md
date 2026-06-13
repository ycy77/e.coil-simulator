---
entity_id: "protein.P07330"
entity_type: "protein"
name: "cheB"
source_database: "UniProt"
source_id: "P07330"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00099, ECO:0000269|PubMed:358191}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cheB b1883 JW1872"
---

# cheB

`protein.P07330`

## Static

- Type: `protein`
- Source: `UniProt:P07330`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00099, ECO:0000269|PubMed:358191}.

## Enriched Summary

FUNCTION: Involved in chemotaxis (PubMed:2188960, PubMed:324984, PubMed:358191, PubMed:392505). Part of a chemotaxis signal transduction system that modulates chemotaxis in response to various stimuli (PubMed:2188960, PubMed:392505). Catalyzes the demethylation of specific methylglutamate residues introduced into the chemoreceptors (methyl-accepting chemotaxis proteins or MCP) by CheR (PubMed:2188960, PubMed:358191, PubMed:392505). Also mediates the irreversible deamidation of specific glutamine residues to glutamic acid (PubMed:6300110, PubMed:6304723). Catalyzes its own deactivation by removing the activating phosphoryl group (PubMed:2188960). {ECO:0000269|PubMed:2188960, ECO:0000269|PubMed:324984, ECO:0000269|PubMed:358191, ECO:0000269|PubMed:392505, ECO:0000269|PubMed:6300110, ECO:0000269|PubMed:6304723}. This is the Asp56 phosphorylated form of the chemotaxis response regulator CheB. CheB is one of two response regulators in chemotactic two component signaling pathways; CheB receives a phosphoryl group from the histidine kinase CheA; CheB-phosphate catalyses the irreversible deamidation of specific glutamine residues and the hydrolysis of specific methylated glutamates in the chemoreceptor proteins CPLX0-8103 "Tsr", CPLX0-8102 "Tar", CPLX0-8105 "Trg" and CPLX0-8104 "Tap"...

## Biological Role

Catalyzes protein glutamine amidohydrolase (reaction.R02622), protein-L-glutamate-O4-methyl-ester acylhydrolase (reaction.R02624), CHEBDEAMID-RXN (reaction.ecocyc.CHEBDEAMID-RXN), CHEBTAPD-RXN (reaction.ecocyc.CHEBTAPD-RXN), CHEBTARD-RXN (reaction.ecocyc.CHEBTARD-RXN), CHEBTRGD-RXN (reaction.ecocyc.CHEBTRGD-RXN), CHEBTSRD-RXN (reaction.ecocyc.CHEBTSRD-RXN), MCPMETEST-RXN (reaction.ecocyc.MCPMETEST-RXN), and 4 more.

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

FUNCTION: Involved in chemotaxis (PubMed:2188960, PubMed:324984, PubMed:358191, PubMed:392505). Part of a chemotaxis signal transduction system that modulates chemotaxis in response to various stimuli (PubMed:2188960, PubMed:392505). Catalyzes the demethylation of specific methylglutamate residues introduced into the chemoreceptors (methyl-accepting chemotaxis proteins or MCP) by CheR (PubMed:2188960, PubMed:358191, PubMed:392505). Also mediates the irreversible deamidation of specific glutamine residues to glutamic acid (PubMed:6300110, PubMed:6304723). Catalyzes its own deactivation by removing the activating phosphoryl group (PubMed:2188960). {ECO:0000269|PubMed:2188960, ECO:0000269|PubMed:324984, ECO:0000269|PubMed:358191, ECO:0000269|PubMed:392505, ECO:0000269|PubMed:6300110, ECO:0000269|PubMed:6304723}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Outgoing Edges (12)

- `catalyzes` --> [[reaction.R02622|reaction.R02622]] `KEGG` `database` - via EC:3.5.1.44
- `catalyzes` --> [[reaction.R02624|reaction.R02624]] `KEGG` `database` - via EC:3.1.1.61
- `catalyzes` --> [[reaction.ecocyc.CHEBDEAMID-RXN|reaction.ecocyc.CHEBDEAMID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CHEBTAPD-RXN|reaction.ecocyc.CHEBTAPD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CHEBTARD-RXN|reaction.ecocyc.CHEBTARD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CHEBTRGD-RXN|reaction.ecocyc.CHEBTRGD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CHEBTSRD-RXN|reaction.ecocyc.CHEBTSRD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.MCPMETEST-RXN|reaction.ecocyc.MCPMETEST-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.MCPTAP-RXN|reaction.ecocyc.MCPTAP-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.MCPTAR-RXN|reaction.ecocyc.MCPTAR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.MCPTRG-RXN|reaction.ecocyc.MCPTRG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.MCPTSR-RXN|reaction.ecocyc.MCPTSR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1883|gene.b1883]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07330`
- `KEGG:ecj:JW1872;eco:b1883;ecoc:C3026_10710;`
- `GeneID:946394;`
- `GO:GO:0000156; GO:0005829; GO:0005886; GO:0006935; GO:0007165; GO:0008984; GO:0035556; GO:0050568; GO:1990827`
- `EC:3.1.1.61; 3.5.1.44`

## Notes

Protein-glutamate methylesterase/protein-glutamine glutaminase (EC 3.1.1.61) (EC 3.5.1.44) (Chemotaxis response regulator protein-glutamate methylesterase/glutamine deamidase) (Methyl-accepting chemotaxis proteins-specific methylesterase/deamidase) (MCP-specific methylesterase/deamidase)
