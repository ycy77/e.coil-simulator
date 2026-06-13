---
entity_id: "protein.P0AE24"
entity_type: "protein"
name: "araE"
source_database: "UniProt"
source_id: "P0AE24"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:2836407, ECO:0000269|PubMed:7030324}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "araE b2841 JW2809"
---

# araE

`protein.P0AE24`

## Static

- Type: `protein`
- Source: `UniProt:P0AE24`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:2836407, ECO:0000269|PubMed:7030324}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Uptake of L-arabinose across the cytoplasmic membrane with the concomitant transport of protons into the cell (symport system) (PubMed:2836407, PubMed:6282256, PubMed:7030324). D-fucose, a nonmetabolizable analog of L-arabinose, is also a good substrate (PubMed:6282256). {ECO:0000269|PubMed:2836407, ECO:0000269|PubMed:6282256, ECO:0000269|PubMed:7030324}. AraE is an arabinose/proton symporter responsible for the uptake of arabinose. Studies in membrane vesicles have shown that AraE can transport L-arabinose with low affinity (140-320 μM) and arabinose transport is coupled with proton transport . The AraE protein has been overproduced and reconstituted in liposomes as an arabinose/proton symporter . AraE is a member of the major facilitator superfamily (MFS) of transporters . Arabinose is the sole inducer of araE expression , which is controlled by the AraC regulator. An inhibitory effect on araE induced by arabinose appeared in the presence of xylose . Imported arabinose is catabolized to xylulose-5-phosphatel, which then enters the pentose phosphate pathway.

## Biological Role

Catalyzes arabinose:proton symport (reaction.ecocyc.TRANS-RXN-10). Transports L-Arabinose (molecule.C00259), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Uptake of L-arabinose across the cytoplasmic membrane with the concomitant transport of protons into the cell (symport system) (PubMed:2836407, PubMed:6282256, PubMed:7030324). D-fucose, a nonmetabolizable analog of L-arabinose, is also a good substrate (PubMed:6282256). {ECO:0000269|PubMed:2836407, ECO:0000269|PubMed:6282256, ECO:0000269|PubMed:7030324}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-10|reaction.ecocyc.TRANS-RXN-10]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00259|molecule.C00259]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2841|gene.b2841]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE24`
- `KEGG:ecj:JW2809;eco:b2841;ecoc:C3026_15600;`
- `GeneID:93779155;947341;`
- `GO:GO:0005886; GO:0015147; GO:0015150; GO:0015293; GO:0015756; GO:0016020; GO:0042882; GO:0055085`

## Notes

Arabinose-proton symporter (Arabinose transporter)
