---
entity_id: "protein.P25527"
entity_type: "protein"
name: "gabP"
source_database: "UniProt"
source_id: "P25527"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11311234, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:9806886}; Multi-pass membrane protein {ECO:0000269|PubMed:9806886}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gabP b2663 JW2638"
---

# gabP

`protein.P25527`

## Static

- Type: `protein`
- Source: `UniProt:P25527`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11311234, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:9806886}; Multi-pass membrane protein {ECO:0000269|PubMed:9806886}.

## Enriched Summary

FUNCTION: Transporter for gamma-aminobutyrate (GABA) (PubMed:8297211, PubMed:8557687). Transport is driven by the membrane potential (PubMed:8297211). Can also transport a number of GABA analogs such as nipecotic acid or muscimol (PubMed:8557687). {ECO:0000269|PubMed:8297211, ECO:0000269|PubMed:8557687}. GabP mediates the uptake of 4-aminobutanoate, the zwitterionic form of γ-aminobutyric acid (GABA). gabP encodes a predicted integral membrane protein; moderate overexpression of cloned gabP enhances uptake of labeled GABA; GabP is a high affinity GABA transporter that is driven by membrane potential . Both open chain and cyclic analogs of GABA (eg. 5-aminopentanoate, piperidine-3-carboxylate) are effective inhibitors of GABA transport ; GabP transports a range of structurally diverse GABA analogs . Experimental topology analysis suggests the protein contains 12 transmembrane domains with the N and C-termini located in the cytoplasm . GabP mediated transport of GABA is dependent upon the presence of phosphatidylethanolamine (PE) within the membrane; in cells lacking PE, the N-terminal hairpin domain of GabP is misorganized and transport function is compromised . GabP is a member of the Amino Acid Transporter Family within the Amino Acid-Polyamine-Organocation (APC) Superfamily of transporters . Early studies isolated and characterized mutants in E...

## Biological Role

Catalyzes 5-aminopentanaote:H+ symport (reaction.ecocyc.TRANS-RXN-384), 4-aminobutanoate:proton symport (reaction.ecocyc.TRANS-RXN-57). Transports 4-Aminobutanoate (molecule.C00334), 5-Aminopentanoate (molecule.C00431), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Transporter for gamma-aminobutyrate (GABA) (PubMed:8297211, PubMed:8557687). Transport is driven by the membrane potential (PubMed:8297211). Can also transport a number of GABA analogs such as nipecotic acid or muscimol (PubMed:8557687). {ECO:0000269|PubMed:8297211, ECO:0000269|PubMed:8557687}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-384|reaction.ecocyc.TRANS-RXN-384]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-57|reaction.ecocyc.TRANS-RXN-57]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00334|molecule.C00334]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00431|molecule.C00431]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2663|gene.b2663]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25527`
- `KEGG:ecj:JW2638;eco:b2663;ecoc:C3026_14680;`
- `GeneID:93779349;948049;`
- `GO:GO:0005886; GO:0006974; GO:0006995; GO:0009450; GO:0015185; GO:0015291; GO:0015812; GO:0016020; GO:0090549`

## Notes

Gamma-aminobutyric acid permease (GABA permease) (4-aminobutyrate carrier) (4-aminobutyrate permease) (Gamma-aminobutyrate permease)
