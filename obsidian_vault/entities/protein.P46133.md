---
entity_id: "protein.P46133"
entity_type: "protein"
name: "abgT"
source_database: "UniProt"
source_id: "P46133"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "abgT ydaH b1336 JW5822 ECK1332"
---

# abgT

`protein.P46133`

## Static

- Type: `protein`
- Source: `UniProt:P46133`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Essential for aminobenzoyl-glutamate utilization. It catalyzes the concentration-dependent uptake of p-aminobenzoyl-glutamate (PABA-GLU) into the cell and allows accumulation of PABA-GLU to a concentration enabling AbgAB to catalyze cleavage into p-aminobenzoate and glutamate. It also seems to increase the sensitivity to low levels of aminobenzoyl-glutamate. May actually serve physiologically as a transporter for some other molecule, perhaps a dipeptide, and that it transports p-aminobenzoyl-glutamate as a secondary activity. The physiological role of abgABT should be clarified. {ECO:0000269|PubMed:17307853, ECO:0000269|PubMed:20190044}. Subject to experimental manipulation, AbgT mediates the transport of p-aminobenzoyl-glutamate - a folate catabolite; the physiological role of the protein has not been confirmed - it may participate in a folate salvage or recycling pathway or it may function to transport an as-yet undefined molecule. Overexpression of abgT supports the growth of p-aminobenzoate auxotrophs on exogenous p-aminobenzoyl glutamate...

## Biological Role

Catalyzes p-aminobenzoyl glutamate: proton symport (reaction.ecocyc.TRANS-RXN0-452). Transports N-(4-aminobenzoyl)-L-glutamate (molecule.ecocyc.CPD0-889), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Essential for aminobenzoyl-glutamate utilization. It catalyzes the concentration-dependent uptake of p-aminobenzoyl-glutamate (PABA-GLU) into the cell and allows accumulation of PABA-GLU to a concentration enabling AbgAB to catalyze cleavage into p-aminobenzoate and glutamate. It also seems to increase the sensitivity to low levels of aminobenzoyl-glutamate. May actually serve physiologically as a transporter for some other molecule, perhaps a dipeptide, and that it transports p-aminobenzoyl-glutamate as a secondary activity. The physiological role of abgABT should be clarified. {ECO:0000269|PubMed:17307853, ECO:0000269|PubMed:20190044}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-452|reaction.ecocyc.TRANS-RXN0-452]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD0-889|molecule.ecocyc.CPD0-889]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1336|gene.b1336]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46133`
- `KEGG:ecj:JW5822;eco:b1336;`
- `GeneID:945912;`
- `GO:GO:0005886; GO:0006865; GO:0015291; GO:0015293; GO:0015558; GO:0015814; GO:1902604`

## Notes

p-aminobenzoyl-glutamate transport protein (PABA-GLU transport protein)
