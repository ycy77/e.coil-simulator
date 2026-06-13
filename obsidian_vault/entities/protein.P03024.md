---
entity_id: "protein.P03024"
entity_type: "protein"
name: "galR"
source_database: "UniProt"
source_id: "P03024"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "galR b2837 JW2805"
---

# galR

`protein.P03024`

## Static

- Type: `protein`
- Source: `UniProt:P03024`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Repressor of the galactose operon. Binds galactose as an inducer. The "Galactose repressor," GalR, is a DNA-binding transcription factor that represses transcription of the operons involved in transport and catabolism of D-galactose . Synthesis of these operons is induced when E. coli is grown in the presence of inducer (D-galactose) and the absence glucose . The expression of galR is increased only in the presence of inducer . In particular, in the absence of D-galactose, GalR represses the galETKM operon . In this repression system, GalR binds to two operators in the presence of HU, resulting in the formation of a repressor loop . This repressor binds in tandem to inverted repeat sequences that are 16 nucleotides long and possess conserved motifs; each dimer binds to one of these conserved sequences . On the other hand, GalR is highly homologous in its amino acid sequence to GalS (55% identical and 88% similar); apparently both act together and are capable of cross-talk to regulate expression of the gal regulon . For this reason these regulators bind the same operators, in the cis regulatory regions, with different affinities . Also, it has been suggested that the DNA-binding consensus sequences that recognize GalR and GalS are not the same . In the presence of inductor, GalR undergoes a conformational change that reduces its affinity for the operator...

## Biological Role

Component of GalR-D-galactose (complex.ecocyc.MONOMER-52).

## Annotation

FUNCTION: Repressor of the galactose operon. Binds galactose as an inducer.

## Outgoing Edges (11)

- `activates` --> [[gene.b0756|gene.b0756]] `RegulonDB` `C` - regulator=GalR; target=galM; function=-+
- `activates` --> [[gene.b0757|gene.b0757]] `RegulonDB` `C` - regulator=GalR; target=galK; function=-+
- `activates` --> [[gene.b0758|gene.b0758]] `RegulonDB` `C` - regulator=GalR; target=galT; function=-+
- `activates` --> [[gene.b0759|gene.b0759]] `RegulonDB` `C` - regulator=GalR; target=galE; function=-+
- `is_component_of` --> [[complex.ecocyc.MONOMER-52|complex.ecocyc.MONOMER-52]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0756|gene.b0756]] `RegulonDB` `C` - regulator=GalR; target=galM; function=-+
- `represses` --> [[gene.b0757|gene.b0757]] `RegulonDB` `C` - regulator=GalR; target=galK; function=-+
- `represses` --> [[gene.b0758|gene.b0758]] `RegulonDB` `C` - regulator=GalR; target=galT; function=-+
- `represses` --> [[gene.b0759|gene.b0759]] `RegulonDB` `C` - regulator=GalR; target=galE; function=-+
- `represses` --> [[gene.b2837|gene.b2837]] `RegulonDB` `S` - regulator=GalR; target=galR; function=-
- `represses` --> [[gene.b2943|gene.b2943]] `RegulonDB` `C` - regulator=GalR; target=galP; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2837|gene.b2837]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P03024`
- `KEGG:ecj:JW2805;eco:b2837;ecoc:C3026_15580;`
- `GeneID:93779159;947314;`
- `GO:GO:0000976; GO:0003677; GO:0003700; GO:0006012; GO:0006351; GO:0006355; GO:0042802`

## Notes

HTH-type transcriptional regulator GalR (Galactose operon repressor)
