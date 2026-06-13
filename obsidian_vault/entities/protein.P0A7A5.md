---
entity_id: "protein.P0A7A5"
entity_type: "protein"
name: "pcm"
source_database: "UniProt"
source_id: "P0A7A5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pcm b2743 JW2713"
---

# pcm

`protein.P0A7A5`

## Static

- Type: `protein`
- Source: `UniProt:P0A7A5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the methyl esterification of L-isoaspartyl residues in peptides and proteins that result from spontaneous decomposition of normal L-aspartyl and L-asparaginyl residues. It plays a role in the repair and/or degradation of damaged proteins. This enzyme does not act on D-aspartyl residues. L-isoaspartate protein carboxylmethyltransferase (PIMT) transfers a methyl group from S-adenosylmethionine (SAM) to the free carboxyl group of D-aspartyl and L-isoaspartyl residues within polypeptides. The enzyme may therefore serve to repair abnormal L-isoaspartyl residues that arise spontaneously from aspartyl and asparaginyl residues in proteins. PIMT enhances survival of E. coli under conditions of environmental stress in late stationary phase and oxidative stress at alkaline pH . PIMT is monomeric in solution. A crystal structure of PIMT was solved at 1.8 Å resolution . Enzymes containing mutations in glutamate residues that were predicted to be involved in SAM binding retained the ability to bind SAM, but altered the kinetic properties of the enzyme . Overexpression of pcm leads to increased tolerance for thermal stress, likely due to induction of the misfolded protein response . pcm was also isolated as a multicopy suppressor of protein aggregation; this effect was not due to induction of the heat shock response...

## Biological Role

Catalyzes 2.1.1.77-RXN (reaction.ecocyc.2.1.1.77-RXN).

## Annotation

FUNCTION: Catalyzes the methyl esterification of L-isoaspartyl residues in peptides and proteins that result from spontaneous decomposition of normal L-aspartyl and L-asparaginyl residues. It plays a role in the repair and/or degradation of damaged proteins. This enzyme does not act on D-aspartyl residues.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.1.1.77-RXN|reaction.ecocyc.2.1.1.77-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2743|gene.b2743]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7A5`
- `KEGG:ecj:JW2713;eco:b2743;ecoc:C3026_15085;`
- `GeneID:93779263;944923;`
- `GO:GO:0004719; GO:0005737; GO:0030091; GO:0032259`
- `EC:2.1.1.77`

## Notes

Protein-L-isoaspartate O-methyltransferase (EC 2.1.1.77) (L-isoaspartyl protein carboxyl methyltransferase) (Protein L-isoaspartyl methyltransferase) (Protein-beta-aspartate methyltransferase) (PIMT)
