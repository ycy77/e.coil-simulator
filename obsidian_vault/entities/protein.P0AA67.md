---
entity_id: "protein.P0AA67"
entity_type: "protein"
name: "rhtA"
source_database: "UniProt"
source_id: "P0AA67"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:12648727}; Multi-pass membrane protein {ECO:0000269|PubMed:12648727}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rhtA ybiF b0813 JW0798"
---

# rhtA

`protein.P0AA67`

## Static

- Type: `protein`
- Source: `UniProt:P0AA67`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:12648727}; Multi-pass membrane protein {ECO:0000269|PubMed:12648727}.

## Enriched Summary

FUNCTION: Involved in the efflux of threonine and homoserine. Can also export other amino acids such as proline, serine, histidine and cysteine. {ECO:0000269|PubMed:12648727}. RhtA can mediate export of L-threonine and L-homoserine and likely operates as a substrate:proton antiporter; the physiological role of the transporter remains unclear. Increased expression of rhtA confers increased resistance to L-homoserine, L-threonine and some other amino acids (proline, serine, cysteine, histidine) and amino acid analogues . Increased expression of rhtA increases L-threonine production in a threonine producing strain and L-homoserine production in an L-homoserine producing strain; addition of the protonophore CPD-7970 results in a significant reduction in the rate of export . Heterologous expression of rhtA increases L-threonine and L-homoserine production in a Corynebacterium glutamicum threonine producing strain . RhtA is a membrane protein with 10 predicted transmembrane segments RhtA is a member of the 10 TMS Drug/Metabolite Exporter (DME) family of transporters within the Drug/Metabolite Transporter (DMT) superfamily . rht: resistance to homoserine and threonine

## Biological Role

Catalyzes L-homoserine:proton antiport (reaction.ecocyc.TRANS-RXN-242), L-threonine:proton antiport (reaction.ecocyc.TRANS-RXN0-0244). Transports L-Homoserine (molecule.C00263), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Involved in the efflux of threonine and homoserine. Can also export other amino acids such as proline, serine, histidine and cysteine. {ECO:0000269|PubMed:12648727}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-242|reaction.ecocyc.TRANS-RXN-242]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-0244|reaction.ecocyc.TRANS-RXN0-0244]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00263|molecule.C00263]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0813|gene.b0813]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA67`
- `KEGG:ecj:JW0798;eco:b0813;ecoc:C3026_05120;`
- `GeneID:93776615;947045;`
- `GO:GO:0005886; GO:0015291; GO:0015565; GO:0015826; GO:0042968; GO:0042970`

## Notes

Threonine/homoserine exporter RhtA
