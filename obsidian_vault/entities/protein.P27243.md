---
entity_id: "protein.P27243"
entity_type: "protein"
name: "waaL"
source_database: "UniProt"
source_id: "P27243"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:19019161, ECO:0000269|PubMed:30047569}; Multi-pass membrane protein {ECO:0000269|PubMed:19019161, ECO:0000269|PubMed:30047569, ECO:0000305|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "waaL rfaL b3622 JW3597"
---

# waaL

`protein.P27243`

## Static

- Type: `protein`
- Source: `UniProt:P27243`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:19019161, ECO:0000269|PubMed:30047569}; Multi-pass membrane protein {ECO:0000269|PubMed:19019161, ECO:0000269|PubMed:30047569, ECO:0000305|PubMed:15919996}.

## Enriched Summary

FUNCTION: Transferase involved in the biosynthesis of the lipopolysaccharide (LPS) (PubMed:21983211). In vitro, catalyzes the transfer of a polymerized O-antigen molecule from its polyprenyl diphosphate membrane anchor to a terminal sugar of the lipid A-core oligosaccharide, finalizing the biosynthesis of the lipopolysaccharide (PubMed:21983211, PubMed:30047569). The enzyme is functional and can be used to give diverse hybrid O-antigens in vitro, but K12 strains do not produce the O-antigen in vivo due to mutations in the rfb gene cluster (Probable). K12 strains are phenotypically rough, their lipopolysaccharide having a complete core structure, but no O-antigen (Probable). In highly mucoid K12 strains, WaaL can ligate colanic acid (CA or M-antigen) repeats to a significant proportion of lipopolysaccharide (LPS) core acceptor molecules, forming the LPS glycoform M(LPS) (PubMed:17227761). The attachment point was identified as O-7 of the L-glycero-D-manno-heptose of the outer LPS core, the same position used for O-antigen ligation (PubMed:17227761). Cannot catalyze ATP hydrolysis in vitro (PubMed:21983211). {ECO:0000269|PubMed:17227761, ECO:0000269|PubMed:21983211, ECO:0000269|PubMed:30047569, ECO:0000305|PubMed:9157235}. In E. coli K-12 MG1655, waaL encodes O-antigen ligase or perhaps more correctly 'surface polymer:lipid A-core ligase' (see )...

## Biological Role

Catalyzes RXN-22510 (reaction.ecocyc.RXN-22510), RXN-25219 (reaction.ecocyc.RXN-25219), RXN0-5294 (reaction.ecocyc.RXN0-5294).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Transferase involved in the biosynthesis of the lipopolysaccharide (LPS) (PubMed:21983211). In vitro, catalyzes the transfer of a polymerized O-antigen molecule from its polyprenyl diphosphate membrane anchor to a terminal sugar of the lipid A-core oligosaccharide, finalizing the biosynthesis of the lipopolysaccharide (PubMed:21983211, PubMed:30047569). The enzyme is functional and can be used to give diverse hybrid O-antigens in vitro, but K12 strains do not produce the O-antigen in vivo due to mutations in the rfb gene cluster (Probable). K12 strains are phenotypically rough, their lipopolysaccharide having a complete core structure, but no O-antigen (Probable). In highly mucoid K12 strains, WaaL can ligate colanic acid (CA or M-antigen) repeats to a significant proportion of lipopolysaccharide (LPS) core acceptor molecules, forming the LPS glycoform M(LPS) (PubMed:17227761). The attachment point was identified as O-7 of the L-glycero-D-manno-heptose of the outer LPS core, the same position used for O-antigen ligation (PubMed:17227761). Cannot catalyze ATP hydrolysis in vitro (PubMed:21983211). {ECO:0000269|PubMed:17227761, ECO:0000269|PubMed:21983211, ECO:0000269|PubMed:30047569, ECO:0000305|PubMed:9157235}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-22510|reaction.ecocyc.RXN-22510]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-25219|reaction.ecocyc.RXN-25219]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5294|reaction.ecocyc.RXN0-5294]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3622|gene.b3622]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27243`
- `KEGG:ecj:JW3597;eco:b3622;ecoc:C3026_19635;`
- `GeneID:948148;`
- `GO:GO:0000271; GO:0005886; GO:0008754; GO:0009244; GO:0016757`
- `EC:2.4.99.26`

## Notes

O-antigen ligase (EC 2.4.99.26) (Surface polymer:lipid A-core ligase)
