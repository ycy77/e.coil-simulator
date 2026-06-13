---
entity_id: "protein.P68187"
entity_type: "protein"
name: "malK"
source_database: "UniProt"
source_id: "P68187"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01709, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:18456666}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01709, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:18456666}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "malK b4035 JW3995"
---

# malK

`protein.P68187`

## Static

- Type: `protein`
- Source: `UniProt:P68187`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01709, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:18456666}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01709, ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:18456666}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex MalEFGK involved in maltose/maltodextrin import. Responsible for energy coupling to the transport system. {ECO:0000269|PubMed:2026607, ECO:0000269|PubMed:2155217}. MalK is the ATP-binding component of the maltose ABC transporter . Opening and closing of the MalK dimer which is associated with ATP binding and hydrolysis is thought to be a key event in the transport cycle. Crystal structures are available for MalK with bound ATP ; MalK without nucleotide (in both an open and semi-open conformation) and MalK with bound ADP . In computer simulations, the introduction of MgATP into the active site of MalK is associated with transition from semi-open to closed conformation and from open to semi-open conformation . Computer simulations also suggest that the closed form of MalK is stable when it contains two bound ATP molecules and that a single ATP hydrolysis will induce opening of the dimer . ATP binds along the dimer interface between the nucleotide binding domains (NBDs), positioned between the Walker A motif of one subunit and the signature LSGGQ motif of the other subunit ; ATP binding tightly tethers the NBDs of the MalK dimer; the γ phosphate of ATP interacts with the Walker A motif, the Q loop, the switch region histidine of one NBD and the LSGGQ motif of the other NBD...

## Biological Role

Component of maltose ABC transporter (complex.ecocyc.ABC-16-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex MalEFGK involved in maltose/maltodextrin import. Responsible for energy coupling to the transport system. {ECO:0000269|PubMed:2026607, ECO:0000269|PubMed:2155217}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-16-CPLX|complex.ecocyc.ABC-16-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4035|gene.b4035]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P68187`
- `KEGG:ecj:JW3995;eco:b4035;ecoc:C3026_21805;`
- `GeneID:93777800;948537;`
- `GO:GO:0005524; GO:0015423; GO:0015768; GO:0016020; GO:0016887; GO:0034763; GO:0042956; GO:0043190; GO:0055052; GO:0140297; GO:1902344; GO:1990060; GO:1990154`
- `EC:7.5.2.1`

## Notes

Maltose/maltodextrin import ATP-binding protein MalK (EC 7.5.2.1)
