---
entity_id: "protein.P15993"
entity_type: "protein"
name: "aroP"
source_database: "UniProt"
source_id: "P15993"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:3015892, ECO:0000269|PubMed:9150230}; Multi-pass membrane protein {ECO:0000269|PubMed:9150230}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aroP b0112 JW0108"
---

# aroP

`protein.P15993`

## Static

- Type: `protein`
- Source: `UniProt:P15993`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:3015892, ECO:0000269|PubMed:9150230}; Multi-pass membrane protein {ECO:0000269|PubMed:9150230}.

## Enriched Summary

FUNCTION: Permease that is involved in the active transport across the cytoplasmic membrane of all three aromatic amino acids, phenylalanine, tyrosine and tryptophan. {ECO:0000269|PubMed:10735864, ECO:0000269|PubMed:4919744, ECO:0000269|PubMed:9150230}. AroP is an aromatic amino acid permease that is a member of the APC Superfamily of transporters . AroP is referred to as the general aromatic amino acid permease because it is responsible for the transport of all three aromatic amino acids, phenylalanine, tyrosine, and tryptophan, across the inner membrane . Based on the hydrophobicity profile and distribution of charged amino acid residues, AroP was shown to have 12 membrane-spanning regions connected by hydrophilic loops . This topographical model is very similar to that reported for the PheP permease, a phenylalanine-specific transporter, which has 61% amino acid sequence identity with the AroP permease. However, despite their high degree of sequence similarity, the substrate specificities and affinities of the AroP and PheP permeases differ . AroP transports each of the aromatic amino acids with a Km of less than 1 μM . A key residue involved in tryptophan transport is tyrosine at position 103 . Studies with uncouplers of oxidative phosphorylation and with strains deficient in F0F1-ATPase indicate that transport via the AroP system is driven by the proton motive force...

## Biological Role

Catalyzes phenylalanine:proton symport (reaction.ecocyc.TRANS-RXN-56), tryptophan:proton symport (reaction.ecocyc.TRANS-RXN-76), L-tyrosine:proton symport (reaction.ecocyc.TRANS-RXN-77). Transports L-Tryptophan (molecule.C00078), (3R)-β-phenylalanine (molecule.ecocyc.CPD-14474), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Permease that is involved in the active transport across the cytoplasmic membrane of all three aromatic amino acids, phenylalanine, tyrosine and tryptophan. {ECO:0000269|PubMed:10735864, ECO:0000269|PubMed:4919744, ECO:0000269|PubMed:9150230}.

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-56|reaction.ecocyc.TRANS-RXN-56]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-76|reaction.ecocyc.TRANS-RXN-76]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-77|reaction.ecocyc.TRANS-RXN-77]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00078|molecule.C00078]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-14474|molecule.ecocyc.CPD-14474]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0112|gene.b0112]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15993`
- `KEGG:ecj:JW0108;eco:b0112;`
- `GeneID:75202073;946018;`
- `GO:GO:0005302; GO:0005886; GO:0015192; GO:0015196; GO:0015823; GO:0015827; GO:0015828; GO:0022857`

## Notes

Aromatic amino acid transport protein AroP (Aromatic amino acid:H(+) symporter AroP) (General aromatic amino acid permease) (General aromatic transport system)
