---
entity_id: "protein.P0AA86"
entity_type: "protein"
name: "dsbE"
source_database: "UniProt"
source_id: "P0AA86"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Single-pass membrane protein; Periplasmic side."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dsbE ccmG yejQ b2195 JW2183"
---

# dsbE

`protein.P0AA86`

## Static

- Type: `protein`
- Source: `UniProt:P0AA86`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Single-pass membrane protein; Periplasmic side.

## Enriched Summary

FUNCTION: Involved in disulfide bond formation. Catalyzes a late, reductive step in the assembly of periplasmic c-type cytochromes, probably the reduction of disulfide bonds of the apocytochrome c to allow covalent linkage with the heme. Possible subunit of a heme lyase. DsbE is maintained in a reduced state by DsbD. CcmG is a membrane-anchored thiol-disulfide reductase implicated in apocytochrome c thioreduction prior to heme ligation in the System I pathway of cytochome c maturation. ccmG is part of an 8 gene cluster (ccmABCDEFGH) which bears sequence similarity to Bradyrhizobium japonicum genes that are required for the biogenesis of Cytochromes-c "c-type cytochromes"; an E. coli ΔccmA-H mutant strain (EC06) is not able to produce mature c-type cytochromes under anaerobic, nonfermentative growth conditions (see also ). An in-frame ccmG deletion mutant is able to produce (plasmid-encoded) apocytochrome c-550 but not holocytochrome c-550 . CcmG is a small protein with a thioredoxin-like motif facing the periplasm, but tethered to the cytoplasmic membrane by a hydrophobic N-terminal domain; CcmG has a reducing role in vivo . CcmG catalyses a late reductive step in holocytochrome c biosynthesis . CcmG is reduced by the DSBD-MONOMER...

## Biological Role

Catalyzes RXN-21421 (reaction.ecocyc.RXN-21421), RXN-21424 (reaction.ecocyc.RXN-21424), RXN-21425 (reaction.ecocyc.RXN-21425).

## Annotation

FUNCTION: Involved in disulfide bond formation. Catalyzes a late, reductive step in the assembly of periplasmic c-type cytochromes, probably the reduction of disulfide bonds of the apocytochrome c to allow covalent linkage with the heme. Possible subunit of a heme lyase. DsbE is maintained in a reduced state by DsbD.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-21421|reaction.ecocyc.RXN-21421]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-21424|reaction.ecocyc.RXN-21424]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-21425|reaction.ecocyc.RXN-21425]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2195|gene.b2195]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA86`
- `KEGG:ecj:JW2183;eco:b2195;ecoc:C3026_12270;`
- `GeneID:93774983;949073;`
- `GO:GO:0005886; GO:0015036; GO:0016491; GO:0017004; GO:0030288`

## Notes

Thiol:disulfide interchange protein DsbE (Cytochrome c biogenesis protein CcmG)
