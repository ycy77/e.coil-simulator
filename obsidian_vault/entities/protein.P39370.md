---
entity_id: "protein.P39370"
entity_type: "protein"
name: "nanS"
source_database: "UniProt"
source_id: "P39370"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:19749043}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nanS yjhS b4309 JW4272"
---

# nanS

`protein.P39370`

## Static

- Type: `protein`
- Source: `UniProt:P39370`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:19749043}.

## Enriched Summary

FUNCTION: Probably catalyzes the hydrolysis of the 9-O-acetyl group of 9-O-acetyl-N-acetylneuraminate (Neu5,9Ac2). Is required for growth of E.coli on Neu5,9Ac2, an alternative sialic acid commonly found in mammalian host mucosal sites, in particular in the human intestine. {ECO:0000269|PubMed:19749043}. N-ACETYL-9-O-ACETYLNEURAMINATE (Neu5,9Ac2) is a commonly occurring sialic acid in the human intestine and can be utilized as the sole source of carbon by E. coli. NanS is predicted to be periplasmic and catalyzes the hydrolysis of the 9-O-acetyl group of Neu5,9Ac2, thereby liberating N-ACETYLNEURAMINATE (Neu5Ac) . Earlier, the enzyme from E. coli O157:H7, whose amino acid sequence is 98% identical to that of K-12 MG1655, has been structurally and biochemically characterized. The Ser19 and His301 residues that were found to be essential for catalysis are conserved. Growth of E. coli on Neu5,9Ac2 requires nanS . nanS is not required for growth on glycerol minimal medium ; an earlier finding that nanS was required for growth on glycerol () may have been due to the particular strain used in that study. nanS, among other genes involved in carbon source transport and metabolism, was downregulated in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 . Reviews:

## Biological Role

Catalyzes RXN-13182 (reaction.ecocyc.RXN-13182).

## Annotation

FUNCTION: Probably catalyzes the hydrolysis of the 9-O-acetyl group of 9-O-acetyl-N-acetylneuraminate (Neu5,9Ac2). Is required for growth of E.coli on Neu5,9Ac2, an alternative sialic acid commonly found in mammalian host mucosal sites, in particular in the human intestine. {ECO:0000269|PubMed:19749043}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-13182|reaction.ecocyc.RXN-13182]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4309|gene.b4309]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39370`
- `KEGG:ecj:JW4272;eco:b4309;ecoc:C3026_23265;`
- `GeneID:948835;`
- `GO:GO:0001681; GO:0006054; GO:0019752; GO:0042597; GO:0052689`
- `EC:3.1.1.-`

## Notes

Probable 9-O-acetyl-N-acetylneuraminic acid deacetylase (Neu5,9Ac2 deacetylase) (EC 3.1.1.-) (Probable 9-O-acetyl-N-acetylneuraminate esterase) (Probable sialyl esterase NanS)
