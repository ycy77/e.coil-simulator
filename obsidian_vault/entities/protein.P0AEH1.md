---
entity_id: "protein.P0AEH1"
entity_type: "protein"
name: "rseP"
source_database: "UniProt"
source_id: "P0AEH1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11689431, ECO:0000269|PubMed:11750129, ECO:0000269|PubMed:11867724, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:11689431, ECO:0000269|PubMed:11750129, ECO:0000269|PubMed:11867724, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rseP ecfE yaeL b0176 JW0171"
---

# rseP

`protein.P0AEH1`

## Static

- Type: `protein`
- Source: `UniProt:P0AEH1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11689431, ECO:0000269|PubMed:11750129, ECO:0000269|PubMed:11867724, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:11689431, ECO:0000269|PubMed:11750129, ECO:0000269|PubMed:11867724, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: A site-2 regulated intramembrane protease (S2P) that cleaves the peptide bond between 'Ala-108' and 'Cys-109' in the transmembrane region of RseA. Part of a regulated intramembrane proteolysis (RIP) cascade. Acts on DegS-cleaved RseA to release the cytoplasmic domain of RseA, residue 'Val-148' of RseA may be required for this. This provides the cell with sigma-E (RpoE) activity through the proteolysis of RseA. Can also cleave sequences in transmembrane regions of other proteins (such as LacY) as well as liberated signal peptides of beta-lactamase, OmpF, LivK, SecM, PhoA, LivJ, OmpC, Lpp and TorA, probably within the membrane. Cleaves FecR within its transmembrane region to release an N-terminal cytoplasmic fragment which binds to sigma factor FecI, allowing it to activate transcription of the fecABCDE operon which mediates ferric citrate transport (PubMed:33865858). {ECO:0000269|PubMed:12183368, ECO:0000269|PubMed:12183369, ECO:0000269|PubMed:15496982, ECO:0000269|PubMed:18268014, ECO:0000269|PubMed:18945679, ECO:0000269|PubMed:21810987, ECO:0000269|PubMed:33865858}. RseP is an integral membrane, zinc-containing site-2 metalloprotease (S2P) which catalyses hydrolytic cleavage of peptide bonds within the hydrophobic lipid bilayer...

## Biological Role

Catalyzes RXN-18678 (reaction.ecocyc.RXN-18678), RXN0-3201 (reaction.ecocyc.RXN0-3201).

## Annotation

FUNCTION: A site-2 regulated intramembrane protease (S2P) that cleaves the peptide bond between 'Ala-108' and 'Cys-109' in the transmembrane region of RseA. Part of a regulated intramembrane proteolysis (RIP) cascade. Acts on DegS-cleaved RseA to release the cytoplasmic domain of RseA, residue 'Val-148' of RseA may be required for this. This provides the cell with sigma-E (RpoE) activity through the proteolysis of RseA. Can also cleave sequences in transmembrane regions of other proteins (such as LacY) as well as liberated signal peptides of beta-lactamase, OmpF, LivK, SecM, PhoA, LivJ, OmpC, Lpp and TorA, probably within the membrane. Cleaves FecR within its transmembrane region to release an N-terminal cytoplasmic fragment which binds to sigma factor FecI, allowing it to activate transcription of the fecABCDE operon which mediates ferric citrate transport (PubMed:33865858). {ECO:0000269|PubMed:12183368, ECO:0000269|PubMed:12183369, ECO:0000269|PubMed:15496982, ECO:0000269|PubMed:18268014, ECO:0000269|PubMed:18945679, ECO:0000269|PubMed:21810987, ECO:0000269|PubMed:33865858}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-18678|reaction.ecocyc.RXN-18678]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-3201|reaction.ecocyc.RXN0-3201]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0176|gene.b0176]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEH1`
- `KEGG:ecj:JW0171;eco:b0176;ecoc:C3026_00805;`
- `GeneID:944871;`
- `GO:GO:0004175; GO:0004222; GO:0005886; GO:0006508; GO:0036460; GO:0043856; GO:0045893; GO:0046872`
- `EC:3.4.24.-`

## Notes

Regulator of sigma-E protease RseP (EC 3.4.24.-) (S2P endopeptidase) (Site-2 protease RseP) (S2P protease RseP) (Site-2-type intramembrane protease)
