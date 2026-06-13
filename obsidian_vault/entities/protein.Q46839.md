---
entity_id: "protein.Q46839"
entity_type: "protein"
name: "glcA"
source_database: "UniProt"
source_id: "Q46839"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glcA yghK b2975 JW2942"
---

# glcA

`protein.Q46839`

## Static

- Type: `protein`
- Source: `UniProt:Q46839`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Uptake of glycolate across the membrane (PubMed:11283302, PubMed:11785976). Can also transport L-lactate and D-lactate (PubMed:11283302, PubMed:11785976). Seems to be driven by a proton motive force (PubMed:11785976). {ECO:0000269|PubMed:11283302, ECO:0000269|PubMed:11785976}. GlcA (formerly YghK), is a glycolate transporter that belongs to the Lactate Permease Family (LctP) , due to its strong sequence similarity with the L-lactate permease, LCTP-MONOMER "LldP". GlcA transports the 2-hydroxymonocarboxylates, glycolate and L- and D-lactate . The glcA gene is located downstream from the glcDEFGB encoding the glycolate degradating enzymes malate synthase and glycolate oxidase. Expression studies using Northern blot analysis and lacZ fusion experiments have shown that the glcA gene is transcribed from the same promoter as the other glc structural genes . Expression of this operon is induced by growth on glycolate and is under the control of the transcriptional regulator, G7546-MONOMER "GlcC" . Growth of a glcA::cat mutant on glycolate was not totally abolished, but its rate was much lower than that of the parental strain, indicating that GlcA probably functions as a glycolate transporter, although glycolate can also enter the cell through another transport system . The lactate permease LldP was also found to be capable of glycolate transport...

## Biological Role

Catalyzes lactate:proton symport (reaction.ecocyc.TRANS-RXN-104), glycolate:proton symport (reaction.ecocyc.TRANS-RXN-105), lactate:proton symport (reaction.ecocyc.TRANS-RXN0-515), hydroxybutanoate:proton symport (reaction.ecocyc.TRANS-RXN0-622). Transports (S)-Lactate (molecule.C00186), (R)-Lactate (molecule.C00256), 2-Hydroxybutanoic acid (molecule.C05984), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Uptake of glycolate across the membrane (PubMed:11283302, PubMed:11785976). Can also transport L-lactate and D-lactate (PubMed:11283302, PubMed:11785976). Seems to be driven by a proton motive force (PubMed:11785976). {ECO:0000269|PubMed:11283302, ECO:0000269|PubMed:11785976}.

## Outgoing Edges (8)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-104|reaction.ecocyc.TRANS-RXN-104]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-105|reaction.ecocyc.TRANS-RXN-105]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-515|reaction.ecocyc.TRANS-RXN0-515]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-622|reaction.ecocyc.TRANS-RXN0-622]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00186|molecule.C00186]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00256|molecule.C00256]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C05984|molecule.C05984]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2975|gene.b2975]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46839`
- `KEGG:ecj:JW2942;eco:b2975;ecoc:C3026_16275;`
- `GeneID:75173100;947259;`
- `GO:GO:0005886; GO:0015129; GO:0015295; GO:0035873; GO:0043879`

## Notes

Glycolate permease GlcA
