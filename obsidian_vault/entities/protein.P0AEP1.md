---
entity_id: "protein.P0AEP1"
entity_type: "protein"
name: "galP"
source_database: "UniProt"
source_id: "P0AEP1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "galP b2943 JW2910"
---

# galP

`protein.P0AEP1`

## Static

- Type: `protein`
- Source: `UniProt:P0AEP1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Uptake of galactose across the boundary membrane with the concomitant transport of protons into the cell (symport system). GalP is a member of the Major Facilitator Superfamily (MFS) of transporters and is one of two, along with MglABC, major routes for galactose transport into E. coli K-12. 2-deoxy-D-galactose is a specific substrate for GalP but not for MglABC and GalP operates by a sugar-proton symport mechanism while MglABC does not . Mutation studies demonstrated that insertions in the galP gene resulted in a mutant strain resistant to 2-deoxygalactose and defective in uptake of radiolabelled 2-deoxyglucose. The GalP protein has been overproduced and purified and reconstituted as a galactose transporter and has been shown to share a high level of sequence similarity with other proton-linked systems for L-arabinose (AraE, 64% identity) and for D-xylose (XylE, 34% identity) in E.coli . Equilibrium binding studies indicate that cytochalasin B, which is a potent inhibitor of passive glucose transporters in mammals, is bound with high-affinity by membranes of an E. coli strain constitutive for GalP. The same studies indicate that this binding is inhibited by the presence of substrates for GalP in order of their effectiveness as substrates and/ or inhibitors of the GalP transporter...

## Biological Role

Catalyzes D-glucose:proton symport (reaction.ecocyc.RXN0-7077), galactose:proton symport (reaction.ecocyc.TRANS-RXN-21). Transports D-Glucose (molecule.C00031), D-Galactose (molecule.C00124), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Uptake of galactose across the boundary membrane with the concomitant transport of protons into the cell (symport system).

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7077|reaction.ecocyc.RXN0-7077]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-21|reaction.ecocyc.TRANS-RXN-21]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00124|molecule.C00124]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2943|gene.b2943]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEP1`
- `KEGG:ecj:JW2910;eco:b2943;ecoc:C3026_16110;`
- `GeneID:86861033;93779054;947434;`
- `GO:GO:0005886; GO:0015293; GO:0015517; GO:0015757; GO:0016020; GO:0055085`

## Notes

Galactose-proton symporter (Galactose transporter)
