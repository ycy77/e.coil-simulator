---
entity_id: "protein.P69789"
entity_type: "protein"
name: "glvB"
source_database: "UniProt"
source_id: "P69789"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glvB glvC yidN b3682 JW3659"
---

# glvB

`protein.P69789`

## Static

- Type: `protein`
- Source: `UniProt:P69789`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This operon may be cryptic in wild-type K12 strains (Probable). {ECO:0000250, ECO:0000305|PubMed:8019415}. The deduced amino acid sequence of GlvB shows similarity with the IIB domain of various Enzyme II proteins (including NAGE-MONOMER "NagE" - Enzyme II of the N-acetylglucosamine PTS - and PTSG-MONOMER "PtsG" - Enzyme IIBC of the glucose PTS) and contains a conserved cysteine residue (Cys92); the glv operon (glvCBG) may be cryptic in wild type E. coli K-12 . glvB is a pseudogene candidate in E. coli K-12 .

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This operon may be cryptic in wild-type K12 strains (Probable). {ECO:0000250, ECO:0000305|PubMed:8019415}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b3682|gene.b3682]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69789`
- `KEGG:ecj:JW3659;ecoc:C3026_19965;`
- `GO:GO:0005886; GO:0008982; GO:0009401; GO:0016301`
- `EC:2.7.1.-`

## Notes

Phosphotransferase enzyme IIB component GlvB (EC 2.7.1.-) (PTS system EIIB component)
