---
entity_id: "protein.P39396"
entity_type: "protein"
name: "btsT"
source_database: "UniProt"
source_id: "P39396"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22685278, ECO:0000269|PubMed:29061664}; Multi-pass membrane protein {ECO:0000305|PubMed:29061664}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "btsT yjiY b4354 JW5791"
---

# btsT

`protein.P39396`

## Static

- Type: `protein`
- Source: `UniProt:P39396`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22685278, ECO:0000269|PubMed:29061664}; Multi-pass membrane protein {ECO:0000305|PubMed:29061664}.

## Enriched Summary

FUNCTION: Transports pyruvate with a high affinity and specificity. The process is driven by the proton motive force (PubMed:29061664). Under nutrient limiting conditions, mediates the uptake of pyruvate, thus enabling it to be used as a carbon source for the growth and survival (PubMed:29061664). Part of a nutrient-sensing regulatory network composed of the two-component regulatory systems BtsS/BtsR and YpdA/YpdB, and their respective target proteins, BtsT and YhjX (PubMed:24659770). {ECO:0000269|PubMed:24659770, ECO:0000269|PubMed:29061664}. BtsT is a high-affinity, pyruvate:H+ symporter which mediates the uptake of pyruvate under nutrient limiting conditions. Extrachromosomal expression of btsT in a ΔbtsT mutant and in a strain with decreased pyruvate metabolism increases the uptake rate of labeled pyruvate compared to the control; transport is highest at pH 7.5, decreases at pH 6 and is not detected at pH 4.5 and 3; transport is abolished upon addition of the protonophores 2,4-dinitro-phenol (DNP) or carbonyl cyanide m-chlorophenyl hydrazone (CCCP) . Purified BtsT, reconstituted into proteoliposomes mediates the active accumulation of labeled pyruvate; transport is dependent on both membrane potential and a proton gradient (interior negative and alkaline)...

## Biological Role

Catalyzes pyruvate:proton symport (reaction.ecocyc.TRANS-RXN-335). Transports Pyruvate (molecule.C00022), hν (molecule.ecocyc.Light).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Transports pyruvate with a high affinity and specificity. The process is driven by the proton motive force (PubMed:29061664). Under nutrient limiting conditions, mediates the uptake of pyruvate, thus enabling it to be used as a carbon source for the growth and survival (PubMed:29061664). Part of a nutrient-sensing regulatory network composed of the two-component regulatory systems BtsS/BtsR and YpdA/YpdB, and their respective target proteins, BtsT and YhjX (PubMed:24659770). {ECO:0000269|PubMed:24659770, ECO:0000269|PubMed:29061664}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-335|reaction.ecocyc.TRANS-RXN-335]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b4354|gene.b4354]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39396`
- `KEGG:ecj:JW5791;eco:b4354;ecoc:C3026_23520;`
- `GeneID:948914;`
- `GO:GO:0005477; GO:0005886; GO:0006849; GO:0006974; GO:0009267; GO:0015293; GO:0031669`

## Notes

Pyruvate/proton symporter BtsT (Brenztraubensaure transporter) (Pyruvate/H(+) symporter)
