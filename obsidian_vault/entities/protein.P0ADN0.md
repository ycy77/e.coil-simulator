---
entity_id: "protein.P0ADN0"
entity_type: "protein"
name: "viaA"
source_database: "UniProt"
source_id: "P0ADN0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:24454883, ECO:0000269|PubMed:36127320}. Cell inner membrane {ECO:0000269|PubMed:24454883, ECO:0000269|PubMed:36127320}; Peripheral membrane protein {ECO:0000269|PubMed:36127320}; Cytoplasmic side {ECO:0000269|PubMed:36127320}. Note=Localizes to the membrane via interaction with specific lipids. {ECO:0000269|PubMed:36127320}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "viaA yieD yieM b3745 JW5610"
---

# viaA

`protein.P0ADN0`

## Static

- Type: `protein`
- Source: `UniProt:P0ADN0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:24454883, ECO:0000269|PubMed:36127320}. Cell inner membrane {ECO:0000269|PubMed:24454883, ECO:0000269|PubMed:36127320}; Peripheral membrane protein {ECO:0000269|PubMed:36127320}; Cytoplasmic side {ECO:0000269|PubMed:36127320}. Note=Localizes to the membrane via interaction with specific lipids. {ECO:0000269|PubMed:36127320}.

## Enriched Summary

FUNCTION: Component of the RavA-ViaA chaperone complex, which may act on the membrane to optimize the function of some of the respiratory chains (PubMed:16301313, PubMed:24454883, PubMed:27979649, PubMed:36127320, PubMed:36625597). ViaA stimulates the ATPase activity of RavA (PubMed:16301313, PubMed:27979649, PubMed:37660904). {ECO:0000269|PubMed:16301313, ECO:0000269|PubMed:24454883, ECO:0000269|PubMed:27979649, ECO:0000269|PubMed:36127320, ECO:0000269|PubMed:36625597, ECO:0000269|PubMed:37660904}.; FUNCTION: The RavA-ViaA system is involved in the regulation of two respiratory complexes, the fumarate reductase (Frd) electron transport complex and the NADH-quinone oxidoreductase complex (NDH-1 or Nuo complex) (PubMed:24454883, PubMed:27979649). It modulates the activity of the Frd complex, signifying a potential regulatory function during bacterial anaerobic respiration with fumarate as the terminal electron acceptor (PubMed:27979649). Interaction of RavA-ViaA with FrdA results in a decrease in Frd activity (PubMed:27979649). It also interacts with the Nuo complex, known to be involved in both the aerobic and the anaerobic respiration (PubMed:24454883). The RavA-ViaA system binds to specific membrane phospholipids, and might chaperone certain respiratory complexes by acting on lipid microdomains in which these complexes are inserted (PubMed:36127320)...

## Annotation

FUNCTION: Component of the RavA-ViaA chaperone complex, which may act on the membrane to optimize the function of some of the respiratory chains (PubMed:16301313, PubMed:24454883, PubMed:27979649, PubMed:36127320, PubMed:36625597). ViaA stimulates the ATPase activity of RavA (PubMed:16301313, PubMed:27979649, PubMed:37660904). {ECO:0000269|PubMed:16301313, ECO:0000269|PubMed:24454883, ECO:0000269|PubMed:27979649, ECO:0000269|PubMed:36127320, ECO:0000269|PubMed:36625597, ECO:0000269|PubMed:37660904}.; FUNCTION: The RavA-ViaA system is involved in the regulation of two respiratory complexes, the fumarate reductase (Frd) electron transport complex and the NADH-quinone oxidoreductase complex (NDH-1 or Nuo complex) (PubMed:24454883, PubMed:27979649). It modulates the activity of the Frd complex, signifying a potential regulatory function during bacterial anaerobic respiration with fumarate as the terminal electron acceptor (PubMed:27979649). Interaction of RavA-ViaA with FrdA results in a decrease in Frd activity (PubMed:27979649). It also interacts with the Nuo complex, known to be involved in both the aerobic and the anaerobic respiration (PubMed:24454883). The RavA-ViaA system binds to specific membrane phospholipids, and might chaperone certain respiratory complexes by acting on lipid microdomains in which these complexes are inserted (PubMed:36127320). The RavA-ViaA system also plays a negative role in bacterial persistence upon treatment with antibiotics through the association of the chaperone complex with Frd (PubMed:37660904). It sensitizes cells to sublethal concentrations of aminoglycoside (AG) antibiotics (PubMed:36127320, PubMed:36625597, PubMed:37660904). The system can facilitate uptake of AG across the membrane when cells are in a low energy state (PubMed:36625597). It sensitizes cells to AG through a proton motive force-dependent mechanism (PubMed:36127320, PubMed:36625597). Under fumarate respiration conditions, it sensitizes cells to AG via a FrdA-dependent mechanism (PubMed:36625597). It does not sensitize cells grown under nitrate respiration to gentamicin (PubMed:36625597). {ECO:0000269|PubMed:24454883, ECO:0000269|PubMed:27979649, ECO:0000269|PubMed:36127320, ECO:0000269|PubMed:36625597, ECO:0000269|PubMed:37660904}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b3745|gene.b3745]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADN0`
- `KEGG:ecj:JW5610;eco:b3745;ecoc:C3026_20290;`
- `GeneID:93778222;948257;`
- `GO:GO:0005829; GO:0005886; GO:0016020`

## Notes

Regulatory protein ViaA (VWA interacting with AAA+ ATPase)
