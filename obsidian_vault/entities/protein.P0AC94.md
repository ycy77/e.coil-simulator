---
entity_id: "protein.P0AC94"
entity_type: "protein"
name: "gntP"
source_database: "UniProt"
source_id: "P0AC94"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gntP yjiB b4321 JW4284"
---

# gntP

`protein.P0AC94`

## Static

- Type: `protein`
- Source: `UniProt:P0AC94`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: High-affinity gluconate transporter with fairly broad specificity, including low affinity for glucuronate, several disaccharides, and some hexoses, but not glucose. GntP is a member of the GntP family transporters and is homologous to the E. coli GntT and GntU gluconate transporters. GntP transports D-fructuronate/D-gluconate . Whole cell experiments have shown that the cloned gntP gene confers gluconate transport with a Km of approx 25 μM, but its expression is not induced by gluconate . gntP gene is induced by fructuronate, the first intermediate of the glucuronate metabolism pathway. It is a member of UxuR regulon which is composed of genes induced by glucuronate via its conversion to fructuronate and these genes are repressed by UxuR . gntP mutants were unable to grow using fructuronate as their sole carbon source. Taken together, these results indicate that GntP is the primary fructuronate transporter . gntP was predicted to be a target of the small RNA OmrB. Overexpression of both OmrB and OmrA decreases the expression of gntP . gntP was found to be downregulated in a MG1655 lysogen carrying the Stx2a phage PA8 .

## Biological Role

Catalyzes fructuronate:proton symport (reaction.ecocyc.TRANS-RXN-81), D-gluconate:proton symport (reaction.ecocyc.TRANS-RXN0-209). Transports D-Gluconic acid (molecule.C00257), D-Fructuronate (molecule.C00905), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: High-affinity gluconate transporter with fairly broad specificity, including low affinity for glucuronate, several disaccharides, and some hexoses, but not glucose.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-81|reaction.ecocyc.TRANS-RXN-81]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-209|reaction.ecocyc.TRANS-RXN0-209]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00257|molecule.C00257]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00905|molecule.C00905]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b4321|gene.b4321]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC94`
- `KEGG:ecj:JW4284;eco:b4321;ecoc:C3026_23340;`
- `GeneID:948848;`
- `GO:GO:0005351; GO:0005886; GO:0015128; GO:0016020; GO:0019521; GO:0035429`

## Notes

High-affinity gluconate transporter (Gluconate permease 3) (Gnt-III system)
