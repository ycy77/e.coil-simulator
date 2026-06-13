---
entity_id: "protein.P0ABI4"
entity_type: "protein"
name: "corA"
source_database: "UniProt"
source_id: "P0ABI4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:780341}; Multi-pass membrane protein {ECO:0000250|UniProtKB:Q9WZ31}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "corA b3816 JW3789"
---

# corA

`protein.P0ABI4`

## Static

- Type: `protein`
- Source: `UniProt:P0ABI4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:780341}; Multi-pass membrane protein {ECO:0000250|UniProtKB:Q9WZ31}.

## Enriched Summary

FUNCTION: Mediates influx of magnesium ions. Can also mediate cobalt and manganese uptake (PubMed:780341). Alternates between open and closed states. Activated by low cytoplasmic Mg(2+) levels. Inactive when cytoplasmic Mg(2+) levels are high (By similarity). {ECO:0000250|UniProtKB:Q9WZ31, ECO:0000269|PubMed:780341}. CorA is an inner membrane magnesium ion transporter . Kinetic analyses indicate that CorA is a constitutive magnesium, cobalt and manganese ion transport protein . A plasmid expressing corA from E.coli can complement a Salmonella enterica corA mutation and restore uptake of Co2+ and Mg2+ . CorA is comprised of a large periplasmic domain and three membrane spanning helices . The purified periplasmic domain of CorA functions as a homotetramer and is able to bind magnesium, cobalt and nickel ions . The well characterised CorA homolog from Salmonella enterica (which has 98% amino acid identity with E. coli CorA) mediates Mg2+ - Mg2+ exchange in addition to the import of magnesium, cobalt and nickel ions . CorA is dependent on the Sec pathway for membrane integration

## Biological Role

Catalyzes TRANS-RXN-141 (reaction.ecocyc.TRANS-RXN-141), TRANS-RXN-141A (reaction.ecocyc.TRANS-RXN-141A), TRANS-RXN-141B (reaction.ecocyc.TRANS-RXN-141B). Transports Magnesium cation (molecule.C00305), Nickel(2+) (molecule.C19609).

## Annotation

FUNCTION: Mediates influx of magnesium ions. Can also mediate cobalt and manganese uptake (PubMed:780341). Alternates between open and closed states. Activated by low cytoplasmic Mg(2+) levels. Inactive when cytoplasmic Mg(2+) levels are high (By similarity). {ECO:0000250|UniProtKB:Q9WZ31, ECO:0000269|PubMed:780341}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-141|reaction.ecocyc.TRANS-RXN-141]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-141A|reaction.ecocyc.TRANS-RXN-141A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-141B|reaction.ecocyc.TRANS-RXN-141B]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3816|gene.b3816]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABI4`
- `KEGG:ecj:JW3789;eco:b3816;ecoc:C3026_20655;`
- `GeneID:93778125;948351;`
- `GO:GO:0005886; GO:0006824; GO:0015087; GO:0015095; GO:0015099; GO:0015693; GO:0035444`

## Notes

Magnesium transport protein CorA
