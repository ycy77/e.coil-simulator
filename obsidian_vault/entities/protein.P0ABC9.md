---
entity_id: "protein.P0ABC9"
entity_type: "protein"
name: "betT"
source_database: "UniProt"
source_id: "P0ABC9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "betT b0314 JW0306"
---

# betT

`protein.P0ABC9`

## Static

- Type: `protein`
- Source: `UniProt:P0ABC9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: High-affinity uptake of choline driven by a proton-motive force. {ECO:0000269|PubMed:1956285}. BetT is a proton-motive-force-driven choline transporter that belongs to the Betaine Carnitine Choline Transport (BCCT) family of proteins. Deletion mutants of betT displayed essentially no choline uptake activity, but could be complemented with a betT-encoding plasmid, restoring rapid choline uptake . Choline uptake is completely inhibited by the protonophore carbonylcyanide p-trifluoromethoxyphenyl hydrazone, suggesting that choline transport by BetT is driven by the proton-motive force . Choline is used to synthesize glycine betaine, which is used by E. coli to overcome growth inhibition caused by osmotic stress . The betTIAB genes are expressed only under aerobic conditions, and are induced by osmotic stress . Analysis of betT-lacZ fusions showed that betT transcription increased 7-10 fold in response to increases in medium osmolarity. The presence of choline further increases this response . betT mRNA decay is controlled by RNase III in response to osmotic stress. betT mRNA contains two tandem RNase III cleavage sites - both of which are required for efficient betT mRNA degradation . BetT is predicted to have 10-12 membrane spanning regions; it also contains a long hydrophilic C-terminal domain of approximately 200 amino acid residues . betT:

## Biological Role

Catalyzes choline:proton symport (reaction.ecocyc.TRANS-RXN-99). Transports Choline (molecule.C00114), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: High-affinity uptake of choline driven by a proton-motive force. {ECO:0000269|PubMed:1956285}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-99|reaction.ecocyc.TRANS-RXN-99]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00114|molecule.C00114]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0314|gene.b0314]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABC9`
- `KEGG:ecj:JW0306;eco:b0314;ecoc:C3026_01535;ecoc:C3026_24710;`
- `GeneID:75170285;75206484;945079;`
- `GO:GO:0005886; GO:0006974; GO:0015220; GO:0015871; GO:0019285; GO:0022857`

## Notes

High-affinity choline transport protein
