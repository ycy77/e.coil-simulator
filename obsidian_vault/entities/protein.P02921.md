---
entity_id: "protein.P02921"
entity_type: "protein"
name: "melB"
source_database: "UniProt"
source_id: "P02921"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:1730719, ECO:0000269|PubMed:7703254, ECO:0000269|PubMed:8672452}; Multi-pass membrane protein {ECO:0000269|PubMed:1730719, ECO:0000269|PubMed:8672452}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "melB mel-4 b4120 JW4081"
---

# melB

`protein.P02921`

## Static

- Type: `protein`
- Source: `UniProt:P02921`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:1730719, ECO:0000269|PubMed:7703254, ECO:0000269|PubMed:8672452}; Multi-pass membrane protein {ECO:0000269|PubMed:1730719, ECO:0000269|PubMed:8672452}.

## Enriched Summary

FUNCTION: Mediates the transport of melibiose and other galactosides by a symport mechanism (PubMed:2185831, PubMed:3311166, PubMed:3316227, PubMed:45782, PubMed:7703254). Can use sodium, lithium and protons as coupling cations, depending on the sugar substrate and the cationic environment (PubMed:3311166, PubMed:3316227, PubMed:45782, PubMed:7703254). Alpha-galactosides (melibiose, raffinose, p-nitrophenyl-alpha-galactoside or methyl-alpha-galactoside) are cotransported with either Na(+) or H(+), whereas beta-galactosides (lactose, L-arabinose-beta-D-galactoside, D-fructose-beta-D-galactoside, methyl-beta-galactoside or p-nitrophenyl-beta-galactoside) are cotransported with Na(+) or Li(+) but not H(+) (PubMed:3311166, PubMed:45782). The monosaccharide D-galactose can use either Na(+) or H(+) for cotransport whereas D-fucose, L-arabinose and D-galactosamine can use only Na(+) (PubMed:3311166). {ECO:0000269|PubMed:2185831, ECO:0000269|PubMed:3311166, ECO:0000269|PubMed:3316227, ECO:0000269|PubMed:45782, ECO:0000269|PubMed:7703254}. MelB is a melibiose-cation cotransport protein belonging to the Glycoside-Pentoside-Hexuronide:Cation Symporter Family (GPH) . Proteins in the GPH family facilitate sugar-cation symport...

## Biological Role

Catalyzes melibionate:proton symport (reaction.ecocyc.RXN-17755), melibiose:proton symport (reaction.ecocyc.TRANS-RXN-94), melibiose:Na+ symport (reaction.ecocyc.TRANS-RXN-94A), melibiose:Li+ symport (reaction.ecocyc.TRANS-RXN-94B), α-methylgalactoside:proton symport (reaction.ecocyc.TRANS-RXN0-519), β-methylgalactoside:Na+ symport (reaction.ecocyc.TRANS-RXN0-520). Transports Sodium cation (molecule.C01330), Methyl beta-D-galactoside (molecule.C03619), Melibiose (molecule.C05402), melibionate (molecule.ecocyc.CPD-3801), Li+ (molecule.ecocyc.LI_), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Mediates the transport of melibiose and other galactosides by a symport mechanism (PubMed:2185831, PubMed:3311166, PubMed:3316227, PubMed:45782, PubMed:7703254). Can use sodium, lithium and protons as coupling cations, depending on the sugar substrate and the cationic environment (PubMed:3311166, PubMed:3316227, PubMed:45782, PubMed:7703254). Alpha-galactosides (melibiose, raffinose, p-nitrophenyl-alpha-galactoside or methyl-alpha-galactoside) are cotransported with either Na(+) or H(+), whereas beta-galactosides (lactose, L-arabinose-beta-D-galactoside, D-fructose-beta-D-galactoside, methyl-beta-galactoside or p-nitrophenyl-beta-galactoside) are cotransported with Na(+) or Li(+) but not H(+) (PubMed:3311166, PubMed:45782). The monosaccharide D-galactose can use either Na(+) or H(+) for cotransport whereas D-fucose, L-arabinose and D-galactosamine can use only Na(+) (PubMed:3311166). {ECO:0000269|PubMed:2185831, ECO:0000269|PubMed:3311166, ECO:0000269|PubMed:3316227, ECO:0000269|PubMed:45782, ECO:0000269|PubMed:7703254}.

## Outgoing Edges (12)

- `catalyzes` --> [[reaction.ecocyc.RXN-17755|reaction.ecocyc.RXN-17755]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-94|reaction.ecocyc.TRANS-RXN-94]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-94A|reaction.ecocyc.TRANS-RXN-94A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-94B|reaction.ecocyc.TRANS-RXN-94B]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-519|reaction.ecocyc.TRANS-RXN0-519]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-520|reaction.ecocyc.TRANS-RXN0-520]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C03619|molecule.C03619]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C05402|molecule.C05402]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-3801|molecule.ecocyc.CPD-3801]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.LI|molecule.ecocyc.LI_]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b4120|gene.b4120]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P02921`
- `KEGG:ecj:JW4081;eco:b4120;ecoc:C3026_22265;`
- `GeneID:948635;`
- `GO:GO:0005886; GO:0015487; GO:0015592; GO:0015765; GO:0015769; GO:0043887; GO:0055085`

## Notes

Melibiose permease (Melibiose carrier) (Melibiose transporter) (Melibiose/cation symporter) (Na+ (Li+)/melibiose symporter) (Thiomethylgalactoside permease II)
