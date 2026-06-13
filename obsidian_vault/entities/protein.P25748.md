---
entity_id: "protein.P25748"
entity_type: "protein"
name: "galS"
source_database: "UniProt"
source_id: "P25748"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "galS b2151 JW2138"
---

# galS

`protein.P25748`

## Static

- Type: `protein`
- Source: `UniProt:P25748`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Repressor of the mgl operon. Binds galactose and D-fucose as inducers. GalS binds to an operator DNA sequence within its own coding sequence (corresponding to residues 15 to 20). The "Galactose isorepressor," GalS, is a DNA-binding transcription factor that represses transcription of the operons involved in transport and catabolism of D-galactose . Synthesis of these operons is induced when E. coli is grown in the presence of the inducer (D-galactose) and the absence glucose . GalS is negatively autoregulated, and its expression is increased in the presence of inducer and glucose . On the other hand, GalS is highly homologous in its amino acid sequence to GalR (55% identical and 88% similar); apparently both act together and are capable of cross-talking to regulate expression of the gal regulon . For this reason these regulators bind the same operators, in the cis regulatory regions, with different affinities. Also, it has been suggested that the DNA-binding consensus sequences that recognize GalR and GalS are not the same . In the presence of an inductor, GalS undergoes a conformational change that reduces its affinity for the operator. Golding et al. showed that GalR is the major repressor of the gal operon...

## Biological Role

Component of GalS-D-galactose (complex.ecocyc.MONOMER-53).

## Annotation

FUNCTION: Repressor of the mgl operon. Binds galactose and D-fucose as inducers. GalS binds to an operator DNA sequence within its own coding sequence (corresponding to residues 15 to 20).

## Outgoing Edges (10)

- `activates` --> [[gene.b0756|gene.b0756]] `RegulonDB` `S` - regulator=GalS; target=galM; function=-+
- `activates` --> [[gene.b0757|gene.b0757]] `RegulonDB` `S` - regulator=GalS; target=galK; function=-+
- `activates` --> [[gene.b0758|gene.b0758]] `RegulonDB` `S` - regulator=GalS; target=galT; function=-+
- `activates` --> [[gene.b0759|gene.b0759]] `RegulonDB` `S` - regulator=GalS; target=galE; function=-+
- `is_component_of` --> [[complex.ecocyc.MONOMER-53|complex.ecocyc.MONOMER-53]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0756|gene.b0756]] `RegulonDB` `S` - regulator=GalS; target=galM; function=-+
- `represses` --> [[gene.b0757|gene.b0757]] `RegulonDB` `S` - regulator=GalS; target=galK; function=-+
- `represses` --> [[gene.b0758|gene.b0758]] `RegulonDB` `S` - regulator=GalS; target=galT; function=-+
- `represses` --> [[gene.b0759|gene.b0759]] `RegulonDB` `S` - regulator=GalS; target=galE; function=-+
- `represses` --> [[gene.b2943|gene.b2943]] `RegulonDB` `C` - regulator=GalS; target=galP; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2151|gene.b2151]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25748`
- `KEGG:ecj:JW2138;eco:b2151;ecoc:C3026_12050;`
- `GeneID:949043;`
- `GO:GO:0000976; GO:0003677; GO:0003700; GO:0006355`

## Notes

HTH-type transcriptional regulator GalS (Mgl repressor and galactose ultrainduction factor)
