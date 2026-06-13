---
entity_id: "protein.P37340"
entity_type: "protein"
name: "mdtK"
source_database: "UniProt"
source_id: "P37340"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000305|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdtK norE norM ydhE b1663 JW1655"
---

# mdtK

`protein.P37340`

## Static

- Type: `protein`
- Source: `UniProt:P37340`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000305|PubMed:15919996}.

## Enriched Summary

FUNCTION: Multidrug efflux pump that probably functions as a Na(+)/drug antiporter. Confers resistance to many drugs such as fluoroquinolones (norfloxacin, ciprofloxacin, enoxacin) and tetraphenylphosphonium ion (TPP) (PubMed:11566977, PubMed:9661020). Also to deoxycholate, doxorubicin, trimethoprim, chloramphenicol, fosfomycin, ethidium bromide and benzalkonium (PubMed:11566977). Also able to export peptides; when overexpressed, allows cells deleted for multiple peptidases (pepA, pepB, pepD and pepN) to grow in the presence of dipeptides Ala-Gln or Gly-Tyr which otherwise inhibit growth (PubMed:20067529). Cells overexpressing this protein have decreased intracellular levels of Ala-Gln dipeptide, and in a system that produces the Ala-Gln dipeptide overproduction of this protein increases export of the dipeptide (PubMed:20067529). {ECO:0000269|PubMed:11566977, ECO:0000269|PubMed:12615854, ECO:0000269|PubMed:20067529, ECO:0000269|PubMed:9661020}. MdtK (also called NorM) is a member of the Multi Antimicrobial Extrusion (MATE) family of transporters (formerly the multidrug and toxic compound extrusion family) within the Multidrug/Oligosaccharidyl-lipid/Polysaccharide (MOP) flippase superfamily . Increased expression of mdtK in an E. coli strain lacking the major drug efflux pump AcrAB (E...

## Biological Role

Catalyzes xenobiotic:Na+ antiport (reaction.ecocyc.RXN0-2561), norfloxacin:Na+ antiport (reaction.ecocyc.TRANS-RXN-347), tetraphenylphosphonium:Na+ antiport (reaction.ecocyc.TRANS-RXN-348), deoxycholate:Na+ antiport (reaction.ecocyc.TRANS-RXN-349). Transports Sodium cation (molecule.C01330), Deoxycholic acid (molecule.C04483), Norfloxacin (molecule.C06687), tetraphenylphosphonium (molecule.ecocyc.CPD-20890).

## Annotation

FUNCTION: Multidrug efflux pump that probably functions as a Na(+)/drug antiporter. Confers resistance to many drugs such as fluoroquinolones (norfloxacin, ciprofloxacin, enoxacin) and tetraphenylphosphonium ion (TPP) (PubMed:11566977, PubMed:9661020). Also to deoxycholate, doxorubicin, trimethoprim, chloramphenicol, fosfomycin, ethidium bromide and benzalkonium (PubMed:11566977). Also able to export peptides; when overexpressed, allows cells deleted for multiple peptidases (pepA, pepB, pepD and pepN) to grow in the presence of dipeptides Ala-Gln or Gly-Tyr which otherwise inhibit growth (PubMed:20067529). Cells overexpressing this protein have decreased intracellular levels of Ala-Gln dipeptide, and in a system that produces the Ala-Gln dipeptide overproduction of this protein increases export of the dipeptide (PubMed:20067529). {ECO:0000269|PubMed:11566977, ECO:0000269|PubMed:12615854, ECO:0000269|PubMed:20067529, ECO:0000269|PubMed:9661020}.

## Outgoing Edges (8)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2561|reaction.ecocyc.RXN0-2561]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-347|reaction.ecocyc.TRANS-RXN-347]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-348|reaction.ecocyc.TRANS-RXN-348]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-349|reaction.ecocyc.TRANS-RXN-349]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C04483|molecule.C04483]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C06687|molecule.C06687]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-20890|molecule.ecocyc.CPD-20890]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1663|gene.b1663]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37340`
- `KEGG:ecj:JW1655;eco:b1663;ecoc:C3026_09540;`
- `GeneID:945883;`
- `GO:GO:0005886; GO:0006814; GO:0006855; GO:0015031; GO:0015297; GO:0016020; GO:0034614; GO:0035442; GO:0042910; GO:0046677; GO:0071916; GO:1990961`

## Notes

Multidrug resistance protein MdtK (Multidrug-efflux transporter)
