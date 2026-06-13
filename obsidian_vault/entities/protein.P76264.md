---
entity_id: "protein.P76264"
entity_type: "protein"
name: "mntP"
source_database: "UniProt"
source_id: "P76264"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:29440394}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mntP yebN b1821 JW5830"
---

# mntP

`protein.P76264`

## Static

- Type: `protein`
- Source: `UniProt:P76264`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:29440394}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Functions as a manganese exporter (PubMed:29440394, PubMed:38869303). Involved in manganese homeostasis (PubMed:21908668, PubMed:25774656, PubMed:29440394). Important for reducing the concentration of manganese in the cell when manganese levels are high, thus reducing its toxicity (PubMed:25774656). Transport of Mn(2+) by MntP is unlikely to be accompanied by an H(+) antiport (PubMed:38869303). Alters cellular resistance to reactive oxygen species (ROS) (PubMed:29440394). {ECO:0000269|PubMed:21908668, ECO:0000269|PubMed:25774656, ECO:0000269|PubMed:29440394, ECO:0000269|PubMed:38869303}. mntP encodes the primary manganese exporter. An mntP deletion strain exhibits increased sensitivity to manganese and accumulates approximately 2-fold more intracellular manganese than the wild type . MntP confers robust manganese resistance; MntP expression affects resistance to reactive oxygen species; ectopic production of MntP halts the growth of a strain (ΔahpCF ΔkatG) that accumulates high levels of hydrogen peroxide . Inactivation of MntP increases the recovery of DNA replication after H2O2 exposure . Exposure to 10 µM manganese chloride results in increased expression of mntP and increased levels of a chromosomal MntP fusion protein; this induction is attenuated in an mntR deletion strain...

## Biological Role

Catalyzes Mn2+ export (reaction.ecocyc.TRANS-RXN0-487). Transports Mn2+ (molecule.ecocyc.MN_2).

## Annotation

FUNCTION: Functions as a manganese exporter (PubMed:29440394, PubMed:38869303). Involved in manganese homeostasis (PubMed:21908668, PubMed:25774656, PubMed:29440394). Important for reducing the concentration of manganese in the cell when manganese levels are high, thus reducing its toxicity (PubMed:25774656). Transport of Mn(2+) by MntP is unlikely to be accompanied by an H(+) antiport (PubMed:38869303). Alters cellular resistance to reactive oxygen species (ROS) (PubMed:29440394). {ECO:0000269|PubMed:21908668, ECO:0000269|PubMed:25774656, ECO:0000269|PubMed:29440394, ECO:0000269|PubMed:38869303}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-487|reaction.ecocyc.TRANS-RXN0-487]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1821|gene.b1821]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76264`
- `KEGG:ecj:JW5830;eco:b1821;ecoc:C3026_10375;`
- `GeneID:93776070;946341;`
- `GO:GO:0005384; GO:0005886; GO:0030026; GO:0140048`

## Notes

Manganese exporter MntP (Manganese efflux protein MntP)
