---
entity_id: "protein.P0AAD2"
entity_type: "protein"
name: "mtr"
source_database: "UniProt"
source_id: "P0AAD2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:7814318}; Multi-pass membrane protein {ECO:0000269|PubMed:7814318}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mtr b3161 JW3130"
---

# mtr

`protein.P0AAD2`

## Static

- Type: `protein`
- Source: `UniProt:P0AAD2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:7814318}; Multi-pass membrane protein {ECO:0000269|PubMed:7814318}.

## Enriched Summary

FUNCTION: Involved in the transport of tryptophan into the cell. {ECO:0000269|PubMed:4919744, ECO:0000269|PubMed:7814318}. Early studies in E. coli K-12 identified several systems for aromatic amino acid transport including one specific for tryptophan with an apparent Michealis constant of 3 μM . 5-methyl-tryptophan resistant (mtr) mutations described initially by result in loss of this tryptophan-specific transport system (see ). Mtr-mediated tryptophan transport is influenced by the growth medium and Mtr is also able to transport indole although this capability has been disputed . Deletion of mtr negates the indole-induced enhancement of antimicrobial (malachite green) uptake . Membrane topology analysis, together with sequence data, suggests that Mtr contains 11 transmembrane domains with its N-terminus located in the cytoplasm . Expression of mtr is repressed by tryptophan via the CPLX-125 Trp repressor and induced by phenylalanine or tyrosine via PD00413 TyrR . In the Transporter Classification Database () Mtr is a member of the Hydroxy/Aromatic Amino Acid Permease (HAAAP) family within the Amino Acid-Polyamine-Organocation (APC) superfamily. Tryptophan can also be imported into cells by the low-affinity transporter TNAB-MONOMER TnaB and by the general aromatic amino acid transporter AROP-MONOMER AroP.

## Biological Role

Catalyzes indole:proton symport (reaction.ecocyc.TRANS-RXN-142), tryptophan:proton symport (reaction.ecocyc.TRANS-RXN-76). Transports Indole (molecule.C00463), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Involved in the transport of tryptophan into the cell. {ECO:0000269|PubMed:4919744, ECO:0000269|PubMed:7814318}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-142|reaction.ecocyc.TRANS-RXN-142]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-76|reaction.ecocyc.TRANS-RXN-76]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00463|molecule.C00463]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3161|gene.b3161]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAD2`
- `KEGG:ecj:JW3130;eco:b3161;ecoc:C3026_17215;`
- `GeneID:947675;`
- `GO:GO:0003333; GO:0005886; GO:0015196; GO:0015293; GO:0015827; GO:0022857`

## Notes

Tryptophan-specific transport protein (Tryptophan permease)
