---
entity_id: "protein.P0A8F4"
entity_type: "protein"
name: "udk"
source_database: "UniProt"
source_id: "P0A8F4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "udk b2066 JW2051"
---

# udk

`protein.P0A8F4`

## Static

- Type: `protein`
- Source: `UniProt:P0A8F4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Uridine kinase (EC 2.7.1.48) (Cytidine monophosphokinase) (Uridine monophosphokinase) Uridine-cytidine kinase phosphorylates both uridine and cytidine; GTP and dGTP are the most efficient phosphate donors . Uridine-cytidine kinase was found to have a molecular weight of 90,000 by gel filtration and is thus likely not monomeric . Overexpression of uridine-cytidine kinase inhibits growth of the bacteriophage T7, particularly in a T7 gp0.7 mutant , due to inadequate inhibition of host RNA polymerase . Overexpression of Udk mimics the absence of Gp2 during T7 infection .

## Biological Role

Catalyzes ATP:cytidine 5'-phosphotransferase (reaction.R00513), GTP:cytidine 5'-phosphotransferase (reaction.R00517), CYTIDINEKIN-RXN (reaction.ecocyc.CYTIDINEKIN-RXN), CYTIKIN-RXN (reaction.ecocyc.CYTIKIN-RXN), URIDINEKIN-RXN (reaction.ecocyc.URIDINEKIN-RXN), GTP:uridine 5'-phosphotransferase (reaction.ecocyc.URKI-RXN).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

Uridine kinase (EC 2.7.1.48) (Cytidine monophosphokinase) (Uridine monophosphokinase)

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.R00513|reaction.R00513]] `KEGG` `database` - via EC:2.7.1.48
- `catalyzes` --> [[reaction.R00517|reaction.R00517]] `KEGG` `database` - via EC:2.7.1.48
- `catalyzes` --> [[reaction.ecocyc.CYTIDINEKIN-RXN|reaction.ecocyc.CYTIDINEKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CYTIKIN-RXN|reaction.ecocyc.CYTIKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.URIDINEKIN-RXN|reaction.ecocyc.URIDINEKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.URKI-RXN|reaction.ecocyc.URKI-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2066|gene.b2066]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8F4`
- `KEGG:ecj:JW2051;eco:b2066;ecoc:C3026_11620;`
- `GeneID:89516832;93775125;946597;`
- `GO:GO:0004849; GO:0005524; GO:0005737; GO:0005829; GO:0043771; GO:0044206; GO:0044211`
- `EC:2.7.1.48`

## Notes

Uridine kinase (EC 2.7.1.48) (Cytidine monophosphokinase) (Uridine monophosphokinase)
