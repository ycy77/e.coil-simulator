---
entity_id: "protein.P75792"
entity_type: "protein"
name: "ybiV"
source_database: "UniProt"
source_id: "P75792"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybiV supH b0822 JW0806"
---

# ybiV

`protein.P75792`

## Static

- Type: `protein`
- Source: `UniProt:P75792`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of sugar phosphate to sugar and inorganic phosphate. Has a wide substrate specificity catalyzing the hydrolysis of ribose-5-phosphate, glucose-6-phosphate, fructose-1-phosphate, acetyl-phosphate, glycerol-1-phosphate, glycerol-2-phosphate, 2-deoxy-glucose-6-phosphate, mannose-6-phosphate and fructose-6-phosphate. Appears to have a low level of phosphotransferase activity using monophosphates as the phosphate donor. {ECO:0000269|PubMed:15657928, ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279}. YbiV is a sugar phosphatase belonging to the family of type II haloacid dehalogenase (HAD)-like hydrolases . It shows a low level of discrimination between its preferred substrates . In addition, YbiV appears to have a low level of phosphotransferase activity using monophosphates as the phosphate donor . The phosphatase activity of YbiV was also discovered in a high-throughput screen of purified proteins . Crystal structures of YbiV have been solved, and a catalytic mechanism was suggested . YbiV may exist as a homodimer in solution . Overexpression of YbiV in an engineered strain that converts pentoses to glucose increases the glucose yield .

## Biological Role

Catalyzes sugar-phosphate phosphohydrolase (reaction.R00804), SUGAR-PHOSPHATASE-RXN (reaction.ecocyc.SUGAR-PHOSPHATASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: Catalyzes the hydrolysis of sugar phosphate to sugar and inorganic phosphate. Has a wide substrate specificity catalyzing the hydrolysis of ribose-5-phosphate, glucose-6-phosphate, fructose-1-phosphate, acetyl-phosphate, glycerol-1-phosphate, glycerol-2-phosphate, 2-deoxy-glucose-6-phosphate, mannose-6-phosphate and fructose-6-phosphate. Appears to have a low level of phosphotransferase activity using monophosphates as the phosphate donor. {ECO:0000269|PubMed:15657928, ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00804|reaction.R00804]] `KEGG` `database` - via EC:3.1.3.23
- `catalyzes` --> [[reaction.ecocyc.SUGAR-PHOSPHATASE-RXN|reaction.ecocyc.SUGAR-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0822|gene.b0822]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75792`
- `KEGG:ecj:JW0806;eco:b0822;ecoc:C3026_05165;`
- `GeneID:945432;`
- `GO:GO:0000287; GO:0005829; GO:0016791; GO:0050286; GO:0050308; GO:0103026`
- `EC:3.1.3.23`

## Notes

Sugar phosphatase YbiV (EC 3.1.3.23)
