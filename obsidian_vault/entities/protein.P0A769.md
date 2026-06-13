---
entity_id: "protein.P0A769"
entity_type: "protein"
name: "mntH"
source_database: "UniProt"
source_id: "P0A769"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00221, ECO:0000269|PubMed:14607838}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00221, ECO:0000269|PubMed:14607838}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mntH yfeP b2392 JW2388"
---

# mntH

`protein.P0A769`

## Static

- Type: `protein`
- Source: `UniProt:P0A769`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00221, ECO:0000269|PubMed:14607838}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00221, ECO:0000269|PubMed:14607838}.

## Enriched Summary

FUNCTION: H(+)-stimulated, divalent metal cation uptake system. Involved in manganese and iron uptake. Can also transport cadmium, cobalt, zinc and to a lesser extent nickel and copper. Involved in response to reactive oxygen. {ECO:0000255|HAMAP-Rule:MF_00221, ECO:0000269|PubMed:10712688, ECO:0000269|PubMed:10844693}. Early studies indicated that E. coli is able to accumulate manganese by means of a highly-specific active transport system . mntH encodes a proton-dependent divalent metal ion transporter with a marked preference for Mn2+; MntH does transport ferrous iron but this is not expected to be physiologically relevant; Cd2+ is an alternative, non-physiological substrate . ΔmntH cells grow normally, but their manganese content is minimal and activity of the manganese-dependent superoxide dismutase SUPEROX-DISMUTMN-CPLX SodA is virtually absent; manganese import is essential in H2O2-stressed cells; manganese is not an efficient scavenger of reactive oxygen species; manganese may substitute for iron in some metalloenzymes making them less vulnerable to to oxidative damage . Manganese import protects RIBULP3EPIM-MONOMER from irreversible damage during H2O2 stress . MntH-mediated manganese import facilitates the recovery of DNA replication after H2O2 exposure; accumulation of intracellular manganese increases cell survival to acute oxidative stress (see also )...

## Biological Role

Catalyzes Mn2+:proton symport (reaction.ecocyc.TRANS-RXN-241). Transports hν (molecule.ecocyc.Light), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

FUNCTION: H(+)-stimulated, divalent metal cation uptake system. Involved in manganese and iron uptake. Can also transport cadmium, cobalt, zinc and to a lesser extent nickel and copper. Involved in response to reactive oxygen. {ECO:0000255|HAMAP-Rule:MF_00221, ECO:0000269|PubMed:10712688, ECO:0000269|PubMed:10844693}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-241|reaction.ecocyc.TRANS-RXN-241]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2392|gene.b2392]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A769`
- `KEGG:ecj:JW2388;eco:b2392;ecoc:C3026_13295;`
- `GeneID:93774737;946899;`
- `GO:GO:0005384; GO:0005886; GO:0006824; GO:0006826; GO:0006828; GO:0006879; GO:0015078; GO:0015086; GO:0015293; GO:0015691; GO:0030001; GO:0030026; GO:0034599; GO:0034755; GO:0046872; GO:0140967`

## Notes

Divalent metal cation transporter MntH
