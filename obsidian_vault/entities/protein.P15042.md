---
entity_id: "protein.P15042"
entity_type: "protein"
name: "ligA"
source_database: "UniProt"
source_id: "P15042"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ligA dnaL lig lop pdeC b2411 JW2403"
---

# ligA

`protein.P15042`

## Static

- Type: `protein`
- Source: `UniProt:P15042`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: DNA ligase that catalyzes the formation of phosphodiester linkages between 5'-phosphoryl and 3'-hydroxyl groups in double-stranded DNA using NAD as a coenzyme and as the energy source for the reaction. It is essential for DNA replication and repair of damaged DNA. LigA is one of two known NAD(+)-dependent DNA ligases, catalyzing the formation of phosphodiester bonds in duplex DNA. LigA ligates duplex DNA in an NAD(+)-dependent fashion . Kinetic evaluations have yielded differing kM values for NAD(+) ranging from 0.7 to 7 μM, a kM for strand breaks of 0.03-0.06 μM and a turnover number of 25 ligations per minute . Participation of fluorescently labeled LigA in the repair of single nucleotide gaps generated during base excision repair (BER) in live E. coli cells has been visualised and quantified . The ligation reaction proceeds via three steps and involves two intermediates - an enzyme-adenylate complex and a DNA adenylate complex . In the absence of DNA, purified E. coli ligase reacts with NAD and forms a stable enzyme-adenylate complex releasing nicotinamide mononucleotide (NMN). Isolated enzyme-adenylate complex can seal single strand breaks in DNA in the absence of NAD; this reaction releases AMP . Once the RNA is completely removed by EG10746-MONOMER, LigA seals the nick . LigA functions as a monomer...

## Biological Role

Catalyzes (deoxyribonucleotide)n:5'-phospho-(deoxyribonucleotide)m ligase (AMP-forming, NMN-forming) (reaction.R00382), DNA-LIGASE-NAD+-RXN (reaction.ecocyc.DNA-LIGASE-NAD_-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03410` Base excision repair (KEGG)
- `eco03420` Nucleotide excision repair (KEGG)
- `eco03430` Mismatch repair (KEGG)

## Annotation

FUNCTION: DNA ligase that catalyzes the formation of phosphodiester linkages between 5'-phosphoryl and 3'-hydroxyl groups in double-stranded DNA using NAD as a coenzyme and as the energy source for the reaction. It is essential for DNA replication and repair of damaged DNA.

## Pathways

- `eco03030` DNA replication (KEGG)
- `eco03410` Base excision repair (KEGG)
- `eco03420` Nucleotide excision repair (KEGG)
- `eco03430` Mismatch repair (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00382|reaction.R00382]] `KEGG` `database` - via EC:6.5.1.2
- `catalyzes` --> [[reaction.ecocyc.DNA-LIGASE-NAD_-RXN|reaction.ecocyc.DNA-LIGASE-NAD_-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2411|gene.b2411]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15042`
- `KEGG:ecj:JW2403;eco:b2411;ecoc:C3026_13405;`
- `GeneID:946885;`
- `GO:GO:0003677; GO:0003911; GO:0005829; GO:0006260; GO:0006281; GO:0046872; GO:0070403`
- `EC:6.5.1.2`

## Notes

DNA ligase (EC 6.5.1.2) (Polydeoxyribonucleotide synthase [NAD(+)])
