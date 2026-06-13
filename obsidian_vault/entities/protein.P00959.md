---
entity_id: "protein.P00959"
entity_type: "protein"
name: "metG"
source_database: "UniProt"
source_id: "P00959"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "metG b2114 JW2101"
---

# metG

`protein.P00959`

## Static

- Type: `protein`
- Source: `UniProt:P00959`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the attachment of L-methionine to tRNA(Met) (PubMed:216545, PubMed:367445, PubMed:4297674, PubMed:4581817, PubMed:7932711). Is required not only for elongation of protein synthesis but also for the initiation of all mRNA translation through initiator tRNA(fMet) aminoacylation (PubMed:216545, PubMed:4581817). MetRS can indeed attach methionine to tRNA(mMet), which supplies methionine for elongation of nascent peptides, and to tRNA(fMet), which supplies formylmethionine for initiation of peptide synthesis (PubMed:216545, PubMed:4581817). However, MetRS charges tRNA(fMet) with a greater efficiency than tRNA(mMet) in several strains of E.coli, suggesting a preference for initiation of new peptides (PubMed:216545). Cannot use D-methionine (PubMed:4297674). {ECO:0000269|PubMed:216545, ECO:0000269|PubMed:367445, ECO:0000269|PubMed:4297674, ECO:0000269|PubMed:4581817, ECO:0000269|PubMed:7932711}.; FUNCTION: In addition, MetRS can reject misactivated homocysteine by a tRNA-independent hydrolysis of the homocysteinyl-AMP intermediate, preventing incorporation of homocysteine into tRNA and proteins (PubMed:2191291, PubMed:7024910). The homocysteinyl-AMP intermediate undergoes an intramolecular cyclization reaction in which the thiolate side chain of homocysteine displaces the AMP group, forming homocysteine-thiolactone and AMP (PubMed:2191291, PubMed:7024910)...

## Biological Role

Component of methionine—tRNA ligase (complex.ecocyc.METG-CPLX).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the attachment of L-methionine to tRNA(Met) (PubMed:216545, PubMed:367445, PubMed:4297674, PubMed:4581817, PubMed:7932711). Is required not only for elongation of protein synthesis but also for the initiation of all mRNA translation through initiator tRNA(fMet) aminoacylation (PubMed:216545, PubMed:4581817). MetRS can indeed attach methionine to tRNA(mMet), which supplies methionine for elongation of nascent peptides, and to tRNA(fMet), which supplies formylmethionine for initiation of peptide synthesis (PubMed:216545, PubMed:4581817). However, MetRS charges tRNA(fMet) with a greater efficiency than tRNA(mMet) in several strains of E.coli, suggesting a preference for initiation of new peptides (PubMed:216545). Cannot use D-methionine (PubMed:4297674). {ECO:0000269|PubMed:216545, ECO:0000269|PubMed:367445, ECO:0000269|PubMed:4297674, ECO:0000269|PubMed:4581817, ECO:0000269|PubMed:7932711}.; FUNCTION: In addition, MetRS can reject misactivated homocysteine by a tRNA-independent hydrolysis of the homocysteinyl-AMP intermediate, preventing incorporation of homocysteine into tRNA and proteins (PubMed:2191291, PubMed:7024910). The homocysteinyl-AMP intermediate undergoes an intramolecular cyclization reaction in which the thiolate side chain of homocysteine displaces the AMP group, forming homocysteine-thiolactone and AMP (PubMed:2191291, PubMed:7024910). {ECO:0000269|PubMed:2191291, ECO:0000269|PubMed:7024910}.

## Pathways

- `eco00450` Selenocompound metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.METG-CPLX|complex.ecocyc.METG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2114|gene.b2114]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00959`
- `KEGG:ecj:JW2101;eco:b2114;ecoc:C3026_11860;`
- `GeneID:946643;`
- `GO:GO:0000049; GO:0004825; GO:0005524; GO:0005829; GO:0006431; GO:0008270; GO:0016020; GO:0042803; GO:0071236`
- `EC:6.1.1.10`

## Notes

Methionine--tRNA ligase (EC 6.1.1.10) (Methionyl transfer RNA synthetase) (Methionyl-tRNA synthetase) (MTS) (MetRS)
