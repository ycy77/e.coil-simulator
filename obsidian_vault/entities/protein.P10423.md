---
entity_id: "protein.P10423"
entity_type: "protein"
name: "iap"
source_database: "UniProt"
source_id: "P10423"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "iap b2753 JW2723"
---

# iap

`protein.P10423`

## Static

- Type: `protein`
- Source: `UniProt:P10423`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This protein, presumably an aminopeptidase, mediates the conversion of E.coli alkaline phosphatase isozyme 1, to isozymes 2 and 3 by removing, one by one, the two N-terminal arginine residues. Alkaline phosphatase isozyme conversion protein is responsible for the stepwise removal of the two amino-terminal arginines from alkaline phosphatase isozyme 1, creating isozymes 2 and 3 in the process . This is presumably an aminopeptidase activity, as it can be inhibited by protease inhibitors . Alkaline phosphatase isozyme conversion protein has a characteristic signal peptide at its amino-terminus and can be found as both full-length and signal-peptide-cleaved forms in the cell. It is a membrane-associated protein that acts in the periplasm . Efficieny of secretion of alkaline phosphatase isozyme conversion protein is reduced when phosphatidylethanolamine is depleted, resulting in less effective modification of alkaline phosphatase .

## Biological Role

Catalyzes RXN0-3261 (reaction.ecocyc.RXN0-3261).

## Annotation

FUNCTION: This protein, presumably an aminopeptidase, mediates the conversion of E.coli alkaline phosphatase isozyme 1, to isozymes 2 and 3 by removing, one by one, the two N-terminal arginine residues.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-3261|reaction.ecocyc.RXN0-3261]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2753|gene.b2753]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P10423`
- `KEGG:ecj:JW2723;eco:b2753;ecoc:C3026_15135;`
- `GeneID:947215;`
- `GO:GO:0004177; GO:0006508; GO:0008235; GO:0030288; GO:0043687; GO:0046872`
- `EC:3.4.11.-`

## Notes

Alkaline phosphatase isozyme conversion protein (EC 3.4.11.-)
