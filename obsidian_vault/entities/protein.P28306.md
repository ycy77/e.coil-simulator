---
entity_id: "protein.P28306"
entity_type: "protein"
name: "mltG"
source_database: "UniProt"
source_id: "P28306"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02065, ECO:0000269|PubMed:26507882, ECO:0000269|PubMed:33278861}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02065, ECO:0000269|PubMed:26507882}. Note=Access to the inner membrane is important for in vivo activity. {ECO:0000269|PubMed:33278861}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mltG yceG b1097 JW1083"
---

# mltG

`protein.P28306`

## Static

- Type: `protein`
- Source: `UniProt:P28306`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02065, ECO:0000269|PubMed:26507882, ECO:0000269|PubMed:33278861}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02065, ECO:0000269|PubMed:26507882}. Note=Access to the inner membrane is important for in vivo activity. {ECO:0000269|PubMed:33278861}.

## Enriched Summary

FUNCTION: Functions as a peptidoglycan terminase that cleaves nascent peptidoglycan strands endolytically to terminate their elongation (PubMed:26507882). Required for normal glycan strand length distribution (PubMed:26507882). May function as a terminase for both classes of peptidoglycan (PG) synthases (aPBP and SEDS-bPBP synthases) by cleaving PG chains as they are being actively synthesized (PubMed:33278861). {ECO:0000269|PubMed:26507882, ECO:0000269|PubMed:33278861}. MltG is an inner membrane enzyme with endolytic murein transglycosylase activity; it may function to terminate nascent peptidoglycan (PG) synthesis . Evidence for an antagonistic relationship between MltG function and PG synthases supports this contention . Purified, soluble MltG degrades purified murein sacculi and releases monomeric GlcNAc-anhydroMurNAc tetrapeptide plus linear tetra- and hexasaccharide oligomers terminating with an anhydroMurNAc end . MltG is predicted to contain a single transmembrane region with a small N-terminal domain located in the cytoplasm and a large C-terminal domain in the periplasm . MltG interacts with CPLX0-3951 "MrcB" (PBP1B) and with itself . Over-expression of mltG is lethal in cells lacking mrcB . An mltG deletion mutant shows impaired membrane invagination and cytokinesis and reduced sensitivity to ampicillin...

## Biological Role

Catalyzes RXN-17393 (reaction.ecocyc.RXN-17393).

## Annotation

FUNCTION: Functions as a peptidoglycan terminase that cleaves nascent peptidoglycan strands endolytically to terminate their elongation (PubMed:26507882). Required for normal glycan strand length distribution (PubMed:26507882). May function as a terminase for both classes of peptidoglycan (PG) synthases (aPBP and SEDS-bPBP synthases) by cleaving PG chains as they are being actively synthesized (PubMed:33278861). {ECO:0000269|PubMed:26507882, ECO:0000269|PubMed:33278861}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-17393|reaction.ecocyc.RXN-17393]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1097|gene.b1097]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P28306`
- `KEGG:ecj:JW1083;eco:b1097;ecoc:C3026_06630;`
- `GeneID:75203683;945660;`
- `GO:GO:0000270; GO:0005886; GO:0008932; GO:0009252; GO:0030288; GO:0071555`
- `EC:4.2.2.29`

## Notes

Endolytic murein transglycosylase (EC 4.2.2.29) (Peptidoglycan lytic transglycosylase) (Peptidoglycan polymerization terminase)
