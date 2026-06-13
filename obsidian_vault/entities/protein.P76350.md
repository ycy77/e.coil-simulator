---
entity_id: "protein.P76350"
entity_type: "protein"
name: "shiA"
source_database: "UniProt"
source_id: "P76350"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "shiA yeeM b1981 JW1962"
---

# shiA

`protein.P76350`

## Static

- Type: `protein`
- Source: `UniProt:P76350`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Involved in the uptake of shikimate, an intermediate in the aromatic amino acid biosynthetic pathway. {ECO:0000269|PubMed:9524262}. ShiA has been implicated in the high affinity transport of shikimate, an intermediate in the aromatic amino acid biosynthetic pathway . Chromosomal mutants in shiA are unable to transport shikimate, and introduction of the cloned shiA gene restores shikimate transport . The ShiA protein has twelve predicted TMS and is a member of the major facilitator superfamily of transporters (MFS) and hence is likely to function as a proton/shikimate symporter. Analysis of a shiA-lacZ fusion has suggested that shiA expression is constitutive and is not regulated by the TyrR repressor . The shiA gene probably constitutes a monocistronic operon. Imported shikimate presumably serves as a substrate for biosynthesis of aromatic compounds.

## Biological Role

Catalyzes shikimate:proton symport (reaction.ecocyc.TRANS-RXN-27). Transports Shikimate (molecule.C00493), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Involved in the uptake of shikimate, an intermediate in the aromatic amino acid biosynthetic pathway. {ECO:0000269|PubMed:9524262}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-27|reaction.ecocyc.TRANS-RXN-27]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00493|molecule.C00493]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1981|gene.b1981]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76350`
- `KEGG:ecj:JW1962;eco:b1981;ecoc:C3026_11185;`
- `GeneID:75202786;946495;`
- `GO:GO:0005886; GO:0015293; GO:0015530; GO:0015733; GO:0022857`

## Notes

Shikimate transporter (Shikimate permease)
