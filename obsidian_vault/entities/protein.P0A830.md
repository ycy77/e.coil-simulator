---
entity_id: "protein.P0A830"
entity_type: "protein"
name: "dctA"
source_database: "UniProt"
source_id: "P0A830"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dctA b3528 JW3496"
---

# dctA

`protein.P0A830`

## Static

- Type: `protein`
- Source: `UniProt:P0A830`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Responsible for the aerobic transport of the dicarboxylates fumarate, L- and D-malate and to a lesser extent succinate, from the periplasm across the inner membrane. {ECO:0000269|PubMed:17088549}. DctA is required for dicarboxylate transport . DctA is a proton motive force-dependent C4-dicarboxylate transporter, responsible for the uptake of fumarate, succinate, L-aspartate and L- and D-malate under aerobic conditions, and also for the uptake of orotate, a pyrimidine precursor . The substrate recognition site of DctA is located on the outer surface of the inner membrane . DctA and DcuB function as co-sensors with DCUS-MONOMER "DcuS" - the sensor histidine kinase of the two-component system that controls the expression of genes required for C4-dicarboxylate degradation. DcuS requires the transport proteins DctA or DcuB for normal function. DctA interacts specifically with DcuS in vivo . DctA is predicted to contain eight transmembrane helices with the N and C-termini located in the cytoplasm. Residues important for interaction with DcuS are located in α-helix 8b . DctA's role in the DctA-DcuS sensor complex is not dependent on transport function - DctA mutants with uncoupled regulatory and transport function can be isolated and DctA-DcuS sensor function can be activated by substrates such as citrate that are not transported by DctA...

## Biological Role

Catalyzes succinate:proton symport (reaction.ecocyc.TRANS-RXN-121), malate:proton symport (reaction.ecocyc.TRANS-RXN-121A), orotate:proton symport (reaction.ecocyc.TRANS-RXN-121C), aspartate:proton symport (reaction.ecocyc.TRANS-RXN-122A), malate:proton symport (reaction.ecocyc.TRANS-RXN0-451), C4-dicarboxylate:proton symport (reaction.ecocyc.TRANS-RXN0-517), fumarate:proton symport (reaction.ecocyc.TRANS-RXN0-553). Transports Fumarate (molecule.C00122), (S)-Malate (molecule.C00149), Orotate (molecule.C00295), (R)-Malate (molecule.C00497), a C4-dicarboxylate (molecule.ecocyc.C4-dicarboxylates). Component of DcuS-DctA sensor complex (complex.ecocyc.CPLX0-8306).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Responsible for the aerobic transport of the dicarboxylates fumarate, L- and D-malate and to a lesser extent succinate, from the periplasm across the inner membrane. {ECO:0000269|PubMed:17088549}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (13)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-121|reaction.ecocyc.TRANS-RXN-121]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-121A|reaction.ecocyc.TRANS-RXN-121A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-121C|reaction.ecocyc.TRANS-RXN-121C]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-122A|reaction.ecocyc.TRANS-RXN-122A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-451|reaction.ecocyc.TRANS-RXN0-451]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-517|reaction.ecocyc.TRANS-RXN0-517]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-553|reaction.ecocyc.TRANS-RXN0-553]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-8306|complex.ecocyc.CPLX0-8306]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `transports` --> [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00149|molecule.C00149]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00295|molecule.C00295]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00497|molecule.C00497]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.C4-dicarboxylates|molecule.ecocyc.C4-dicarboxylates]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3528|gene.b3528]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A830`
- `KEGG:ecj:JW3496;eco:b3528;`
- `GeneID:86862070;93778248;948039;`
- `GO:GO:0005886; GO:0006974; GO:0015138; GO:0015141; GO:0015183; GO:0015366; GO:0015741; GO:0016020; GO:0070778`

## Notes

Aerobic C4-dicarboxylate transport protein
