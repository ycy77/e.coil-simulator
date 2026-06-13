---
entity_id: "protein.P75892"
entity_type: "protein"
name: "rutG"
source_database: "UniProt"
source_id: "P75892"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rutG ycdG b1006 JW5137"
---

# rutG

`protein.P75892`

## Static

- Type: `protein`
- Source: `UniProt:P75892`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: May function as a proton-driven pyrimidine uptake system. {ECO:0000269|PubMed:16540542}. RutG is a high-affinity pyrimidine transporter; RutG mediates the uptake of both uracil and thymidine; the uptake of labeled uracil is abolished by the protonophore carbonyl cyanide m-chlorophenyl hydrazone (CCCP) . RutG transports xanthine with low affinity and efficiency; it does not transport cytosine, adenine, guanine, hypoxanthine or uric acid . rutG is the last gene in a 7 gene operon (rutABCDEFG) that encodes proteins involved in the utilization of pyrimidines as a nitrogen source in E. coli K-12 . Expression of the rut operon is activated by the nitrogen regulatory protein C (NtrC) when nitrogen is limiting and repressed by the global regulator RutR . A rutG deletion mutant does not grow on uracil as the sole source of nitrogen at room temperature . Deletion of upp, encoding URACIL-PRIBOSYLTRANS-CPLX, prevents the uptake of uracil by RutG and by CPLX0-8247 UraA . E. coli cannot use pyrimidines as the sole nitrogen source at 37oC however the rut operon is highly expressed at this temperature under nitrogen limiting conditions. The Rut pathway may function during nitrogen limitation to scavenge the pyrimidines released from RNA degradation RutG is a member of the nucleobase:cation symporter-2 (NCS2) family of transporters...

## Biological Role

Catalyzes xanthine:proton symport (reaction.ecocyc.RXN-5076), uracil:proton symport (reaction.ecocyc.TRANS-RXN-132), thymine:proton symport (reaction.ecocyc.TRANS-RXN-362). Transports Uracil (molecule.C00106), Thymine (molecule.C00178), Xanthine (molecule.C00385), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: May function as a proton-driven pyrimidine uptake system. {ECO:0000269|PubMed:16540542}.

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.ecocyc.RXN-5076|reaction.ecocyc.RXN-5076]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-132|reaction.ecocyc.TRANS-RXN-132]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-362|reaction.ecocyc.TRANS-RXN-362]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00106|molecule.C00106]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00178|molecule.C00178]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00385|molecule.C00385]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1006|gene.b1006]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75892`
- `KEGG:ecj:JW5137;eco:b1006;ecoc:C3026_06125;`
- `GeneID:946589;`
- `GO:GO:0005350; GO:0005886; GO:0006212; GO:0015210; GO:0015218; GO:0015505; GO:0098721; GO:1904082`

## Notes

Putative pyrimidine permease RutG
