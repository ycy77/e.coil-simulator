---
entity_id: "protein.P07364"
entity_type: "protein"
name: "cheR"
source_database: "UniProt"
source_id: "P07364"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cheR cheX b1884 JW1873"
---

# cheR

`protein.P07364`

## Static

- Type: `protein`
- Source: `UniProt:P07364`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Methylation of the membrane-bound methyl-accepting chemotaxis proteins (MCP) to form gamma-glutamyl methyl ester residues in MCP. cheR encodes an S-adenosylmethionine-dependent methyltransferase; CheR methylates specific glutamate residues in the cytoplasmic domains of the methyl-accepting chemotaxis proteins (MCPs) CPLX0-8103 "Tsr", CPLX0-8102 "Tar", CPLX0-8105 "Trg" and CPLX0-8104 "Tap". Together, the CheR methyltransferase and the CHEB-MONOMER "CheB" deamidase/methylesterase modulate the level of chemoreceptor methylation in a feedback loop that enables the cell to adapt to chemotactic stimuli (see reviews ). In the absence of chemoeffector gradients the adaption enzymes CheR and CheB promote synchronous rotational switching of flagellar motors which supports the characteristic run-and-tumble swimming behaviour . CheR, from Salmonella typhimurium has been well characterized and used in experiments examining methylation of E. coli chemoreceptors (see for example ); the S. typhimurium CheR methyltransferase is expected to be functionally identical to the E. coli homolog . Mutants defective in cheR (formerly cheX) function are non-chemotactic and lack MCP methyltransferase activity .

## Biological Role

Catalyzes S-adenosyl-L-methionine:protein-L-glutamate O-methyltransferase (reaction.R02623), CHER-RXN (reaction.ecocyc.CHER-RXN), CHERTAPM-RXN (reaction.ecocyc.CHERTAPM-RXN), CHERTARM-RXN (reaction.ecocyc.CHERTARM-RXN), CHERTRGM-RXN (reaction.ecocyc.CHERTRGM-RXN), CHERTSRM-RXN (reaction.ecocyc.CHERTSRM-RXN), RXN-19922 (reaction.ecocyc.RXN-19922).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

FUNCTION: Methylation of the membrane-bound methyl-accepting chemotaxis proteins (MCP) to form gamma-glutamyl methyl ester residues in MCP.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.R02623|reaction.R02623]] `KEGG` `database` - via EC:2.1.1.80
- `catalyzes` --> [[reaction.ecocyc.CHER-RXN|reaction.ecocyc.CHER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CHERTAPM-RXN|reaction.ecocyc.CHERTAPM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CHERTARM-RXN|reaction.ecocyc.CHERTARM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CHERTRGM-RXN|reaction.ecocyc.CHERTRGM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CHERTSRM-RXN|reaction.ecocyc.CHERTSRM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19922|reaction.ecocyc.RXN-19922]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1884|gene.b1884]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07364`
- `KEGG:ecj:JW1873;eco:b1884;ecoc:C3026_10715;`
- `GeneID:946396;`
- `GO:GO:0005829; GO:0005886; GO:0006935; GO:0008276; GO:0008983; GO:0032259; GO:0035556; GO:0098561`
- `EC:2.1.1.80`

## Notes

Chemotaxis protein methyltransferase (EC 2.1.1.80)
