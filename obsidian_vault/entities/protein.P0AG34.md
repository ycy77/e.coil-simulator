---
entity_id: "protein.P0AG34"
entity_type: "protein"
name: "rhtB"
source_database: "UniProt"
source_id: "P0AG34"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rhtB yigK b3824 JW5585"
---

# rhtB

`protein.P0AG34`

## Static

- Type: `protein`
- Source: `UniProt:P0AG34`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Conducts the efflux of homoserine and homoserine lactone. {ECO:0000269|PubMed:10386596}. RhtB can mediate the export of L-homoserine, L-homoserine lactone and L-threonine; the physiological role of the transporter remains uncertain. Multicopy expression of rhtB confers increased resistance to L-homoserine, L-homoserine lactone, L-threonine , S-methyl methionine and possibly L-serine . Disruption or deletion of rhtB decreases resistance to L-homoserine and L-homoserine lactone , L-serine and DL-β-hydroxynorvaline and L-threonine . Multicopy expression of rhtB increases homoserine production in homoserine producer strains of E. coli; disruption of rhtB (rhtB::cat) decreases production . Multicopy expression of rhtB increases threonine production in a threonine producing strain of E. coli . RhtB contains 6 predicted transmembrane regions and is the prototype member of the Resistance to Homoserine/Threonine (RhtB) family of transporters within the LysE superfamily . rht: resistance to homoserine and threonine .

## Biological Role

Catalyzes L-homoserine:proton antiport (reaction.ecocyc.TRANS-RXN-242), L-homoserine lactone:proton antiport (reaction.ecocyc.TRANS-RXN-242A), L-threonine:proton antiport (reaction.ecocyc.TRANS-RXN0-0244). Transports L-Threonine (molecule.C00188), L-homoserine lactone (molecule.ecocyc.CPD-15554), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Conducts the efflux of homoserine and homoserine lactone. {ECO:0000269|PubMed:10386596}.

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-242|reaction.ecocyc.TRANS-RXN-242]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-242A|reaction.ecocyc.TRANS-RXN-242A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-0244|reaction.ecocyc.TRANS-RXN0-0244]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-15554|molecule.ecocyc.CPD-15554]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3824|gene.b3824]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG34`
- `KEGG:ecj:JW5585;eco:b3824;ecoc:C3026_20695;`
- `GeneID:93778113;948316;`
- `GO:GO:0005886; GO:0015565; GO:0015826; GO:0042968; GO:0042970`

## Notes

Homoserine/homoserine lactone efflux protein
