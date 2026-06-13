---
entity_id: "protein.P0AEE5"
entity_type: "protein"
name: "mglB"
source_database: "UniProt"
source_id: "P0AEE5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mglB b2150 JW2137"
---

# mglB

`protein.P0AEE5`

## Static

- Type: `protein`
- Source: `UniProt:P0AEE5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex MglABC involved in galactose/methyl galactoside import (Probable). In addition, binds D-galactose and D-glucose and plays a role in the chemotaxis towards these two sugars by interacting with the Trg chemoreceptor (PubMed:3057628, PubMed:4927373). Chemotaxis requires MglB, but not MglA or MglC (PubMed:6294056). {ECO:0000269|PubMed:3057628, ECO:0000269|PubMed:4927373, ECO:0000269|PubMed:6294056, ECO:0000305|PubMed:1719366, ECO:0000305|PubMed:6294056}. MglB is the periplasmic binding protein of a D-galactose / methyl-D-galactoside ABC transport system; ligand bound MglB also interacts with the EG11018 "Trg" sensory protein to mediate taxis to galactose and glucose. mglB mutants are defective in both galactose transport and galactose taxis . mglB mutants are unable to accumulate labeled methyl-β-D-galactopyranoside . mglB+ plasmids synthesize both the precursor and the mature form of galactose binding protein in minicells; chemotaxis towards galactose requires MglB but not MglA or MglC . MglB (purified from E. coli W3092) has a single binding site and binds galactose and glucose with µM affinity . Purified MglB consists of two globular domains joined by three separate peptide segments . D-glucose and D-galactose bind in a cleft between the two domains; bound sugars are detected in their β anomeric form...

## Biological Role

Component of D-galactose / methyl-β-D-galactoside ABC transporter (complex.ecocyc.ABC-18-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex MglABC involved in galactose/methyl galactoside import (Probable). In addition, binds D-galactose and D-glucose and plays a role in the chemotaxis towards these two sugars by interacting with the Trg chemoreceptor (PubMed:3057628, PubMed:4927373). Chemotaxis requires MglB, but not MglA or MglC (PubMed:6294056). {ECO:0000269|PubMed:3057628, ECO:0000269|PubMed:4927373, ECO:0000269|PubMed:6294056, ECO:0000305|PubMed:1719366, ECO:0000305|PubMed:6294056}.

## Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-18-CPLX|complex.ecocyc.ABC-18-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2150|gene.b2150]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEE5`
- `KEGG:ecj:JW2137;eco:b2150;ecoc:C3026_12045;`
- `GeneID:86860325;93775032;949041;`
- `GO:GO:0005509; GO:0006935; GO:0015757; GO:0015765; GO:0016020; GO:0030246; GO:0030288; GO:0055052`

## Notes

D-galactose/methyl-galactoside binding periplasmic protein MglB (D-galactose-binding periplasmic protein) (GBP) (D-galactose/D-glucose-binding protein) (GGBP)
