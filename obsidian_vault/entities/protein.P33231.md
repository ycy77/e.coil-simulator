---
entity_id: "protein.P33231"
entity_type: "protein"
name: "lldP"
source_database: "UniProt"
source_id: "P33231"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lldP lctP b3603 JW3578"
---

# lldP

`protein.P33231`

## Static

- Type: `protein`
- Source: `UniProt:P33231`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Uptake of L-lactate across the membrane (PubMed:11283302, PubMed:11785976). Can also transport D-lactate and glycolate (PubMed:11283302, PubMed:11785976). Seems to be driven by a proton motive force (PubMed:11785976). {ECO:0000269|PubMed:11283302, ECO:0000269|PubMed:11785976}. LldP is an inner membrane permease that functions in the the uptake of L-lactate, D-lactate and glycolate . The lldP gene is located in a lactate-inducible operon with the lldD and lldR genes encoding a lactate dehydrogenase and a regulatory protein, respectively . E.coli strains lacking both 2-hydroxymonocarboxylate transporters LldP and B2975-MONOMER "GlcA" are unable to grow with D-lactate, L-lactate or glyoxylate as sole carbon source. Overexpression of a plasmid carrying lldP restores growth of the double mutant on all three substrates . Transport is abolished by addition of the proton ionophore, carbonyl cyanide m-chlorophenylhydrazone (CCCP) . Disruption of the lld operon decreased lactate transport, which could be restored by complementation with the cloned lldP gene . Glycolate does not induce expression of the lld operon - basal expression of lldP is sufficient to transport this substrate at a rate which supports growth .

## Biological Role

Catalyzes lactate:proton symport (reaction.ecocyc.TRANS-RXN-104), glycolate:proton symport (reaction.ecocyc.TRANS-RXN-105), lactate:proton symport (reaction.ecocyc.TRANS-RXN0-515), hydroxybutanoate:proton symport (reaction.ecocyc.TRANS-RXN0-622). Transports Glycolate (molecule.C00160), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Uptake of L-lactate across the membrane (PubMed:11283302, PubMed:11785976). Can also transport D-lactate and glycolate (PubMed:11283302, PubMed:11785976). Seems to be driven by a proton motive force (PubMed:11785976). {ECO:0000269|PubMed:11283302, ECO:0000269|PubMed:11785976}.

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-104|reaction.ecocyc.TRANS-RXN-104]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-105|reaction.ecocyc.TRANS-RXN-105]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-515|reaction.ecocyc.TRANS-RXN0-515]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-622|reaction.ecocyc.TRANS-RXN0-622]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00160|molecule.C00160]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3603|gene.b3603]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33231`
- `KEGG:ecj:JW3578;eco:b3603;ecoc:C3026_19540;`
- `GeneID:948114;`
- `GO:GO:0005886; GO:0006974; GO:0015129; GO:0015295; GO:0035873; GO:0043879`

## Notes

L-lactate permease
